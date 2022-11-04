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

wu_tang_forever = {'████████████████████████████████████████\n'
'████████████████████████████████████████\n'
'███████████████████████████████▜████████\n'
'████████▜██████████████████▛▀▖▗▗▜███████\n'
'███████▘▗ ▖▝▝▀▀█████████▛▀▖▝▗▝ ▖ ▜██████\n'
'██████▛ ▘▗ ▘▘▘▘ ▗▟████▛▗ ▘ ▘▖▖▘▖▘▖██████\n'
'██████ ▘▝▗▝ ▘▝▗▘███████▌▝▝▝▗ ▖▘▗▗▗▐█████\n'
'█████▌▘▘▘▖▝▝▝▝ ▖██▀▘▖▀█▛▖▘▝▗▝ ▝ ▖▗▝█████\n'
'█████▌▘▝▗ ▚▝ ▘▘▖▜▙▘▘▗▝▜▘▖▘▘▖▖▘▘▘▖▖▝█████\n'
'█████▚▜▛▟█▞▐▜▙▚▙▙▙▜▝▘▚█▙▚█▞▝▞▟█▟▞▞▚█████\n'
'█████▙▜█▗█▚█▗█▙▞█▜█▛▟█▞▟▜▝█▀█▙▐▚▛▛▜█████\n'
'██████▙▟▙▟██▙██▟███▙▟█▙██▙█▟██▟▙██▟█████\n'
'█████▙▗ ▖▖ ▖▗  ▖▗ ▖▗▟▙▖▗ ▖▖▗  ▗   ▟█████\n'
'██████▌▗▗ ▘▗▗▝▗▗▗▗▗ ███▗▝ ▖▖▝▝▗▝▝▐██████\n'
'███████▄▗▝▝ ▖▝ ▖▗ ▖▝███▙ ▘▗ ▘▞ ▖▘███████\n'
'████████▙ ▘▘ ▘▝▗ ▖▖▘▐███▞▝▗▝▗ ▖▖████████\n'
'██████████▙▞▝▝▝ ▖▖▖▘▖▐██▙▘▖▗▗▝▗█████████\n'
'█████████████▙▙▟▄▗▗▄▖▙▟█▙▗ ▘▄▟██████████\n'
'████████████████████████▛▄▟█████████████\n'
'████████████████████████████████████████\n'}

# def select_all():
#     table_name = input('ENTER TABLE NAME: ')
#     query = "SELECT * from heroes WHERE name = %s"

#     list_of_heroes = execute_query(query, (table_name,)).fetchall()
#     print(list_of_heroes)
#     for record in list_of_heroes:
#         print(record[1])

# select_all()



def create():
    # print('create works')
    name = input('WHAT IS YOUR NAME: ')
    about_me = input('WHAT DO YOU WANT OTHERS TO KNOW ABOUT YOU: ')
    biography = input('TELL US A LITTLE BIT ABOUT YOURSELF: ')
    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)"
    execute_query(query, (name, about_me, biography))
    print(name + ', ' + biography)
    init()



# Read functions
def select_all():
    query = "SELECT name From heroes"

    list_of_heroes = execute_query(query, )
    for record in list_of_heroes:
        print(" \n" + 
            record[0]
            )

    
def select_powers(name):
    query = """SELECT ability_types.name 
    FROM heroes 
    JOIN abilities ON heroes.id = abilities.hero_id 
    JOIN ability_types ON ability_types.id = abilities.ability_type_id 
    WHERE heroes.name = %s"""
    list_of_heroes = execute_query(query, (name,))
    for record in list_of_heroes:
        print('\n________ \n' + record[0] + '\n________ \n')
    # attribute = input('ABOUT_ME? Biography?')
    # query = "SELECT %s from heroes WHERE name = %s"
    # list_of_heroes = execute_query(query, (attribute, name))
    # for record in list_of_heroes:
    #     print(record[0])

def select_all_attributes(name):
    query = "SELECT * from heroes WHERE name = %s"
    list_of_heroes = execute_query(query, (name,))
    for record in list_of_heroes:
        print(record)

def select_contestant():
    contestant_name = input('ENTER CONTESTANT\'S NAME: ')
    selection_list = {
        '1': select_powers,
        '2': select_all_attributes
    }
    user_selection = input(
        '========================================\n'
        '|WHAT\'S THE MOVE?                      |\n'
        '|1 - VIEW POWERS                       |\n'
        '|2 - VIEW ALL ATTRIBUTES.              |\n'
        # '|3 - BACK TO MAIN MENU.                 |\n'
        '|______________________________________|\n'
        'INPUT A VALID ACTION #\n'
        ' \n')
    if int(user_selection) in range(1, 3):
        selection_list[user_selection](contestant_name)
    elif int(user_selection) > 2:
        read()
    elif int(user_selection) is 0:
        read()
    



