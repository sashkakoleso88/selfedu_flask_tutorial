from flask import Flask, render_template

app = Flask(__name__)

menu = ["Install", "Tutorial", "Contacts"]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='About us', menu=menu)


if __name__ == '__main__':
    app.run()
