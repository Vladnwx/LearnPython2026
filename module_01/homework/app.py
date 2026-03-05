import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'


@app.route('/cars')
def cars():
    pass


@app.route('/cats')
def cats():
    pass


@app.route('/get_time/now')
def get_time_now():
    pass


@app.route('/get_time/future')
def get_time_future():
    pass


@app.route('/get_random_word')
def get_random_word():
    pass


@app.route('/counter')
def counter():
    pass


if __name__ == '__main__':
    app.run(debug=True)
