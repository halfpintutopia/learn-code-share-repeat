release: python backend/manage.py makemigrations && python backend/manage.py migrate
web: gunicorn app.wsgi --log-file -