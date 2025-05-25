    BOOKING

    ОПИСАНИЕ ПРОЕКТА:
Booking — это проект Django REST API для управления отелями, номерами, пользователями и бронированиями. Он позволяет пользователям регистрироваться, просматривать отели и номера, а также создавать бронирования для доступных номеров.

    ДЛЯ ЗАПУСКА ВАМ ПОТРЕБУЮТСЯ:
1. Python 3.12+
2. Менеджер пакетов pip
3. Virtualenv

    УСТАНОВКА И НАСТРОЙКА:
1) Клонировать репозиторий:
 git clone https://github.com/SIberianBears/booking.git
 cd booking

2)  Создать и активировать виртуальную среду:
  
    macOS/Linux:
 python3 -m venv venv
 source venv/bin/activate

    Windows:
 python -m venv venv
 venv\Scripts\activate

3) Установить зависимости:
 
 pip install -r requirements.txt

4) Применить миграции:
 
 python manage.py migrate

5) Запустить сервер:
 
 python manage.py runserver



 

