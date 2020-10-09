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

## REST API

### Панель администратора

`/api/v1/admin/`

Позволяет создавать, редактировать и удалять справочники и их элементы при помощи 
несложного дефолтного UI Django. Переводом UI я не озадачился, но указал 
читабельные названия у полей моделей.

### Список всех справочников

GET `/api/v1/catalogs/`

Всё и так понятно - получаем все существующие справочники.

### Список справочников, актуальных на указанную дату

GET `/api/v1/catalogs/actual/<dd-mm-yyyy>/`

Получаем все справочники, которые были созданы до указанной даты и не успели истечь 
до неё же. Если не указывать дату, то API выдаст актуальные справочники на текущий 
день. 

При желании можно обработать и другие форматы даты, но пока работает только этот.

Этот эндпоинт демонстрирует возможность передачи динамически меняющихся параметров 
через URL.

### Элементы заданного справочника указанной/текущей версии

GET `api/v1/elements/from/?catalog_name=<name>&catalog_version=<version>`

Получаем все элементы указанного справочника. Если версия не указана, берётся 
справочник с самой свежей датой начала действия.

Этот эндпоинт демонстрирует возможность передачи динамически меняющихся параметров 
через строку запроса (query string).

### Валидация элемента заданного справочника по указанной/текущей версии

GET `/api/v1/element/validation/`

Проверяем, валидный элемент или нет. Для проверки требуется в API передать JSON 
следующего вида:

```
{
    "catalog": {
        "short_name": <name>,
        "version": <version>
    },
    "element": {
        "code": <code>,
        "description": <description>
    }
}
```

Если не передавать версию справочника, API будет проверять по самой свежей его версии.

Этот эндпоинт демонстрирует возможность передачи динамически меняющихся данных 
через тело запроса. Такое не получится проверить в браузере, можно использовать 
REST-клиент типа Postman.


### Я не хочу деплоить это на своей машине

Побаловаться с API и админской панелью можно по адресу 
http://51.158.163.234:8000/api/v1/ 
(не обещаю, что буду держать его запущенным 24/7).

Логин и пароль для админа - `komtek-admin`.
