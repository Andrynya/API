from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Запрос к API для получения случайной цитаты
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data['content']
        author = quote_data['author']
    else:
        quote = "Не удалось получить цитату."
        author = ""

    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)