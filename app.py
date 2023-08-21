# Из flask импортируем класс Flask для работы сайта.
from flask import Flask
# Из flask импортируем render_template для передачи шаблонов html.
from flask import render_template
# Из flask_sqlalchemy импортируем класс SQLAlchemy для работы с бд.
from flask_sqlalchemy import SQLAlchemy


# Создадим объект класса Flask с именем файла.
app = Flask(__name__)
# Создадим базу данных, обращаясь к объекту app и устанавливая ему настройки.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://shop.db'

db=SQLAlchemy(app)

# Создаем класс Item, который наследуется от модели для создания таблицы бд.
class Item(db.Model):
    # Создаем поле id, число, создается автоматически.
     id= db.Column(db.Integer, primary_key = True)
    # Создаем поле title, строка.
     title = db.Column(db.String)
    # Создаем поле price, число.
     price = db.Column(db.Integer)
    # Создаем поле active, строка.
     active = db.Column(db.String)
     
     
# Начало работы функции mainpage при переходе по ссылке.
@app.route('/mainpage')
# Функция, выводящая на страницу данные шаблона html.
def mainpage():
    # Возвращение шаблон html на страницу.
     return render_template('mainpage.html') 


# Начало работы функции about при переходе по ссылке.
@app.route('/about')
# Функция, выводящая на страницу данные шаблона html.
def about():
    # Возвращение шаблон html на страницу.
     return render_template('about.html') 

# Если имя такое же как название этого файла.
if __name__=='__main__':
    # То запускаем приложение flask, в режиме исправления ошибок.
    app.run(debug=True)