# Тестовое задание на разработчика Python

Суть задания описана в [task.md](task.md).

В режиме дебага приложение легко запускается и тестируется при помощи обычной `python manage.py runserver`, но для размещения на моём VPS пришлось попотеть и завернуть всё в nginx.

## Установка

Для начала нужно иметь установленные Docker и Docker-compose. 

### 1 

Перемещаемся в желаемую директорию и клонируем этот репозиторий: 

`git clone https://github.com/Sunkek/komtek-django`

### 2

Входим в репозиторий при помощи `cd komtek-django` и создаём файл с переменными окружения для нашего API: 

`touch komtek-api.env

vim komtek-api.env`

Содержание файла должно иметь следующий вид:
```
DEBUG=1
SECRET_KEY=qwertyasdfghzxcvbn
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```
`DEBUG=1` - включен тестовый режим, не использовать в продакшне! `SECRET_KEY` тоже нужно будет посерьёзнее. В `ALLOWED_HOSTS` можно добавить публичный IP и домен хоста.

### 3

Строим и запускаем контейнер:

`docker-compose up --build`

### 4 

После запуска контейнера нужно мигрировать базу данных и создать суперюзера для входа в админскую панель. Открываем терминал в этой же директории (или используем tmux):

`docker-compose exec api python manage.py makemigrations`

`docker-compose exec api python manage.py migrate`

`docker-compose exec api python manage.py makemigrations api`

`docker-compose exec api python manage.py migrate api`

`docker-compose exec api python manage.py createsuperuser`

Готово!

### Я не хочу деплоить это на своей машине

Побаловаться с API и админской панелью можно по адресу 
http://www.komtek.suncake.ga/api/v1/
(не обещаю, что буду держать его запущенным 24/7).

Логин и пароль для админа - `komtek-admin`.

## REST API

### Панель администратора

[`/admin/`](http://www.komtek.suncake.ga/api/v1/admin/)

Позволяет создавать, редактировать и удалять справочники и их элементы при помощи 
несложного дефолтного UI Django. Переводом UI я не озадачился, но указал 
читабельные названия у полей моделей.

### Список всех справочников

GET [`/catalogs/`](http://www.komtek.suncake.ga/api/v1/catalogs/)

Всё и так понятно - получаем все существующие справочники.

### Список справочников, актуальных на указанную дату

GET [`/catalogs/actual/<dd-mm-yyyy>/`](http://www.komtek.suncake.ga/api/v1/catalogs/actual/01-10-2020/)

Получаем все справочники, которые были созданы до указанной даты и не успели истечь 
до неё же. Если не указывать дату, то API выдаст актуальные справочники на текущий 
день. 

При желании можно обработать и другие форматы даты, но пока работает только этот.

Этот эндпоинт демонстрирует возможность передачи динамически меняющихся параметров 
через URL.

### Элементы заданного справочника указанной/текущей версии

GET [`/elements/from/?catalog_name=<name>&catalog_version=<version>`](http://www.komtek.suncake.ga/api/v1/elements/from/?catalog_name=%D0%A2%D0%B5%D1%81%D1%82&catalog_version=0.1)

Получаем все элементы указанного справочника. Если версия не указана, берётся 
справочник с самой свежей датой начала действия.

Этот эндпоинт демонстрирует возможность передачи динамически меняющихся параметров 
через строку запроса (query string).

### Валидация элемента заданного справочника по указанной/текущей версии

POST [`/element/validation/`](http://www.komtek.suncake.ga/api/v1/element/validation)

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
Если не передавать описание элемента, то API просто вернёт элемент по его коду (если тот существует).

Этот эндпоинт демонстрирует возможность передачи динамически меняющихся данных 
через тело запроса.

## P.S.

Моё почтение авторам [этого гайда](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/).
