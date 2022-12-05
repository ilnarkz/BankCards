install:
	pip install -r requirements.txt
lint:
	flake8 bank_cards
start:
	python manage.py runserver 0.0.0.0:8000
migrate:
	poetry run python manage.py migrate
