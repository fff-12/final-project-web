import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

def create_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS class(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS weapon(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                image VARCHAR,
                damage VARCHAR,
                stage VARCHAR,
                craft_elements VARCHAR,
                description VARCHAR)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS armor(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                image VARCHAR,
                defens VARCHAR,
                stage VARCHAR,
                craft_elements VARCHAR,
                description VARCHAR)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS accessories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                bonus VARCHAR,
                damage VARCHAR,
                stage VARCHAR,
                craft_elements VARCHAR,
                description VARCHAR)''')

def fill_db():
    Class = ["meele ","ranger ", "summoner", "magic"]
    Weapon = [
    [
        [
           'Starfury', 'https://terraria.wiki.gg/images/2/2d/Starfury.png?e01256', '25', '', '', '',
           'Blade of Grass', 'https://terraria.wiki.gg/images/thumb/8/85/Blade_of_Grass.png/58px-Blade_of_Grass.png?b18050', '18', '', '', '',
           'Amazon', 'https://terraria.wiki.gg/images/d/db/Amazon.png?6e31c2', '18', '', '', '',
           'Thorn Chakram', 'https://terraria.wiki.gg/images/e/e8/Thorn_Chakram.png?68c31c', '25', '', '', '',
       ],
       [
           'Minishark', 'https://terraria.wiki.gg/images/9/96/Minishark.png?1a8a90', '6', '', '', '',
           'Boomstick', 'https://terraria.wiki.gg/images/e/e1/Boomstick.png?8b821c', '14', '', '', '',
           'Blood Rain Bow', 'https://terraria.wiki.gg/images/1/1e/Blood_Rain_Bow.png?b27c0a', '14', '', '', '',
           'Musket', 'https://terraria.wiki.gg/images/2/2b/Musket.png?11d540', '31', '', '', '',
           'The Undertaker', 'https://terraria.wiki.gg/images/8/83/The_Undertaker.png?edd4e9', '19', '', '', '',
       ],
       [
           'Vampire Frog Staff (1x)', 'https://terraria.wiki.gg/images/3/37/Vampire_Frog_Staff.png?b749bc', '11', '', '', '',
           'Flinx Staff (2x)', 'https://terraria.wiki.gg/images/d/de/Flinx_Staff.png?b1154b', '8', '', '', '',
           'Snapthorn', 'https://terraria.wiki.gg/images/a/a0/Snapthorn.png?701cd0', '18', '', '', '',
           'Leather Whip', 'https://terraria.wiki.gg/images/8/85/Leather_Whip.png?40663e', '14', '', '', '',
       ],
       [
           'Demon Scythe', 'https://terraria.wiki.gg/images/e/e2/Demon_Scythe.png?1d979b', '35', '', '', '',
           'Thunder Zapper', 'https://terraria.wiki.gg/images/1/14/Thunder_Zapper.png?7751e2', '20', '', '', '',
           'Diamond Staff', 'https://terraria.wiki.gg/images/b/b0/Diamond_Staff.png?27d173', '23', '', '', '',
           'Vilethorn', 'https://terraria.wiki.gg/images/5/5c/Vilethorn.png?187463', '10', '', '', '',
       ]
    ],
    [
       [
           'Hive-Five', 'https://terraria.wiki.gg/images/0/0e/Hive-Five.png?bc7c4e', '23', '', '', '',
           'Flamarang', 'https://terraria.wiki.gg/images/b/b8/Flamarang.png?615f9d', '49', '', '', '',
           'Volcano', 'https://terraria.wiki.gg/images/c/cf/Volcano.png?e0c908', '40', '', '', '',
       ],
       [
           'The Bee`s Knees', 'https://terraria.wiki.gg/images/2/21/The_Bee%27s_Knees.png?805784', '23', '', '', '',
           'Star Cannon', 'https://terraria.wiki.gg/images/7/70/Star_Cannon.png?eb100d', '55', '', '', '',
           'Molten Fury', 'https://terraria.wiki.gg/images/e/e4/Molten_Fury.png?682784', '31', '', '', '',
           'Beenades', 'https://terraria.wiki.gg/images/0/02/Beenade.png?85d560', '14', '', '', '',
       ],
       [
           'Imp Staff (1x)', 'https://terraria.wiki.gg/images/7/72/Imp_Staff.png?317f8d', '17', '', '', '',
           'Hornet Staff (1x)', 'https://terraria.wiki.gg/images/4/4f/Hornet_Staff.png?f4cb03', '12', '', '', '',
           'Snapthorn', 'https://terraria.wiki.gg/images/a/a0/Snapthorn.png?701cd0', '18', '', '', '',
           'Houndius Shootius', 'https://terraria.wiki.gg/images/c/c8/Houndius_Shootius.png?ddbd1b', '24', '', '', '',
       ],
       [
           'Demon Scythe', 'https://terraria.wiki.gg/images/e/e2/Demon_Scythe.png?1d979b', '35', '', '', '',
           'Gray Zapinator', 'https://terraria.wiki.gg/images/0/0a/Gray_Zapinator.png?726b11', '42', '', '', '',
           'Bee Gun', 'https://terraria.wiki.gg/images/0/03/Bee_Gun.png?cb3c58', '9', '', '', '',
           'Thunder Zapper', 'https://terraria.wiki.gg/images/1/14/Thunder_Zapper.png?7751e2', '20', '', '', '',
       ]
    ],
    [
       [
           'Night`s Edge', 'https://terraria.wiki.gg/images/thumb/9/98/Night%27s_Edge.png/43px-Night%27s_Edge.png?464d44', '40', '', '', '',
           'Dark Lance', 'https://terraria.wiki.gg/images/thumb/e/ef/Dark_Lance.png/39px-Dark_Lance.png?e430f2', '34', '', '', '',
           'Hive-Five', 'https://terraria.wiki.gg/images/0/0e/Hive-Five.png?bc7c4e', '24', '', '', '',
           'Cascade', 'https://terraria.wiki.gg/images/f/f8/Cascade.png?b7f287', '27', '', '', '',
       ],
       [
           'Star Cannon', 'https://terraria.wiki.gg/images/7/70/Star_Cannon.png?eb100d', '55', '', '', '',
           'Phoenix Blaster', 'https://terraria.wiki.gg/images/a/af/Phoenix_Blaster.png?508d6f', '22', '', '', '',
           'Hellwing Bow', 'https://terraria.wiki.gg/images/d/df/Hellwing_Bow.png?c20680', '30', '', '', '',
           'The Bee`s Knees', 'https://terraria.wiki.gg/images/2/21/The_Bee%27s_Knees.png?805784', '23', '', '', '',
       ],
       [
           'Imp Staff (1x)', 'https://terraria.wiki.gg/images/7/72/Imp_Staff.png?317f8d', '17', '', '', '',
           'Hornet Staff (1x)', 'https://terraria.wiki.gg/images/4/4f/Hornet_Staff.png?f4cb03', '12', '', '', '',
           'Spinal Tap', 'https://terraria.wiki.gg/images/4/4d/Spinal_Tap.png?b45b00', '27', '', '', '',
       ],
       [
           'Demon Scythe', 'https://terraria.wiki.gg/images/e/e2/Demon_Scythe.png?1d979b', '35', '', '', '',
           'Gray Zapinator', 'https://terraria.wiki.gg/images/0/0a/Gray_Zapinator.png?726b11', '42', '', '', '',
           'Aqua Scepter', 'https://terraria.wiki.gg/images/f/ff/Aqua_Scepter.png?8a3c62', '27', '', '', '',
           'Flamelash', 'https://terraria.wiki.gg/images/0/0f/Flamelash.png?fc6def', '32', '', '', '',
       ]
    ]
    ]
    Armor = []
    Accessories = []