# pull official base image
FROM python:3-alpine

# set work directory
WORKDIR /usr/src/app/komtek

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# migrate the database
RUN python manage.py migrate --noinput
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput
# create superuser for testing
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('komtek-admin', 'admin@komtek.com', 'komtek-admin')" | python manage.py shell

# copy project
COPY . .