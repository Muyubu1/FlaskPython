from flask import Flask, render_template
from forms.forms import NamerForm #formu entegre ettik


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key'
@app.route("/")
def home():
    stuff="<h1>Hello, World!</h1>"
    return render_template("index.html", stuff=stuff)

@app.route("/index") 
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template(f"user.html", username=name)

@app.route("/pizza")
def pizza():
    toppings=["cheese", "pepperoni", "mushrooms"]
    return render_template(f"pizza.html", toppings=toppings)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

@app.route("/name", methods=["GET", "POST"])
def name():
    form = NamerForm()
    name = None

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''  # Formu temizle

    return render_template("index.html", form=form, name=name)


if __name__ == "__main__":
    app.run(debug=True)
