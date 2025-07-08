'''
SELECT sha1(CONCAT(name,age)) AS X FROM Ages ORDER BY X команда не підтримується моїм браузером скл, поміг чатжпт
'''



import sqlite3
import hashlib

# Підключення до вашої SQLite-бази
conn = sqlite3.connect('SQL 1 ASS.db')  # заміни на назву свого .db-файлу
cur = conn.cursor()

# Отримуємо name та age з таблиці Ages
cur.execute('SELECT name, age FROM Ages')
rows = cur.fetchall()

# Створюємо список з кортежами (sha1, name, age)
hashed_rows = []
for name, age in rows:
    combined = f"{name}{age}"
    sha1_hash = hashlib.sha1(combined.encode()).hexdigest()
    hashed_rows.append((sha1_hash, name, age))

# Сортуємо за хешем
hashed_rows.sort()

# Виводимо результат
for sha1_hash, name, age in hashed_rows:
    print(f"{sha1_hash} - {name}, {age}")

# Закриваємо з'єднання
conn.close()