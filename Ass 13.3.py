"""
Програма запитає місцезнаходження, зв'яжеться з вебсервісом і отримає JSON для вебсервісу, 
запарсить ці дані і отримає перший plus_code з JSON

Ця хуйня не працювала в зразку opengeo.py, я хз чого працює тут, код написав чатжпт, але він майже ідентичний тому з урока.
"""
# Monterrey Institute of Technology and Higher Education

import urllib.request, urllib.parse
import json, ssl

# API endpoint
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# SSL context to handle HTTPS
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Prompt for location
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # Prepare the URL with the encoded parameters
    parms = {'q': address.strip()}
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    try:
        # Retrieve data from the API
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')
    except Exception as e:
        print('Error retrieving data:', e)
        continue

    try:
        # Parse JSON data
        js = json.loads(data)
    except json.JSONDecodeError:
        print('Failed to parse JSON')
        continue

    # Check if the response contains valid data
    if not js or 'features' not in js or len(js['features']) == 0:
        print('==== Object not found or invalid response ====')
        continue

    # Extract the plus_code from the first feature
    properties = js['features'][0].get('properties', {})
    plus_code = properties.get('plus_code')

    if plus_code:
        print('Plus Code:', plus_code)
    else:
        print('Plus Code not found')

    # Print the full properties for debugging
    print(json.dumps(properties, indent=4))