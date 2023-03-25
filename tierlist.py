import sqlite3

def tierlist():
    try:
        # тут возможно поменять на DB_NAME
        # или вообще просто функцию вызвать
        sqlite_connection = sqlite3.connect('yandexbot.db')
        cursor = sqlite_connection.cursor()

        cursor.execute("SELECT name, progress, balance FROM user ORDER BY balance DESC LIMIT 10")
        record = cursor.fetchall()
        cursor.close()

        columns = ["Имя ", "Прогресс ", "Баланс "] # шапка таблицы
    
        max_columns = [] # список максимальной длинны колонок
        for col in zip(*record):
            len_el = []
            [len_el.append(len(str(el))) for el in col]
            max_columns.append(max(len_el))


        # печать шапки таблицы
        for column in columns:
            print(f'{column:{max(max_columns)+1}}', end='')
        print()
        # печать разделителя шапки
        print(f'{"="*max(max_columns)*4}')
        # печать тела таблицы
        for el in record:
            for col in el: 
                print(f'{col:{max(max_columns)}}', end='')
            print()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

