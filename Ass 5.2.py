"""
Напишіть програму, яка просить користувача вводити цілі числа допоки користувач не зазначить «готово» (“done”). 
Після введення «готово» (“done”), виведіть найбільше та найменше з введених чисел. 
Якщо користувач вводить некоректне число, обробіть його за допомогою try / except, виведіть на екран відповідне повідомлення, 
та проігноруйте це число. 
Виведіть 7, 2, bob, 10, і 4, та порівняйте з наведеними нижче результатами.
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = float(num)
    except ValueError:
        print('Invalid input')
        continue
    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", int(largest))
print("Minimum is", int(smallest))