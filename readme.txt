this is the test phrase (returns if oxygen issue) and this is the accepted format for call:
{"spo2":95,"pulse":84}

-------------------
"modelVenv" is the virtualEnvironment for this project
to use virtualEnv: command1: cd to modelVenv/Scripts 
	           command2: activate

--------------
#venv Creation: 
1. python -m venv env_name // "D:/softwares/Python 3.12.4/python.exe" -m venv modelVenv
2. cd Scripts -> activate.bat
3. pip list #to list packages installed
4. to create requirements.txt : pip freeze > requirements.txt
5. to install from requirements.txt : pip install -r requirements.txt
6. Deactivate : deactivate
---------------

creating Django server
0. pip install django
1. django-admin startproject double_server
2. cd double_server

3. python manage.py startapp api

4. In the file settings.py add the following:
INSTALLED_APPS = [
    ...
    'api',
]

5. modify api/views.py, api/urls.py and server/urls.py
	(main code in inside view.py, the urls.py files only store the api call required)
6. run using: python manage.py runserver

------------------

server deploy steps:

1. modify settings
2. add middlewares: gunicorn, whitenoise, dj-database-url
3. assign staticfile path in settings.py and then:
    python manage.py collectstatic
4. server run command while deployed:
    gunicorn theServer.wsgi:application
