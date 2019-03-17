from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/Главная')
@app.route('/главная')
@app.route('/main page')
def index():
    return render_template('index.html', image=url_for("static", filename="img/my_images/str211.jpg"),
                           style=url_for("static", filename="spring.css"))


@app.route("/str3.html")
def str3():
    return render_template('str3.html', style=url_for("static", filename="spring.css"),
                           image1=url_for("static", filename="img/images/str241.jpg"),
                           image2=url_for("static", filename="img/my_images/str312.jpg"),
                           image3=url_for("static", filename="img/images/str242.jpg"),
                           image4=url_for("static", filename="img/images/str243.jpg"),
                           image5=url_for("static", filename="img/images/str244.jpg"),
                           image6=url_for("static", filename="img/images/str245.jpg"),
                           image7=url_for("static", filename="img/images/str246.jpg"),
                           image8=url_for("static", filename="img/images/str247.jpg"))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8080, host='127.0.0.1')
