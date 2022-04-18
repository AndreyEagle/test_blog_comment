## Тестовое задание "Система комментариев блога"
### Как запустить проект:
1. Клонировать репозиторий :
```
git clone
```
2. Перед запуском проекта создать файл переменных окружения .env:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<ваш username>
POSTGRES_PASSWORD=<ваш password>
DB_HOST=db
DB_PORT=5432

DJANGO_DEBUG=''
SECRET_KEY=<ваш secret key>
```
3. Сборка и запуск проекта:
```
docker-compose up -d --build
```
4. Выполнить миграции:
```
docker-compose exec web python manage.py makemigrations
```
```
docker-compose exec web python manage.py migrate
```
5. Создать статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
6. Создать администратора:
```
docker-compose exec backend python manage.py createsuperuser
```

### Документация API:
```
http://localhost/swagger/
```
```
http://localhost/redoc/
```