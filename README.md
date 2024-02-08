# Проект Recipegram

### Описание проекта
Foodgram - сервис для публикации рецептов, на котором можно посмотреть на что-нибудь вкусное, потом приготовить и съесть. Можно подписываться на любых авторов, добавлять рецепты в избранное и корзину для покупки необходимых ингредиентов.
### Запуск с помощью CI/CD
В Settings Secrets создаем переменные с данными:
```
DOCKER_PASSWORD
DOCKER_USERNAME
HOST
SSH_KEY
SSH_PASSPHRASE
TELEGRAM_TO
TELEGRAM_TOKEN
USER
```

Действия выполняются на локальной машине и на сервере Яндекс Облака.
Предварительно нужно установить необходимые компоненты для функционирования проекта:
```
ssh -i username@ip
#Выполнить вход в Яндекс облако.

sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo systemctl start docker.service && sudo systemctl enable docker.service
#Установить компоненты.
```
Создаём директорию проекта foodgram и папку внутри него infra, в главной директории создаём файл .env c данными:
```
POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_NAME=foodgram
DB_HOST=db
DB_PORT=5432
DEBUG=False
SECRET_KEY=#секретный ключ из settings.py
ALLOWED_HOSTS=127.0.0.1,localhost
```
Копируем файлы docker-compose.production.yml и nginx.conf в папку infra

Выполняем команду docker compose -f docker-compose.production.yml up -d

Проект запустился и доступен по указанному адресу, но необходимо наполнить его данными для этого выполняем следующие команды:
```
docker compose -f docker-compose.production.yml exec backend manage.py makemigrations #миграции
docker compose -f docker-compose.production.yml exec backend manage.py migrate #миграции
docker compose -f docker-compose.production.yml exec backend manage.py createsuperuser #создание суперпользователя
docker compose -f docker-compose.production.yml exec backend manage.py collectstatic #статика
docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/ #статика
docker compose -f docker-compose.production.yml exec backend manage.py load_tags #загрузка тегов
docker compose -f docker-compose.production.yml exec backend manage.py load_ingredients #загрузка ингредиентов
```
Проект работает и наполнен данными!

Для остановки работы проекта:
```
docker compose -f docker-compose.production.yml stop
docker compose -f docker-compose.production.yml down -v
```
### Запуск проекта локально
Клонируем репозитории на локальную машину, заходим в папку infra и запускаем:
```
docker compose up --build
```
Наполняем данными:
```
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
docker compose exec backend python manage.py load_tags
docker compose exec backend python manage.py load_ingredients
```
Проект работает локально!

Автор: Ермеев Павел https://github.com/bytplokhim
