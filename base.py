from boltiot import Bolt
import time
api_key = "445c90a1-ce8b-4621-99c1-ce356fb17eef"
device_id  = "BOLT6094114"
mybolt = Bolt(api_key, device_id)
response = mybolt.digitalWrite('0', 'HIGH')
print(response)
time.sleep(5)
response = mybolt.digitalWrite('0','LOW')
print (response)