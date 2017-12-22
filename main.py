#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import subprocess
import sys
import time
import os

import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType

from visor import where_am_i, get_direction, capture
from led_visor import init_output, light

LED_PIN = 32

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))

def find_current_location():
    current_location = where_am_i()
    aiy.audio.say(current_location)

def find_direction(destination):
    print(destination)
    directions = get_direction(destination)

    for direction in directions:
        instruction = direction['instruction']
        duration = direction['duration']

        os.system('google_speech -l id "%s" -e delay 1' % instruction)
        #aiy.audio.say(instruction)
        time.sleep(int(duration))

def detect_object():
    objects = capture()
    print(objects)

    text = 'there are '
    for object in objects:
        if objects[object] > 1:
           text += '{} {}s,'.format(objects[object], object)
        else:
           text += '{} {}, '.format(objects[object], object)

    text += ' in front of you'
    print(text)

    aiy.audio.say(text)

def get_time():
    time = subprocess.check_output('date "+%H:%M %p"', shell=True).decode('utf-8')
    print(time)
    aiy.audio.say("the time is " + str(time))


def process_event(assistant, event):
    #status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        #status_ui.status('ready')
        light(LED_PIN, 'on')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    #elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        #status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        print(text)
        if 'location' in text:
            assistant.stop_conversation()
            find_current_location()
        elif 'direction to' in text:
            assistant.stop_conversation()
            destination = text.split('direction to')[-1]
            find_direction(destination)
        elif 'what am i seeing' in text or 'vision' in text:
            assistant.stop_conversation()
            detect_object()
        elif 'what time is it' in text:
            assistant.stop_conversation()
            get_time()

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        light(LED_PIN, 'off')
        #status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        light(LED_PIN, 'on')
        #status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    init_output([LED_PIN])
    light(LED_PIN, 'on')
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
