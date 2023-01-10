## SQL Heros


**Requirements**

Create, read, update and delete

1. Create a Connection to a gitpod Database using Python 3 and view the database (using pgAdmin)
    * PostgreSQL: Username “postgres” / Password “postgres”
    * pgAdmin: Username “bootcamp@awesomeinc.org” / Password “awesome”
2. The supplied superheroes.sql Database file contains create table and insert statements to get you started. (Do not modify the SQL file directly. Use CRUD operations to achieve CRUD)
3. Decide on a minimum of four CRUD operations you wish to implement (at least one operation for Create, Read, Update, & Delete) - document these in your README.md
4. Raise proper errors for defensive programming.
5. Interactive creation, update, delete of a hero in the terminal via Python script, with commands that are available for the README.md


Python template
Sql-heros

Pip —version
Pip install psycopg
Pip freeze > requirements.txt
Pip install -r

### Pseudocode:

init():
    Initialize menu for picking one of the crud functions
    user input selects function for specific task

    based on input
        create()
        read()
        update()
        delete()



create():
    user input name, about me, bio


read():
    select {user input}


update():
    update user input hero.name value user input value


delete():
    delete user input hero.name
