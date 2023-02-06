# ИТОГОВЫЙ ПРОЕКТ 6.9 (HW-03)
### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Переименуйте файл .env.sample в .env и скопируйте в него следующее:

```bash
DEBUG=True
SECRET_KEY='generated secret key'

EMAIL_HOST='host'
EMAIL_HOST_USER='user'
EMAIL_HOST_PASSWORD='password'
EMAIL_PORT=25

REDIS_HOST='localhost'
REDIS_PORT=6379
```

### Запуск проекта

```bash
./manage.py runserver
```

### Для проверки работоспособности проекта есть два тестовых аккаунта:
```bash
chat_user1@gmail.com / 123qweasdzxc123
chat_user2@gmail.com / 123qweasdzxc123
```

### Описание функционала:
```bash
http://127.0.0.1:8000/ - Поиск или создание новой комнаты для общения 
http://127.0.0.1:8000/swagger-ui/ - Доступный API 
http://127.0.0.1:8000/users/ - Доступные пользователи
http://127.0.0.1:8000/rooms/ - Доступные комнаты
http://127.0.0.1:8000/user/profile/ - Профиль юзера
```
### Внимание
```bash
Так же обращаю внимание, что функционал websocket'ов 
реализован с помощью django-channels. Для корректной работы 
проекта нужно иметь поl рукой Redis server. 
```