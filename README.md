*This project, as well as [Sport](https://github.com/mykola-kond-73/sport), are projects written on the Django framework*

----

## Startup order

First you need to create a virtual environment with the command **`python -m venv <new_dir_name_with_venv>`**.

Next, go to the directory with the virtual environment and activate his team **`.\Scripts\activate`**.
To deactivate the virtual environment, enter the **`deactivate`** command.

After activating the virtual environment, you need to install Django with the command **`pip install django djoser django-ranged-response django-simple-captcha django-cors-headers django-debug-toolbar Pillow coreapi coreschema Jinja2 MarkupSafe`**.

After go to the coolsite directory with the **`cd coolsite`** command.

Next, run the command **`python manage.py runserver`** to start the server

----

### PostgreSQL database is used here
You need to recreate the database from the dump **(db_dump.sql file)**

### Super user in admin panel
login:*admin*
pass:*admin*  