def read():
    read_function_list = {
        '1': select_all,
        '2': select_contestant,
        '3': init
    }

    read_user_input = input(
        '========================================\n'
        '|WHAT\'S THE MOVE?                      |\n'
        '|1 - WHO\'S LEFT ON THE ISLAND          |\n'
        '|2 - SPECIFIC CONTESTANT\'S ATTRIBUTES  |\n'
        '|3 - BACK TO MAIN MENU.                |\n'
        '|______________________________________|\n'
        'INPUT A VALID ACTION #\n'
        ' \n')
    if int(read_user_input) in range(1, 4):
        read_function_list[read_user_input]()
    elif int(read_user_input) > 3:
        read()
    elif int(read_user_input) is 0:
        read()
    

    init()



# Update functions
def update_name():
    name = input('WHICH CONTESTANT\'S NAME DO YA WANNA UPDATE?: ')
    old_name = "SELECT * FROM heroes WHERE %s = heroes.name"
    older_name = execute_query(old_name, (name,))
    for item in older_name:
        print( '\n' + 'OLD NAME: ' + f"{item[1]}" + '\n')
    new_name = input('ENTER NEW NAME: ')
    query = "UPDATE heroes SET name = %s WHERE %s = heroes.name "
    execute_query(query, (new_name, name))

def update_about():
    name = input('WHICH CONTESTANT\'S ABOUT DO YA WANNA UPDATE?: ')
    old_about = "SELECT about_me FROM heroes WHERE %s = heroes.name"
    older_about = execute_query(old_about, (name,))
    for about in older_about:
        print( '\n' + 'OLD ABOUT: ' + f"{about[0]}" + '\n')
    new_about = input('ENTER NEW ABOUT: ')
    query = "UPDATE heroes SET about_me = %s WHERE %s = heroes.name "
    execute_query(query, (new_about, name))

def update_bio():
    name = input('WHICH CONTESTANT\'S BIO DO YA WANNA UPDATE?: ')
    old_bio = "SELECT biography FROM heroes WHERE %s = heroes.name"
    older_bio = execute_query(old_bio, (name,))
    for bio in older_bio:
        print( '\n' + 'OLD BIO: ' + f"{bio[0]}" + '\n')
    new_bio = input('ENTER NEW BIO: ')
    query = "UPDATE heroes SET biography = %s WHERE %s = heroes.name "
    execute_query(query, (new_bio, name))

def update_power():
    name = input('WHICH CONTESTANT\'S POWER DO YA WANNA UPDATE?: ')
    select_powers(name)
    new_ability = input('WHAT KINDA POWERS DOES THIS BOY GOT?: ')
    query = """UPDATE ability_types.name = %s 
    FROM heroes 
    JOIN abilities ON heroes.id = abilities.hero_id 
    JOIN ability_types ON ability_types.id = abilities.ability_type_id 
    WHERE heroes.name = %s"""
    select_powers(name)
    # list_of_heroes = execute_query(query, (new_ability, name))
    # for record in list_of_heroes:
    #     print('\n________ \n' + record[0] + '\n________ \n')

def update():
    update_function_list = {
        '1': update_name,
        '2': update_about,
        '3': update_bio,
        '4': update_power,
        '5': init
    }
    update_user_input = input(
        '========================================\n'
        '|WHAT\'S THE MOVE?                      |\n'
        '|1 - UPDATE A CONTESTANT\'S NAME        |\n'
        '|2 - UPDATE A CONTESTANT\'S ABOUT.      |\n'
        '|3 - UPDATE A CONTESTANT\'S BIO.        |\n'
        '|4 - UPDATE A CONTESTANT\'S POWER.      |\n'
        '|5 - BACK TO MAIN MENU.                |\n'
        '|______________________________________|\n'
        'INPUT A VALID ACTION #\n'
        ' \n')
    # try:
    #     update_function_list[update_user_input]()
    # except:
    #     update()
        # print('INVALID COMMAND YOU FOOL')
    if int(update_user_input) in range(1, 5):
        update_function_list[update_user_input]()
    elif int(update_user_input) > 5 or int(update_user_input) == 0:
        update()
    # elif int(update_user_input) is 0:
    #     update()
    



    init()



def delete():
    name = input('WHICH CHARACTER DO YA WANNA DELETE FROM THIS THANG?: ')
    confirmation = input('ARE YOU SURE YOU WANT TO VOTE ' + name + ' OFF??')
    if confirmation.lower() == 'no' or confirmation.lower() == 'back':
        init()
    else:
        query = "DELETE FROM heroes WHERE %s = heroes.name"
        execute_query(query, (name,))
    

    init()


def init():
    user_input = {
        '1': create, 
        '2': read, 
        '3': update, 
        '4': delete,
        '5': init
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
    if int(init_user_input) in range(1, 5):
        user_input[init_user_input]()
    elif int(init_user_input) > 4:
        init()
    elif int(init_user_input) is 0:
        init()

def logo():
    # print(wu_tang_forever[0])
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