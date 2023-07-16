# Postal system
this project is code changllenge for create custom User model and customize permision_class and serializer_class in ModelViewSet by drf
i use jwt for autentication.

## requirments of project
- cell_phone instead of username
- post user open without autentication
- get users just for admin user
- customizable pagination

## usage in ubuntu terminal
if you want to use this project:
  - install python3 pip:  sudo apt install python3-pip
  - install virtualenv: pip install virtualenv
  - create virtualenv in "src" directory: python3 -m virtualenv --python=python3.8 venv
  - activate venv: source venv/bin/activate
  - install requirements.txt: pip install -r requirements.txt
  - apply migrations: python manage.py migrate
  - create super user: python manage.py createsuperuser
  - run project: python manage.py runserver

alternative way for run project:
  - docker compose -f docker-compose.yml up -d --build

apis info: {{base_route}}:8000/swagger/schema/
