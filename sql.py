import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Weapons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    weapon_name TEXT NOT NULL,
    img TEXT NOT NULL,
    damage INTEGER NOT NULL,
    info TEXT NOT NULL,
    FOREIGN KEY (class_id) REFERENCES Classes (id)
)
""")

def add_class_via_input(cursor):
    name = input("Enter class name: ")
    cursor.execute(
        "INSERT INTO Classes (name) VALUES (?)",
        (name,)
    )

def add_weapon_via_input(cursor):
    class_id = int(input("Enter class_id: "))
    weapon_name = input("Enter weapon name: ")
    img = input("Enter image URL or path: ")
    damage = int(input("Enter damage: "))
    info = input("Enter info: ")
    cursor.execute(
        "INSERT INTO Weapons (class_id, weapon_name, img, damage, info) VALUES (?, ?, ?, ?, ?)",
        (class_id, weapon_name, img, damage, info)
    )

# add_class_via_input(cursor)
add_weapon_via_input(cursor)
connection.commit()
connection.close()
# /static/img/
# <div class="item-card">
#                 <div class="item-image">
#                   <img src={{weapons1[2][3]}} alt="Дерев'яний меч" />
#                   <div class="stats-boxes">
#                     <div class="stat-box">Шкода: {{weapons1[2][4]}}</div>
#                   </div>
#                 </div>
#                 <div class="item-text">
#                   <div class="item-name">{{weapons1[2][2]}}</div>
#                   <div class="item-desc">{{weapons1[2][5]}}</div>
#                 </div>
#               </div>