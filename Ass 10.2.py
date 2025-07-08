"""
Напишіть програму, яка прочитає файл mbox-short.txt і визначить розподіл по годинах доби для кожного з повідомлень. 
Ви можете витягнути годину з рядка 'From ', знайшовши час і розділивши рядок вдруге двокрапкою.
From stephen.marquard@uct.ac.za Sat Jan  5 #09#:14:16 2008
Після того, як ви накопичили кількість повідомлень для кожної години, виведіть їх, 
відсортовані за годинами, як показано нижче (у бажаному результаті).
"""

fname = input("Enter file: ")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)

hours_count = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        hours_count[hour] = hours_count.get(hour, 0) + 1

sorted_hours = sorted(hours_count.items())

for hour, count in sorted_hours:
    print(hour, count)

