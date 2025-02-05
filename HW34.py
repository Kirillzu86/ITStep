import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="your_db",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)
cursor = conn.cursor()

# Создание таблицы (если ее нет)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
""")
conn.commit()

# Функция CREATE (Добавление записи)
def create_user(name, age):
    try:
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s);", (name, age))
        conn.commit()  # Фиксация транзакции
        print("User added successfully")
    except Exception as e:
        conn.rollback()  # Откат в случае ошибки
        print("Error:", e)

# Функция READ (Чтение всех записей)
def read_users():
    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()

# Функция READ (Чтение одной записи)
def read_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
    return cursor.fetchone()

# Функция UPDATE (Обновление данных)
def update_user(user_id, new_name, new_age):
    try:
        cursor.execute("UPDATE users SET name = %s, age = %s WHERE id = %s;", (new_name, new_age, user_id))
        conn.commit()
        print("User updated successfully")
    except Exception as e:
        conn.rollback()
        print("Error:", e)

# Функция DELETE (Удаление записи)
def delete_user(user_id):
    try:
        cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        conn.commit()
        print("User deleted successfully")
    except Exception as e:
        conn.rollback()
        print("Error:", e)

# Тестирование CRUD
create_user("Alice", 25)
create_user("Bob", 30)

print("All users:", read_users())

print("Single user:", read_user(1))

update_user(1, "Alice Cooper", 26)
print("Updated user:", read_user(1))

delete_user(2)
print("Users after deletion:", read_users())

# Закрытие соединения
cursor.close()
conn.close()
