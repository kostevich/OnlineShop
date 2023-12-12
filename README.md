# OnlineShop
**OnlineShop** – учебный проект на [Flask](https://github.com/pallets/flask), представляющий собой интернет-магазин спортивной одежды, осуществляющий добавление товаров в магазин и их оплату.

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать. 
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: [cloudipsp](https://github.com/cloudipsp/python-sdk), [dublib](https://github.com/DUB1401/dublib), [flask](https://github.com/pallets/flask?ysclid=lpxvt6k9hy682670415), [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/latest/). 
```
pip install cloudipsp 
pip install flask
pip install flask-sqlalchemy
pip install git+https://github.com/DUB1401/dublib
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
4. Настроить оплату путём редактирования [_Settings.json_](#Settings).
5. В среде исполнения запустить файл _app.py_ командой:
```
 flask run
```
6. Перейти по ссылке (пример: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)).

# Settings.json
<a name="Settings"></a> 

```JSON
"merchant_id":0,
"secret_key":""
```
Сюда необходимо занести данные мерчантов (можно получить на сайте [Fondy](https://portal.fondy.eu/).


# Отслеживание в базе данных.

Откройте файл Shop.db в программе для открытия баз данных (пример: [SQLiteStudio](https://sqlitestudio.pl/)).

# Пример работы
**Главная страница:**

![image](https://github.com/kostevich/OnlineShop/assets/109979502/74253b1c-0e35-46ca-b73c-cba50f7ece18)

**Форма добавления товара:**

![image](https://github.com/kostevich/OnlineShop/assets/109979502/48a1b02e-2981-4768-80c2-89ea2b2c00a6)

**Страница оплаты**

![image](https://github.com/kostevich/OnlineShop/assets/109979502/8229d9bc-6b6c-4a17-81c4-bbe4af62d08c)

# Известные проблемы
В некоторых странах для корректной работы оплаты необходимо воспользоваться vpn.

_Copyright © Kostevich Irina. 2023._
