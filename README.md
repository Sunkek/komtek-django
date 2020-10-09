# Тестовое задание на разработчика Python

Суть задания описана в [task.md](task.md).

Задание ещё не выполнено до конца.


## Установка

...

После запуска контейнеров нужно мигрировать базу данных и создать суперюзера:

```
docker-compose exec api python manage.py makemigrations --noinput
docker-compose exec api python manage.py migrate --noinput
docker-compose exec api python manage.py createsuperuser
```