release: python backend/manage.py makemigrations && python manage.py migrate
web: gunicorn backend.app.wsgi --log-file -