lint:
	flake8 --ignore=E402,E501,E712,W503,E203
	black --check .

format:
	black .
	isort .

shell:
	python manage.py shell

requirements:
	pip list --format=freeze > requirements.txt