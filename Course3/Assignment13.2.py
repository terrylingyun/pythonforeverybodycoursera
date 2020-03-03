import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('User count:', len(info['comments']))
total = 0
for item in info['comments'] :
    count = int(item['count'])
    total = total + count
print('Sum:', total)
