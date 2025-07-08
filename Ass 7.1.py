"""
Напишіть програму, яка запитує ім'я файлу, відкриває цей файл, читає його і виводить вміст файлу у верхньому регістрі. 
Використовуйте файл words.txt для виведення наведених даних.
Зразки даних можна завантажити на сайті.
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
print(str.rstrip(str.upper(fhand.read())))