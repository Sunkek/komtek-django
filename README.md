# Тестовое задание на разработчика Python

Суть задания описана в [task.md](task.md).

Задание ещё не выполнено до конца:

- Описание эндпоинтов и примеры использования.
- Более детальные сообщения об ошибках.


## Установка

...

После запуска контейнеров нужно мигрировать базу данных и создать суперюзера:

```
docker-compose exec api python manage.py makemigrations --noinput
docker-compose exec api python manage.py migrate --noinput
docker-compose exec api python manage.py createsuperuser
```

...


Побаловаться с API и админской панелью можно по адресу 
http://51.158.163.234:8000/api/v1/ 
(не обещаю, что буду держать его запущенным 24/7).
