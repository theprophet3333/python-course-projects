"""
Напишіть програму, яка запитує ім'я файлу, потім відкриває цей файл і читає його, шукаючи рядки заданої форми:
X-DSPAM-Confidence:    0.8475
Підрахуйте кількість цих рядків і витягніть значення з рухомою крапкою з кожного такого рядка, 
обчисліть середнє арифметичне цих значень і виведіть результат, як показано нижче. 
Не використовуйте функцію sum() або змінну з іменем sum у своєму розв'язку.
Зразок даних можна завантажити за адресою. Під час тестування введіть mbox-short.txt як ім'я файлу.
"""

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
bigcount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    data = line.replace('X-DSPAM-Confidence: ', '')
    count = count + 1
    bigcount = bigcount + float(data)
    data1 = bigcount/count
print("Average spam confidence:", data1)