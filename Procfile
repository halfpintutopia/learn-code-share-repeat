release: python backend/manage.py makemigrations && python backend/manage.py migrate
web: cd backend && gunicorn app.wsgi --log-file -
worker: cd frontend && yarn build && yarn preview