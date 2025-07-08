"""
Програма запитає URL-адресу, прочитає XML-дані з цієї адреси за допомогою urllib,
а потім запарсить і витягне кількість коментарів з XML-даних, обчислить суму чисел у файлі.
"""

import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'https://py4e-data.dr-chuck.net/comments_2220123.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

lst = []

total = 0
lst = tree.findall('.//count')

for item in lst:
    try:
        number = int(item.text)
        total += number
    except (ValueError, IndexError, TypeError):
        continue
print(len(lst), total)

