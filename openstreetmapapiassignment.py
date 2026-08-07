import urllib.request, urllib.parse, urllib.error
import json,http,ssl

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

while True:
    #Inputs: Embry-Riddle Aeronautical University, Irkutsk State University
    address = input('Enter location: ')
    if len(address) < 1: 
        print('No address...')
        break

    url = serviceurl + urllib.parse.urlencode({'q': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None 


    plus_code = js["features"][0]["properties"]["plus_code"]
    print('Plus code', plus_code)
    formatted = js["features"][0]["properties"]["formatted"]
    print('Plus code', formatted)
json_data = urllib.request.urlopen(url).read()