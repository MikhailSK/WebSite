from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/Главная')
@app.route('/главная')
@app.route('/main page')
def index():
    return render_template('index.html', image=url_for(
        "static", filename="img/my_images/str211.jpg"),
                           style=url_for(
                               "static", filename="spring.css"))


@app.route("/str3.html")
def str3():
    return render_template('str3.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/images/str241.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str312.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "img/images/str242.jpg"),
                           image4=url_for("static",
                                          filename=
                                          "img/images/str243.jpg"),
                           image5=url_for("static",
                                          filename=
                                          "img/images/str244.jpg"),
                           image6=url_for("static",
                                          filename=
                                          "img/images/str245.jpg"),
                           image7=url_for("static",
                                          filename=
                                          "img/images/str246.jpg"),
                           image8=url_for("static",
                                          filename=
                                          "img/images/str247.jpg"))


@app.route("/str4.html")
def str4():
    return render_template('str4.html',
                           style=url_for("static",
                                         filename="spring.css"))


@app.route("/str21.html")
def str21():
    return render_template('str21.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str212.jpg"))


@app.route("/str22.html")
def str22():
    return render_template('str22.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str221.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str222.jpg"))


@app.route("/str23.html")
def str23():
    return render_template('str23.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str231.jpg"))


@app.route("/str31.html")
def str31():
    return render_template('str31.html',
                           style=url_for("static",
                                         filename="spring.css"))


@app.route("/str32.html")
def str32():
    return render_template('str32.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str231.jpg"))


@app.route("/str40.html")
def str40():
    return render_template('str40.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str401.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str402.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "img/my_images/str403.jpg"),
                           image4=url_for("static",
                                          filename=
                                          "img/my_images/str404.jpg"))


@app.route("/str41.html")
def str41():
    return render_template('str41.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str410.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str411.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "img/my_images/str412.jpg"),
                           image4=url_for("static",
                                          filename=
                                          "img/my_images/str413.jpg"),
                           image5=url_for("static",
                                          filename=
                                          "img/my_images/str414.jpg"),
                           image6=url_for("static",
                                          filename=
                                          "img/my_images/str415.jpg"))


@app.route("/str42.html")
def str42():
    return render_template('str42.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str421.jpg"))


@app.route("/str43.html")
def str43():
    return render_template('str43.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str431.jpg"))


@app.route("/str44.html")
def str44():
    return render_template('str44.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str440.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str441.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "img/my_images/str442.jpg"))


@app.route("/str45.html")
def str45():
    return render_template('str45.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str450.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str451.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "img/my_images/str452.jpg"))


@app.route("/str46.html")
def str46():
    return render_template('str46.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str461.jpg"))


@app.route("/str47.html")
def str47():
    return render_template('str47.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str470.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str471.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "img/my_images/str472.jpg"))


@app.route("/str48.html")
def str48():
    return render_template('str48.html',
                           style=url_for("static",
                                         filename="spring.css"))


@app.route("/str49.html")
def str49():
    return render_template('str49.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str490.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str491.jpg"))


@app.route("/str491.html")
def str491():
    return render_template('str491.html',
                           style=url_for("static",
                                         filename="spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "img/my_images/str4911.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "img/my_images/str4911.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "img/my_images/str4914.jpg"))


@app.route("/input.html")
def input1():
    return render_template('input.html',
                           style=url_for("static",
                                         filename="spring.css"))


@app.route("/registration.html")
def registration():
    return render_template('registration.html',
                           style=url_for("static",
                                         filename="spring.css"), )


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8080, host='127.0.0.1')
