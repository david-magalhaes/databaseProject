import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

#consulta = "INSERT INTO users VALUES (NULL, 'david', 'asdf')"
consulta = 'SELECT * FROM users'
result = cursor.execute(consulta)
print(result)

for row in result:
    print(row)

# connection.commit()
connection.close()
