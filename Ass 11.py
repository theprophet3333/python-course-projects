'''
У цій вправі вам потрібно буде прочитати та запарсити файл з текстом та числами. 
Ви повинні витягти всі числа з файлу та обчислити їхню суму.
Основна схема цієї задачі полягає у читанні файлу, пошуку цілих чисел за допомогою функції re.findall(), 
пошуку регулярного виразу '[0-9]+ ', 
а потім перетворенні витягнутих рядків на цілі числа і підсумовуванні цілих чисел.
'''

#Варіант Сані

#import re

#hand = open('Actual data.txt').read()

#numbers = re.findall('[0-9]+', hand)
#sum_of_numbers = 0
#for number in numbers :
#    sum_of_numbers += int(number)
#print(sum_of_numbers)

#Варіант для розваги, в одній строці

#import re

#print(sum([int(n) for n in re.findall("\\d+", open("Actual data.txt").read())]))



import re

hand = open('Actual data.txt')
lst = []
sum_of_nums = 0
for line in hand :
    matched_numbers = re.findall('[0-9]+', line)
    lst = lst + matched_numbers

for number in lst:
    sum_of_nums = sum_of_nums + int(number)

print(sum_of_nums)



   


   




