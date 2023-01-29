from flask import Flask, render_template, url_for

app = Flask(__name__)

# app1 = Flask("app1")  # Flask обеспечивает поддержку сразу нескольких  WSGI приложений.
# app2 = Flask("app2")  # Каждое приложение отвечает за свой функционал сайта, и может иметь разные настройки

menu = ["Install", "Tutorial", "Contacts"]


@app.route('/')
def index():
    print(url_for('index'))  # работает только в контексте запроса
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))  # работает только в контексте запроса
    return render_template('about.html', title='About us', menu=menu)


# with app.test_request_context():  # искусственно созданный тестовый контекст запроса без активации веб сервера
#     print(url_for('about'))


@app.route('/profile/<username>')  # динамическая переменная в URL
def profile(username):
    return f'User : {username}'


@app.route('/profile/<path:variables>')  # Всё, что пишется после конвертера path: будет считаться единым url адресом
def profile_with_path(variables):
    return f'User : {variables}'         # '/profile/abcd/1234' ------> User : abcd/1234


@app.route('/profile_int/<int:variable>')    # Переменной может быть только целое число
def profile_int_only(variable):
    return f'User : {variable}'


@app.route('/profile_float/<float:variable>')    # В переменную можно записать только число с плавающей точкой
def profile_with_float(variable):
    return f'User : {variable}'


@app.route('/profile_int_path/<int:variable>/<path:text_path>')    # Комбинирование конвертеров int и path
def profile_int_and_path(variable, text_path):
    return f'User : {variable} - {text_path}'    # profile_int_path/1234/test/something --> User : 1234 - test/something


# with app.test_request_context():    # Тестовый менеджер запроса с передачей динамичекого аргумента
#     print(url_for('profile', username='Alex'))


if __name__ == '__main__':
    app.run()
