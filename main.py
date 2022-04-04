from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def collect_data():
    return render_template("LogIn.html")


@app.route("/Register")
def Search():
    return render_template("register.html")





if __name__ == "__main__":
    app.run()