import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

def create_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS weapon(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                class VARCHAR,
                name VARCHAR,
                image VARCHAR,
                damage VARCHAR,
                stage VARCHAR,
                description VARCHAR)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS armor(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                class VARCHAR,
                name VARCHAR,
                image VARCHAR,
                defens VARCHAR,
                stage VARCHAR,
                description VARCHAR)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS accessories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                class VARCHAR,
                name VARCHAR,
                bonus VARCHAR,
                damage VARCHAR,
                stage VARCHAR,
                description VARCHAR)''')

def fill_db():
    Weapon_description = {
        'Starfury': "Зоряна лють — це pre-Hardmode меч, який має 1/4 (25%) шанс знайти в скринях Skyware на Плавучих островах , а також 1/4 (25%) шанс отримати зНебесні ящикиіЛазурні ящики. Під час розмаху він час від часу викликає зірковий снаряд, який падає з неба на курсор. Зірка випромінює світло, завдає ×1,5 шкоди від зброї (37 базової шкоди), але не відкидає , і пробиває один раз. Зірка пройде крізь усі блоки , доки не досягне найнижчого порожнього місця на або над курсором, після чого розіб’ється на наступному блоці, якого вона потрапить. Його найкращий модифікатор — Legendary.",
        'Blade of Grass': "Трав'яний клинок — це pre-Hardmode меч. Під час розмаху він стріляє маленьким зеленим снарядом «Листяна пластинка», який летить угору по колу, залишаючи візуальні частинки листя. Снаряд Leaf Blade може проходити крізь блоки , завдає 25% шкоди зброї (4 базової шкоди), має 20 пробиття броні, проникає через ворогів у радіусі 9375 тайлів і може пробити двох ворогів. І меч, і його снаряди мають 1/4 (25%) шанс завдати негативного ефекту « Отруєння » на 7 секунд після удару. Його найкращий модифікатор — Legendary.",
        'Amazon': "Амазон — це йойо до Hardmode. Його найкращий модифікатор — Божественний або Демонічний. Обидва модифікатори збільшують середню потужність шкоди на однакову величину. Однак Безжалісний може бути кращим, якщо гравець уже має дуже високий шанс критичного удару.",
        'Thorn Chakram':  "Чакрам - це Йо-йо яке може бути зроблено з матеріалів здобутих в Джунглях. Він має велику базову шкоду і тримається в повітрі досить довго, що робить його відмінним вибором для гравців, які користуються йо-йо або зброєю ближнього бою. Чакрам може триматися в повітрі 8.5 секунд. Якщо гравець ризикне, він зможе отримати Чакрам вже за пару днів зі створення світу, бо всі матеріали можуть бути знайдені у підземельних джунглях. Найкращий модифікатор для цього предмета – божественний чи демонічний . Середній показник ушкодження від зброї в обох модифікаторів один і той же.",

        'Minishark': "Міні-акула- це вогнепальна зброя простого режиму , яку можна купити у зброяра за 35 монет. Вона має шанс 1/3 (33,33%) не витратити боєприпаси та найнижчий час використання серед усієї зброї далекого бою простого режиму. Найкращий модифікатор для цього предмета — демонічний , тому що він не має відкидання і тому немає таких модифікаторів, які б вплинули на нього. Він також може мати модифікатор «смертоносний»",
        'Boomstick': "Обріз - Вогнепальна зброя, що рідко зустрічається в Гробниці . Обріз робить відразу три постріли з розкидом, але при цьому витрачає одну кулю. Обріз дуже ефективний на близьких дистанціях, але на далеких розкидах куль різко втрачає ефективність",
        'Blood Rain Bow': 'Кривава злива - це pre-Hardmode, який випускає з небес криваві струмені в кількості 1-3 штук струменів замість стріл . Кожен постріл витрачає лише одну стрілу із інвентарю гравця. Струмені випускаються в напрямку курсору з широким розкидом, але блокуються будь-якими блоками . З шансом 1/8 (12,5%) випадає з блукаючого рибоока і зомбі-тритону . Найкращий модифікатор для цього предмета – нереальний .',
        'Musket': ,
        'The Undertaker': ,
        
        'Vampire Frog Staff': ,
        'Flinx Staff': ,
        'Snapthorn': ,
        'Leather Whip': ,

        'Demon Scythe': ,
        'Thunder Zapper': ,
        'Diamond Staff': ,
        'Vilethorn': ,

        'Hive-Five': ,
        'Flamarang': ,
        'Volcano': ,

        'The Bee`s Knees': ,
        'Star Cannon': ,
        'Molten Fury': ,
        'Beenades': ,

        'Imp Staff': ,
        'Hornet Staff': ,
        'Snapthorn': ,
        'Houndius Shootius': ,

        'Gray Zapinator': ,
        'Bee Gun': ,

        'Night`s Edge': ,
        'Dark Lance': ,
        'Cascade': ,

        'Phoenix Blaster': ,
        'Hellwing Bow': ,

        'Spinal Tap': ,

        'Aqua Scepter': ,
        'Flamelash': ,
    }

    
    Class = ["meele ","ranger ", "summoner", "magic"]
    Weapon = [
    [
        [
           'Starfury', 'https://terraria.wiki.gg/images/2/2d/Starfury.png?e01256', '25', '1', '', '',
           'Blade of Grass', 'https://terraria.wiki.gg/images/thumb/8/85/Blade_of_Grass.png/58px-Blade_of_Grass.png?b18050', '18', '1', '', '',
           'Amazon', 'https://terraria.wiki.gg/images/d/db/Amazon.png?6e31c2', '18', '1', '', '',
           'Thorn Chakram', 'https://terraria.wiki.gg/images/e/e8/Thorn_Chakram.png?68c31c', '25', '1', '', '',
       ],
       [
           'Minishark', 'https://terraria.wiki.gg/images/9/96/Minishark.png?1a8a90', '6', '1', '', '',
           'Boomstick', 'https://terraria.wiki.gg/images/e/e1/Boomstick.png?8b821c', '14', '1', '', '',
           'Blood Rain Bow', 'https://terraria.wiki.gg/images/1/1e/Blood_Rain_Bow.png?b27c0a', '14', '1', '', '',
           'Musket', 'https://terraria.wiki.gg/images/2/2b/Musket.png?11d540', '31', '1', '', '',
           'The Undertaker', 'https://terraria.wiki.gg/images/8/83/The_Undertaker.png?edd4e9', '19', '1', '', '',
       ],
       [
           'Vampire Frog Staff (1x)', 'https://terraria.wiki.gg/images/3/37/Vampire_Frog_Staff.png?b749bc', '11', '1', '', '',
           'Flinx Staff (2x)', 'https://terraria.wiki.gg/images/d/de/Flinx_Staff.png?b1154b', '8', '1', '', '',
           'Snapthorn', 'https://terraria.wiki.gg/images/a/a0/Snapthorn.png?701cd0', '18', '1', '', '',
           'Leather Whip', 'https://terraria.wiki.gg/images/8/85/Leather_Whip.png?40663e', '14', '1', '', '',
       ],
       [
           'Demon Scythe', 'https://terraria.wiki.gg/images/e/e2/Demon_Scythe.png?1d979b', '35', '1', '', '',
           'Thunder Zapper', 'https://terraria.wiki.gg/images/1/14/Thunder_Zapper.png?7751e2', '20', '1', '', '',
           'Diamond Staff', 'https://terraria.wiki.gg/images/b/b0/Diamond_Staff.png?27d173', '23', '1', '', '',
           'Vilethorn', 'https://terraria.wiki.gg/images/5/5c/Vilethorn.png?187463', '10', '1', '', '',
       ]
    ],
    [
       [
           'Hive-Five', 'https://terraria.wiki.gg/images/0/0e/Hive-Five.png?bc7c4e', '23', '2', '', '',
           'Flamarang', 'https://terraria.wiki.gg/images/b/b8/Flamarang.png?615f9d', '49', '2', '', '',
           'Volcano', 'https://terraria.wiki.gg/images/c/cf/Volcano.png?e0c908', '40', '2', '', '',
       ],
       [
           'The Bee`s Knees', 'https://terraria.wiki.gg/images/2/21/The_Bee%27s_Knees.png?805784', '23', '2', '', '',
           'Star Cannon', 'https://terraria.wiki.gg/images/7/70/Star_Cannon.png?eb100d', '55', '2', '', '',
           'Molten Fury', 'https://terraria.wiki.gg/images/e/e4/Molten_Fury.png?682784', '31', '2', '', '',
           'Beenades', 'https://terraria.wiki.gg/images/0/02/Beenade.png?85d560', '14', '2', '', '',
       ],
       [
           'Imp Staff (1x)', 'https://terraria.wiki.gg/images/7/72/Imp_Staff.png?317f8d', '17', '2', '', '',
           'Hornet Staff (1x)', 'https://terraria.wiki.gg/images/4/4f/Hornet_Staff.png?f4cb03', '12', '2', '', '',
           'Snapthorn', 'https://terraria.wiki.gg/images/a/a0/Snapthorn.png?701cd0', '18', '2', '', '',
           'Houndius Shootius', 'https://terraria.wiki.gg/images/c/c8/Houndius_Shootius.png?ddbd1b', '24', '2', '', '',
       ],
       [
           'Demon Scythe', 'https://terraria.wiki.gg/images/e/e2/Demon_Scythe.png?1d979b', '35', '2', '', '',
           'Gray Zapinator', 'https://terraria.wiki.gg/images/0/0a/Gray_Zapinator.png?726b11', '42', '2', '', '',
           'Bee Gun', 'https://terraria.wiki.gg/images/0/03/Bee_Gun.png?cb3c58', '9', '2', '', '',
           'Thunder Zapper', 'https://terraria.wiki.gg/images/1/14/Thunder_Zapper.png?7751e2', '20', '2', '', '',
       ]
    ],
    [
       [
           'Night`s Edge', 'https://terraria.wiki.gg/images/thumb/9/98/Night%27s_Edge.png/43px-Night%27s_Edge.png?464d44', '40', '3', '', '',
           'Dark Lance', 'https://terraria.wiki.gg/images/thumb/e/ef/Dark_Lance.png/39px-Dark_Lance.png?e430f2', '34', '3', '', '',
           'Hive-Five', 'https://terraria.wiki.gg/images/0/0e/Hive-Five.png?bc7c4e', '24', '3', '', '',
           'Cascade', 'https://terraria.wiki.gg/images/f/f8/Cascade.png?b7f287', '27', '3', '', '',
       ],
       [
           'Star Cannon', 'https://terraria.wiki.gg/images/7/70/Star_Cannon.png?eb100d', '55', '3', '', '',
           'Phoenix Blaster', 'https://terraria.wiki.gg/images/a/af/Phoenix_Blaster.png?508d6f', '22', '3', '', '',
           'Hellwing Bow', 'https://terraria.wiki.gg/images/d/df/Hellwing_Bow.png?c20680', '30', '3', '', '',
           'The Bee`s Knees', 'https://terraria.wiki.gg/images/2/21/The_Bee%27s_Knees.png?805784', '23', '3', '', '',
       ],
       [
           'Imp Staff (1x)', 'https://terraria.wiki.gg/images/7/72/Imp_Staff.png?317f8d', '17', '3', '', '',
           'Hornet Staff (1x)', 'https://terraria.wiki.gg/images/4/4f/Hornet_Staff.png?f4cb03', '12', '3', '', '',
           'Spinal Tap', 'https://terraria.wiki.gg/images/4/4d/Spinal_Tap.png?b45b00', '27', '3', '', '',
       ],
       [
           'Demon Scythe', 'https://terraria.wiki.gg/images/e/e2/Demon_Scythe.png?1d979b', '35', '3', '', '',
           'Gray Zapinator', 'https://terraria.wiki.gg/images/0/0a/Gray_Zapinator.png?726b11', '42', '3', '', '',
           'Aqua Scepter', 'https://terraria.wiki.gg/images/f/ff/Aqua_Scepter.png?8a3c62', '27', '3', '', '',
           'Flamelash', 'https://terraria.wiki.gg/images/0/0f/Flamelash.png?fc6def', '32', '3', '', '',
       ]
    ]
    ]
    Armor = []
    Accessories = []

def select(sql, par = None):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    if par:
        cursor.execute(sql, par)
    else:
        cursor.execute(sql)

    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data