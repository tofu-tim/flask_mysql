from flask import Flask, render_template, request, redirect

from users import User

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("read_all.html", users=User.get_all())

@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route("/users/create", methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
