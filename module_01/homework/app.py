import datetime
import random
from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'


CARS_STRING = "Chevrolet, Renault, Ford, Lada"
CARS_LIST = CARS_STRING.split(", ")

@app.route('/cars')
def cars():
    return CARS_LIST

CATS_STRING = "корниш-рекс, русская голубая, шотландская вислоухая, мейн-кун, манчкин"
CATS_LIST = CATS_STRING.split(", ")

@app.route('/cats')
def cats():
    return random.choice(CATS_LIST)


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


@app.route('/')
def index():
    # Список всех эндпоинтов
    links = []
    for rule in app.url_map.iter_rules():
        if "static" not in rule.endpoint:
            url = rule.rule
            links.append(f'<li><a href="{url}">{url}</a></li>')
    
    return f"""
    <h1>Навигация по модулю 01</h1>
    <ul>
        {"".join(links)}
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
