## Quest 1
import psycopg2

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="your_db",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)
cursor = conn.cursor()

# Чтение всех строк
cursor.execute("SELECT * FROM your_table;")
rows = cursor.fetchall()
print("Все строки:", rows)

# Чтение одной строки
cursor.execute("SELECT * FROM your_table LIMIT 1;")
row = cursor.fetchone()
print("Одна строка:", row)

# Закрытие соединения
cursor.close()
conn.close()


## Quest 2
import pyodbc

# Подключение к MySQL
conn = pyodbc.connect(
    "DRIVER={MySQL ODBC 8.0 Driver};"
    "SERVER=your_host;"
    "DATABASE=your_db;"
    "UID=your_user;"
    "PWD=your_password;"
)
cursor = conn.cursor()

# Чтение всех строк
cursor.execute("SELECT * FROM your_table;")
rows = cursor.fetchall()
print("Все строки:", rows)

# Чтение одной строки
cursor.execute("SELECT * FROM your_table LIMIT 1;")
row = cursor.fetchone()
print("Одна строка:", row)

# Закрытие соединения
cursor.close()
conn.close()