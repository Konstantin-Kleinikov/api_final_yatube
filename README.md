 API для Yatube

Этот проект реализует REST API для социальной сети Yatube. Он позволяет 
внешним приложениям создавать публикации, создавать комментарии к публикациям,
подписываться на других пользователей и получать информацию о сообществах.

## Описание
- Аутентификация пользователей с использованием JWT
- Операции CRUD для публикаций, комментариев, подписок и сообществ
- Функционал подписки на пользователей
- Пагинация и права доступа

## Установка
1. Клонируйте репозиторий:  
git clone https://github.com/Konstantin-Kleinikov/api_final_yatube


2. Перейдите в директорию проекта:  
cd api_final_yatube


3. Создайте и активируйте виртуальное окружение:  
python -m venv venv  
source venv/bin/activate # Для Windows: venv\Scripts\activate


4. Установите зависимости:  
python3 -m pip install --upgrade pip  
pip install -r requirements.txt  


5. Заполните базу данных начальными данными:  
Перейдите в папку _postman_collection_ и выполните команду `bash set_up_data.sh` 
в терминале Bash.


6. Примените миграции:  
python manage.py migrate  


7. Импортируйте предопределённые API-запросы в Postman:  
Откройте Postman и импортируйте коллекцию из файла 
_postman_collection_\ _API_for_yatube.postman_collection.json_.  


8. Используйте Django Debug Toolbar с Django Rest Framework (DRF) для
оптимизации SQL-запросов:  
Выполните запрос в Postman.  
В браузере перейдите на страницу http://127.0.0.1:8000/__debug__/ и на панели
Django Debug Toolbar выберите History, сделайте Refresh, для выбранной записи
нажмите на кнопку Switch и на панели перейдите в пункт SQL для анализа запроса.

## Использование
Запустите сервер разработки:  
python manage.py runserver  

Ознакомьтесь с документацией API по адресу http://127.0.0.1:8000/redoc/.

### Примеры API-запросов
1. Создание новой публикации 
POST-запрос для авторизованного пользователя по адресу http://127.0.0.1:8000/api/v1/posts/  
с телом запроса  
```json
{
    "text": "Post with group (Example)",
}
```
должен создать новую публикацию в базе данных и вернуть ответ со статусом **201 Created**. 


## Testing
Запустите тесты, используя:  
pytest


