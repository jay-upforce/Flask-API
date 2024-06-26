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
    app.py


Run the Migrations:
-------------------
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
flask run       =====> app run 
flask --app app --debug run     =====> run app in debug mode
