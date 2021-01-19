# ____________ВАРИАНТ 2____________

# ----------------Задание с SQLite----------------
# Удалите имя исполнителя (то, которое вы указали при создании таблицы),
# обновите таблицу альбомов (измените издателя у любых 2х альбомов),
# подтвердите изменения. Выберете все записи, подходящие под переданное имя исполнителя,
# воспользуйтесь fetchall() для получения результатов
import sqlite3 as sql

connection = sql.connect("Audios_Homework.db")
cursor = connection.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS Audios_Homework( 
    ID INT PRIMARY KEY,
    title TEXT,
    artist TEXT,
    release_date TEXT,
    publisher TEXT,
    media_type TEXT)""")
coll = []
coll.append(('00001', 'Chto oni znayut?', 'Egor Kreed', '2017', 'Bclack Star inc.', 'Pop'))
coll.append(('00002', 'Holostyak', 'Egor Kreed', '2015', 'Black Star inc.', 'Pop'))
coll.append(('00003', 'One More Light', 'Linkin Park', '2017', 'Warner Brothers Records', 'Alternative'))
coll.append(('00004', 'Victorious', 'Skillet', '2019', '	Atlantic Records', 'Alternative'))
coll.append(('00005', 'Evolve', 'Imagine Dragons', '2017', 'KIDinaKORNER', 'Alternative'))

for elem in coll:
    cursor.execute("INSERT INTO Audios_Homework VALUES(?, ?, ?, ?, ?, ?);", elem)

cursor.execute(""""UPDATE Audios_Homework
    SET artist = NULL
    WHERE title = 'Skillet';""")
cursor.execute(""""UPDATE Audios_Homework
    SET publisher = 'Unknown'
    WHERE artist = 'Egor Kreed';""")
connection.commit()

print("Введите Имя артиста")
name = input()
cursor.execute(f"SELECT * FROM Audios_Homework WHERE artist = '{name}' ;")
all_Results = cursor.fetchall()
for elem in all_Results:
    print(elem)
# ________________________________________________
# ---------------Задание со строкой---------------
# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов. Используйте для решения задачи метод.
#
# Определить количество слов в строке (слова разделены пробелами), воспользуйтесь методом count.

string = "Введённая строка с большим количетсовом пробелом пробел1 пробел2 пробел3 пробел4 пробел5 раз два три ёлочка гори"

# нахождение количества слов произвольным образом
collection = string.split()
print(f"В строке {len(collection)} слов")

# Нахождение количества слов с помощью метода count()
print(f"В строке {string.count(' ') + 1} слов")
# ------------------------------------------------







