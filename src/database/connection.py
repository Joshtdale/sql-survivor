import psycopg
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")

        #===============DONT EDIT ABOVE THIS=========================


# def select_all():
#     table_name = input('ENTER TABLE NAME: ')
#     query = "SELECT * from heroes WHERE name = %s"

#     list_of_heroes = execute_query(query, (table_name,)).fetchall()
#     print(list_of_heroes)
#     for record in list_of_heroes:
#         print(record[1])

# select_all()

def select_all():
    # table_name = input('ENTER TABLE NAME: ')
    query = "SELECT name From heroes"

    list_of_heroes = execute_query(query, )
    # print(list_of_heroes)
    for record in list_of_heroes:
        print(" \n" + 
            record[0]
            )

def select_contestant():
    contestant_name = input('ENTER CONTESTANT\'S NAME: ')
    query = "SELECT * from heroes WHERE name = %s"

    list_of_heroes = execute_query(query, (contestant_name,))
    # print(list_of_heroes)
    for record in list_of_heroes:
        print(record)

def create():
    # print('create works')
    name = input('WHAT IS YOUR NAME: ')
    about_me = input('WHAT DO YOU WANT OTHERS TO KNOW ABOUT YOU: ')
    biography = input('TELL US A LITTLE BIT ABOUT YOURSELF: ')
    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)"
    execute_query(query, (name, about_me, biography))
    print(name + ', ' + biography)
    init()

def read():
    read_function_list = {
        '1': select_all,
        '2': select_contestant
    }
    read_user_input = input(
        '_______________________________________\n'
        '|WHAT\'S THE MOVE?                     |\n'
        '|1 - WHO\'S LEFT ON THE ISLAND         |\n'
        '|2 - SPECIFIC CONTESTANT\'S ATTRIBUTES |\n'
        '|_____________________________________|\n'
        'INPUT A VALID ACTION #\n'
        ' \n')
    read_function_list[read_user_input]()
    init()

def update():
    print('update works')
    init()

def delete():
    name = input('WHICH CHARACTER DO YA WANNA DELETE FROM THIS THANG?: ')
    query = "DELETE FROM heroes WHERE %s = heroes.name"
    execute_query(query, (name,))
    init()


def init():
    user_input = {
        '1': create, 
        '2': read, 
        '3': update, 
        '4': delete
        }

    init_user_input = input(
        '======================================\n'
        '|WHAT\'S THE MOVE?                    |\n'
        '|1 - Create contestant               |\n'
        '|2 - Read contestant attributes.     |\n'
        '|3 - Update contestant attributes.   |\n'
        '|4 - Vote a contestant off the Island|\n'
        '|____________________________________|\n'
        'INPUT A VALID ACTION #\n'
        ' \n')
    user_input[init_user_input]()

def logo():
    print('\nTHIS TIME ON...')
    print('  _____                  _                     \n '    
'/  ___|                (_)                 \n'
' \ `--. _   _ _ ____   _____   _____  _ __  \n'
'  `--. \ | | | \'__\ \ / / \ \ / / _ \| \'__| \n'
' /\__/ / |_| | |   \ V /| |\ V / (_) | |    \n'
' \____/ \__,_|_|    \_/ |_| \_/ \___/|_|    \n'
'  Feat. Wu-Tang                       \n')
    

logo()

init()