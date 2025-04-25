this is the test phrase (returns risk level) and this is the accepted format for call:
 {
   "no_data": "[[99, 16, 36.654748, 95.011801, 118, 72, 41, 0, 96.006188, 1.833629], [83, 12, 36.044191, 98.584497, 111, 84, 50, 0, 79.295332, 1.672735], [79, 12, 36.884979, 95.987129, 130, 70, 22, 1, 79.869933, 1.922334], [66, 15, 36.957178, 97.916267, 131, 77, 61, 1, 53.923400, 1.896381], [72, 16, 36.8, 98, 120, 80, 20, 1, 78, 1.78]]"
 }

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
