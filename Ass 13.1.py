"""
Програма запитає URL-адресу, прочитає JSON-дані з цієї адреси за допомогою urllib, 
а потім запарсить і витягне кількість коментарів з JSON-даних, обчислить суму чисел у файлі. 
Цю сумму потрібно ввести у відповідному полі.
"""


import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
if len(url) < 1:
    url = 'https://py4e-data.dr-chuck.net/comments_2220122.json'

lst = []
count = 0
total = 0

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
lst = info.get('comments', [])  # Extract the list of comments
for item in lst:
    print(item.get('count', 0))  # Safely access 'count'
    count = count + 1
    try:
        number = int(item.get('count', 0))
        total = total + number
    except (ValueError, IndexError):
        continue
print('Count: ', count, 'Sum: ', total)

    

