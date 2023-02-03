# ИТОГОВЫЙ ПРОЕКТ 6.9 (HW-03)
### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Так же в .env надо прописать следующие переменные

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
