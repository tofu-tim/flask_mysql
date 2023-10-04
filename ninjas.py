from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template('dojos_main.html', dojos=dojos)

@app.route('/ninjas', methods=['GET', 'POST'])
def ninjas():
    ninjas = Ninja.get_all()
    return render_template('ninja.html', ninjas=ninjas,  get_dojo=Ninja.get_dojo)

# @app.route('/ninjas', methods=['GET', 'POST'])
# def ninjas():
#     ninjas = Ninja.get_all()
#     return render_template('ninja.html', ninjas=ninjas, get_dojo=Ninja.get_dojo)

@app.route('/new/ninja')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')

@app.route('/ninjas/delete/<ninja_id>/<dojo_id>', methods=['POST'])
def delete_ninja(ninja_id, dojo_id):
    Ninja.destroy(request.form)
    return redirect('/ninjas')


@app.route('/ninjas/edit/<int:id>', methods=['GET','POST'])
def edit_ninja(id):
    ninja = Ninja.get_one({"id": id})
    dojos = Dojo.get_all()
    return render_template('edit_ninja.html', ninja=ninja, dojos=dojos)


@app.route('/ninjas/update/<int:id>', methods=['GET','POST'])
def update_ninja(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.update(data)
    return redirect('/ninjas')
