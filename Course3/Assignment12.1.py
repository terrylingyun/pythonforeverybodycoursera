from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
count = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    number = tag.contents[0]
    number = int(number)
    total = total + number
    count = count + 1

print('Count', count)
print('Sum', total)
