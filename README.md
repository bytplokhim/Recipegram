# Проект Foodgram

### Описание проекта
Foodgram - сервис для публикации рецептов, на котором можно посмотреть на что-нибудь вкусное, потом приготовить и съесть. Можно подписываться на любых авторов, добавлять рецепты в избранное и корзину для покупки необходимых ингредиентов.

### Запуск проекта локально
Клонировать репозиторий с github
```
git clone git@github.com:bytplokhim/foodgram-project-react.git
```
Установить и активировать виртуальное окружение
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из requirements.txt
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции
```
python3 manage.py migrate
```
Запустить проект
```
python3 manage.py runserver
```
Автор: Ермеев Павел https://github.com/bytplokhim