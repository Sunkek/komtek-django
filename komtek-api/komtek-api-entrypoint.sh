#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.create_superuser\
('komtek-admin', 'admin@komtek.com', 'komtek-admin')" | python manage.py shell