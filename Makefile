up-build:
	docker compose up --build

up:
	docker compose up

down:
	docker compose down

migrate:
	docker compose run backend python manage.py migrate

makemigrations:
	docker compose run backend python manage.py makemigrations

test:
	docker compose run backend python manage.py test

startapp:
	@read -p "Enter app name: " app_name; \
	docker compose run backend python manage.py startapp $$app_name

createsuperuser:
	docker compose run backend python manage.py createsuperuser

shell:
	docker compose run backend python manage.py shell

logs:
	docker compose logs -f