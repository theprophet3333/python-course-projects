"""
Напишіть програму, яка обчислить номінальну заробітну плату користувача відповідно до кількості робочих годин і ставки на годину. 
При тестуванні зазначте 35 годин та ставку 2.75 за годину (зарплата має бути 96.25). 
Ви маєте застосувати input  для читання рядка і float(), аби перетворити рядок на число. 
Не зважайте на перевірку помилок або некоректні дані від користувача.
"""

inp = input("Enter a number: ")
inp2 = input("Enter a rate:")
print('Pay:',float(inp) * float(inp2))