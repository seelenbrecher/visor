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

import aiy
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat


def main():
    aiy.i18n.set_language_code('id-ID')
    recognizer = aiy.cloudspeech.get_recognizer()
    
    # Ga pake hotwords, manual aja
    # recognizer.expect_hotwords(['Visor', 'Oke, Visor', 'OK, Visor'])
    
    # Train
    training_phrases = ['dimana saya', 'arahkan saya', 'universitas indonesia', 'pondok cina', 'margo city']
    for phrase in training_phrases:
        print('Training for the phrase: {}'.format(phrase))
        recognizer.expect_phrase(phrase)')

    aiy.audio.get_recorder().start()

    while True:
        # Tapi disini perlu hotwords / trigger apapun
        text = recognizer.recognize()
        if not text:
            aiy.audio.say('Maaf, bisa diulangi?')
        else:
            if 'dimana' in text:
                # ini panggil yang di main
                pass
            elif 'arahkan' in text:
                aiy.audio.say('Oke, kemana?')
                location = recognizer.recognize()
                # ini direction


if __name__ == '__main__':
    main()
