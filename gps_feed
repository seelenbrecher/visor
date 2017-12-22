from module_gps import get_lat_lng
import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration


PUB_KEY = 'pub-c-b06e92d9-fa30-4b16-817f-c7c63bffc96e'
SUB_KEY = 'sub-c-0c92ef92-e646-11e7-a966-520fb0a815a8'

pnconfig = PNConfiguration()
pnconfig.publish_key = PUB_KEY
pnconfig.subscribe_key = SUB_KEY

pubnub = PubNub(pnconfig)
channel = 'pi-visor'

def on_publish(result, status):
	if not status.is_error():
		print('[+] Successfully published.')
	else:
		print('[-] Error publishing')



if __name__ == "__main__":

	while True:
		lat, lng = get_lat_lng()

		data = {
			'latitude': lat,
			'longitude': lng
		}

		pubnub.publish().channel(channel).message(data).async(on_publish)

		time.sleep(10)
