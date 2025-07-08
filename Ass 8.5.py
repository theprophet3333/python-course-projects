"""
Відкрийте файл mbox-short.txt і прочитайте його рядок за рядком. 
Коли ви знайдете рядок, який починається з 'From', як у цьому рядку:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Ви маєте запарсити рядок From за допомогою методу split() і вивести друге слово у рядку (тобто повну адресу людини, яка надіслала повідомлення). 
Потім виведіть кількість отриманих повідомлень.
Підказка: переконайтеся, що не включаєте рядки, які починаються з 'From:'. 
Також подивіться на останній рядок прикладу даних, щоб дізнатися, як виводити кількість.
"""

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

lst = list()
count = 0
for line in fh:
    if not line.startswith('From '):
        continue
    mails = line.split()
    email = mails[1]
    print(email)
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
