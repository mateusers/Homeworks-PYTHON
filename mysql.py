import pymysql

db = pymysql.connect('127.0.0.1', 'master2', '123456', 'mydb')

cursor = db.cursor()
while True:
    print('''Добро пожаловать в Tottenham!\nЧтобы просмотреть стартовый состав команды, напишите 'show'.
    Чтобы редактировать состав команды введите 'edit'.
Чтобы добавить игроков введите 'add'.
Чтобы удалить игрока введите 'delete'.
Для выхода из базы данных напишите 'exit'.''')
    x = input("Введите значение: ")
    if x == 'show':

        cursor.execute("SELECT * FROM mydb.players;")
        db = cursor.fetchall()

        print(*db, sep="\n")

    elif x == 'add':

         sur=input('Введите фамилию игрока: ')
         name=input('Введите имя игрока: ')
         pos=input('Введите позицию игрока: ')
         num=int(input('Ведите номер игрока: '))

         cursor.execute("INSERT INTO `mydb`.`players` (`Surname`, `Name`, `Position`, `Number`) VALUES (%s, %s, %s, %s);",
                        (sur, name, pos, num))
         print('Игрок добавлен в состав команды')

    elif x == 'edit':

        id = input("Введите ID игрока для изменения: ")
        sur = input('Введите фамилию игрока: ')
        name = input('Введите имя игрока: ')
        pos = input('Введите позицию игрока: ')
        num = int(input('Ведите номер игрока: '))

        upd = cursor.execute("UPDATE `mydb`.`players` SET `Surname` = '%s', `Name` = '%s', `Position` = '%s', `Number` = '%s' WHERE (`Player` = '%s');",
                             (sur, name, pos, num))

        cursor.execute(upd)
        cursor.execute("SELECT * FROM mydb.players;")
        print("Игрок изменен")

    elif x == 'delete':
        id = input("Введите ID игрока для его удаления из команды: ")

        upd = cursor.execute("DELETE FROM `mydb`.`players` WHERE (`Player` = '%s');",
                             (id))
        cursor.execute(upd)
        cursor.execute("SELECT * FROM mydb.players;")
        print("Игрок удален из команды")

    elif x == 'exit':
        break

db.commit()

db.close()