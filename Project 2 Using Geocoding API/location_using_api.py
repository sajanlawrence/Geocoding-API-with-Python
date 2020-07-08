import urllib.request,urllib.parse,urllib.error
import json
import ssl

api_key = False
#if you have a Google Places API key, enter it here
#api_key = 'enter here'

if api_key is False:
	api_key = 42
	serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
	serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while(True):
	address = input("Enter The Address: ")
	if len(address) < 1 :
		break
	param = dict()
	param['address'] = address
	if api_key is not False:
		param['key'] = api_key
	url = serviceurl + urllib.parse.urlencode(param)
	print("Retrieving",url)#http://py4e-data.dr-chuck.net/json?address=thrissur%2Ckerala&key=42
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print("Retrieved",len(data),'characters')
	try:
		js = json.loads(data) # we get a dictionary of tree object form
	except:
		js = None
	if not js or 'status' not in js or js['status'] != 'OK':
		print("===Failed to Retrieve===")
		print(data)
		continue
	#print(js)
	print(json.dumps(js,indent=4)) #opposite of loads or same as print(data)
	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	print('lat', lat, 'lng', lng)
	location = js['results'][0]['formatted_address']
	print(location)
    


