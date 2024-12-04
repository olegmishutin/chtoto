# Запуск проекта
 - docker-compose up --build
 - зайти на http://localhost:8000/

### Для создания администратора
- docker-compose exec -it backend bash
- python manage.py createsuperuser
- заполняем данные