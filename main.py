from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from validate_email import validate_email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# users_pars = Users
users = {}


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    username = StringField('Имя', validators=[DataRequired()])
    submit = SubmitField('Войти')


class InForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class User:
    last_user = 0
    signed = 0
    name = 0


user = User


@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/Главная')
@app.route('/главная')
@app.route('/main page')
def index():
    return render_template('index.html', image=url_for(
        "static", filename="css/img/my_images/str211.jpg"),
                           style=url_for(
                               "static", filename="css/spring.css"),
                           name=user.name, signed=user.signed)


@app.route("/str3.html")
def str3():
    return render_template('str3.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/images/str241.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str312.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "css/img/images/str242.jpg"),
                           image4=url_for("static",
                                          filename=
                                          "css/img/images/str243.jpg"),
                           image5=url_for("static",
                                          filename=
                                          "css/img/images/str244.jpg"),
                           image6=url_for("static",
                                          filename=
                                          "css/img/images/str245.jpg"),
                           image7=url_for("static",
                                          filename=
                                          "css/img/images/str246.jpg"),
                           image8=url_for("static",
                                          filename=
                                          "css/img/images/str247.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str4.html")
def str4():
    return render_template('str4.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           name=user.name, signed=user.signed)


@app.route("/str21.html")
def str21():
    return render_template('str21.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str212.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str22.html")
def str22():
    return render_template('str22.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str221.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str222.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str23.html")
def str23():
    return render_template('str23.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str231.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str31.html")
def str31():
    return render_template('str31.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           name=user.name, signed=user.signed)


@app.route("/str32.html")
def str32():
    return render_template('str32.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str231.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str40.html")
def str40():
    return render_template('str40.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str401.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str402.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "css/img/my_images/str403.jpg"),
                           image4=url_for("static",
                                          filename=
                                          "css/img/my_images/str404.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str41.html")
def str41():
    return render_template('str41.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str410.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str411.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "css/img/my_images/str412.jpg"),
                           image4=url_for("static",
                                          filename=
                                          "css/img/my_images/str413.jpg"),
                           image5=url_for("static",
                                          filename=
                                          "css/img/my_images/str414.jpg"),
                           image6=url_for("static",
                                          filename=
                                          "css/img/my_images/str415.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str42.html")
def str42():
    return render_template('str42.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str421.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str43.html")
def str43():
    return render_template('str43.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str431.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str44.html")
def str44():
    return render_template('str44.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str440.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str441.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "css/img/my_images/str442.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str45.html")
def str45():
    return render_template('str45.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str450.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str451.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "css/img/my_images/str452.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str46.html")
def str46():
    return render_template('str46.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str461.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str47.html")
def str47():
    return render_template('str47.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str470.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str471.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "css/img/my_images/str472.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str48.html")
def str48():
    return render_template('str48.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           name=user.name, signed=user.signed)


@app.route("/str49.html")
def str49():
    return render_template('str49.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str490.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str491.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/str491.html")
def str491():
    return render_template('str491.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           image1=url_for("static",
                                          filename=
                                          "css/img/my_images/str4911.jpg"),
                           image2=url_for("static",
                                          filename=
                                          "css/img/my_images/str4911.jpg"),
                           image3=url_for("static",
                                          filename=
                                          "css/img/my_images/str4914.jpg"),
                           name=user.name, signed=user.signed)


@app.route("/out.html")
def out():
    user.signed = 0
    user.name = 0
    user.last_user = 0
    return render_template('out.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           name=user.name, signed=user.signed)


@app.route("/personal.html")
def personal():
    return render_template('personal.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           name=user.name, signed=user.signed)


@app.route("/str5.html")
def str5():
    return render_template('str5.html',
                           style=url_for("static",
                                         filename="css/spring.css"),
                           name=user.name, signed=user.signed)


def reg_funk(email, name, password):
    last_user = email
    error = 0
    if not validate_email(last_user):
        error = 1
        print(last_user)
    elif last_user in users.keys():
        error = 2
    else:
        user.last_user = last_user
        user.signed = 1
        user.name = name
        users[last_user] = (name, password)
        print(users)
    return error


def in_funk(email, password):
    print("in funk")
    print("email                  ", email)
    print("password               ", password)
    print("users[last_user][0]    ", users[email][0])
    print("users[last_user][1]    ", users[email][1])
    last_user = email
    error = 0
    if last_user not in users.keys():
        error = 1
        print("2")
    elif password != users[last_user][0]:
        error = 3
        print("3")
    else:
        print("OK")
        user.last_user = last_user
        user.signed = 1
        user.name = users[last_user][0]
        print(users)
    return error


@app.route("/registration.html", methods=['GET', 'POST'])
def registration():
    form = LoginForm()
    if form.validate_on_submit():
        error = reg_funk(str(form.email.data), str(form.username.data), str(form.password.data))
        return render_template('success.html',
                               style=url_for("static",
                                             filename="css/spring.css"),
                               par=error, name=user.name,
                               signed=user.signed)

    return render_template('registration.html', form=form,
                           style=url_for("static",
                                         filename="css/spring.css"),
                           name=user.name, signed=user.signed)


@app.route("/input.html", methods=['GET', 'POST'])
def input1():
    form = InForm()
    if form.validate_on_submit():
        error = in_funk(str(form.email.data), str(form.password.data))
        return render_template('success.html',
                               style=url_for("static",
                                             filename="css/spring.css"),
                               par=error, name=user.name,
                               signed=user.signed)

    return render_template('input.html', form=form,
                           style=url_for("static",
                                         filename="css/spring.css"),
                           name=user.name, signed=user.signed)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8080, host='127.0.0.1')
