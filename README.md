# dynamic-application-system
Django application combined with devops tools

## Start up commands
```bash
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd dynamic_application_system
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

```bash
python manage.py runserver
gunicorn dynamic_application_system.wsgi:application
gunicorn --bind 0.0.0.0:8000 dynamic_application_system.wsgi:application
```