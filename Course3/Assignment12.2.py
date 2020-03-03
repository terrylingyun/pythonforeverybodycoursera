import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input ('Enter position: ')
times = 0
count = int(count)
position = int(position)
print('Retrieving:', url)

while times < count :
    times = times + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    links = list()
    for tag in tags:
        links.append(tag.get('href', None))
    url = links[position - 1]
    print('Retrieving:', url)
