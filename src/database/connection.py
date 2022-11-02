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

def init():
    init_user_input = input(
        '_______________________________\n'
        '|WHAT\'S THE MOVE?             |\n'
        '|1 - Create hero              |\n'
        '|2 - Read hero attributes.    |\n'
        '|3 - Update hero attributes.  |\n'
        '|4 - Delete hero              |\n'
        '-------------------------------\n'
        'INPUT A VALID ACTION #\n'
        ' \n')
    print(init_user_input)

init()