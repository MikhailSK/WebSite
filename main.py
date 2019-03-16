from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/Главная')
@app.route('/главная')
def index():
    return render_template('index.html', image=url_for("static", filename="img/my_images/str211.jpg"),
                           style=url_for("static", filename="spring.css"))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8080, host='127.0.0.1')
