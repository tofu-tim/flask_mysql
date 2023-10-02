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
    return render_template('ninja.html', ninjas=ninjas)

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


@app.route('/ninjas/edit/<int:id>', methods=['GET', 'POST'])
def edit_ninja_form(id):
    ninja = Ninja.get_one(id)
    dojos = Dojo.get_all()
    return render_template('edit_ninja.html', ninja=ninja, dojos=dojos)


@app.route('/ninjas/update/', methods=["GET", "POST"])
def update_ninja():
    if request.method == "POST":
        print("Received form data: ", request.form)
        result = Ninja.update(request.form)
        if result:
            print("Ninja updated successfully")
        else:
            print("Ninja update failed")
        return redirect('/ninjas')

