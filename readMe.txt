The Task is:
Create a three tables(User, Competition, entry)

User Table:
***********
id (pk)
name
email
gender
phone number
created_on (datetime autofield)
updated_on (datetime autofield)
is_delete
is_active

Competition Table:
******************
id (pk)
title
social_issue (list)
user_id (FK)
created_on (datetime autofield)
updated_on (datetime autofield)
is_delete
is_active

Entry Table:
*************
id(PK)
name
country
state
how_did_you_hear
Competition_id (FK)
is_entrant_part_of_institution
i_am_part_of
created_on (datetime autofield)
updated_on (datetime autofield)
is_delete
is_active

Tasks:
Create a flask web application
create CRUD opeations for all models
Use postgres tables
create a API which fetch all the entries of that particular user


Project Structure:
------------------
/project
    /migrations
    /User_app
        /__init__.py
        /models.py
        /schemas.py
        /views.py
    /Competition_app
        /__init__.py
        /models.py
        /schemas.py
        /views.py
    /Entry_app
        /__init__.py
        /models.py
        /schemas.py
        /views.py
    app.py
    requirements.txt
    


Run the Migrations:
-------------------
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
flask run       =====> app run 
flask --app app --debug run     =====> run app in debug mode

Note: postmen collection added for your reference.