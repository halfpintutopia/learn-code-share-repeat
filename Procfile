release: python backend/manage.py makemigrations && python backend/manage.py migrate
web: gunicorn backend.app.wsgi --log-file -
worker: yarn --cwd frontend build && yarn --cwd frontend preview