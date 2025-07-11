"""
Відкрийте файл romeo.txt і прочитайте його рядок за рядком. 
Для кожного рядка розбийте його на список слів за допомогою методу split(). 
Програма повинна побудувати список слів. Для кожного слова у кожному рядку перевірте, чи воно вже є у списку, і якщо ні, 
то додайте його до списку. 
Коли програма завершить роботу, відсортуйте і виведіть отримані слова за допомогою методу sort(), як показано у бажаних результатах.

Ви можете завантажити приклад даних за посиланням.
"""

fname = input("Enter file name: ")
try:
    fh = open(fname, 'r')
except:
    print('file cannot be opened', fname)
    quit()
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)