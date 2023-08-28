# Из flask импортируем класс Flask для работы сайта.
from flask import Flask
# Из flask импортируем render_template для передачи шаблонов html.
from flask import render_template
# Из flask импортируем request для обработки данных со страниц.
from flask import request
# Импортируем модуль redirect для перенаправления на другую страницу.
from flask import redirect
# Из flask_sqlalchemy импортируем класс SQLAlchemy для работы с бд.
from flask_sqlalchemy import SQLAlchemy
# Из cloudipsp импортируем Api, Checkout для работы кнопки оплаты.
from cloudipsp import Api, Checkout


# Создадим объект класса Flask с именем файла.
app = Flask(__name__)
# Создадим базу данных, обращаясь к объекту app и устанавливая ему настройки.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# База данных принадлежит приложению app.
db = SQLAlchemy(app)

# Создаем класс Item, который наследуется от модели для создания таблицы бд.
class Item(db.Model):
    # Создаем поле id, число, создается автоматически.
     id= db.Column(db.Integer, primary_key = True)
    # Создаем поле title, строка.
     title = db.Column(db.String(100), nullable = False)
    # Создаем поле price, число.
     price = db.Column(db.Integer, nullable = False)
    # Создаем поле active, логический тип.
     active = db.Column(db.Boolean, default = True)
     # Создаем поле description, строка.
     description = db.Column(db.Text, nullable = False)
     
     # Получение данных объекта базы данных в виде строки.
     def __repr__(self):
        # Возвращаем поле title класса Item в текстовом виде.
        return self.title
     
# Начало работы функции mainpage при переходе по ссылке.
@app.route('/mainpage')
# Функция, выводящая на страницу данные шаблона html.
def mainpage():
    # Сохраняем объект, в котором находится данные выбранной статьи.
    items = Item.query.order_by(Item.price).all()
    # Возвращение шаблон html на страницу.
    return render_template('mainpage.html', items = items) 

# Начало работы функции buy_product при переходе по ссылке.
@app.route('/buy_product/<int:id>')
# Функция, выводящая на страницу страницу оплаты.
def buy_product(id):
    # Сохраняем объект, в котором находится данные выбранного товара.
    item = Item.query.get(id)
    # Передаем объекту класса Api данные продавца и секретный ключ.
    api = Api(merchant_id=1531733,
          secret_key='j42hKroTARZebzlXvaQAByiBPKCYT0lq')
    # Создаем объект класса Checkout и передаем туда данные продавца.
    checkout = Checkout(api=api)
    # Cохраняем словарь с ценой выбранного товара и валютой.
    data = {
    "currency": "BYN",
    "amount": str(item.price)+"00"}
    # Формируем ссылку с оплатой товара.
    url = checkout.url(data).get('checkout_url')
    # Переадресация на страницу оплаты.
    return redirect(url)

# Начало работы функции create_product при переходе по ссылке.
@app.route('/createproduct', methods = ['POST', 'GET'])
# Функция, выводящая на страницу данные шаблона html.
def create_product():
    # Если пришел запрос с методом POST. 
    if request.method == 'POST':
        # Сохраняем в переменную title значение из поля формы title.
        title = request.form['title']
        # Сохраняем в переменную value значение из поля формы value.
        price = request.form['price']
        # Сохраняем в переменную description значение из поля формы value.
        description = request.form['description']
        # Сохраняем объект класса Item с данными из переменных, записанных в нужные поля.
        item = Item(title=title, price=price, description=description)
        # Попробуем добавить значения в базу данных.
        try:
            # Добавление объекта класса Item в сессию.
            db.session.add(item)
            # Сохранение в базе данных.
            db.session.commit()
            # Переадресация на страницу со всеми статьями.
            return redirect('/mainpage')
        # Исключение.
        except:
            # Возвращаем ошибку: "Не удалось добавить статью".
            return "Не удалось добавить статью."
    # Если пришел GET-запрос.
    else:
        # Возвращение шаблон html на страницу.
        return render_template('create_product.html') 

# Создание контекста приложения.
with app.app_context():
    # Создание бд.
    db.create_all()
# Если имя такое же как название этого файла.
if __name__=='__main__':
    # То запускаем приложение flask, в режиме исправления ошибок.
    app.run(debug=True)