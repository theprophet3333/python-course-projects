"""
Напишіть програму, яка читає файл mbox-short.txt і з'ясовує, хто надіслав найбільшу кількість повідомлень. 
Програма шукає рядки «From » і за другим словом цього рядка визначає особу, яка надіслала повідомлення. 
Програма створює словник Python, який зіставляє поштову адресу відправника з кількістю разів, коли вона з'являється у файлі. 
Після того, як словник створено, програма читає його, використовуючи цикл визначення максимального, 
щоб знайти найактивнішого дописувача.
"""

name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("File cannot be opened:", name)
    quit()

counts = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)