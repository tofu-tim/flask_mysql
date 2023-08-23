from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return render_template("dojos_main.html")

@app.route('/ninjas')
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


# @app.route('/ninjas/edit/<ninja_id>')
# def edit_page(ninja_id):
#     print("Editing ninja id:", ninja_id)
#     return render_template('edit_ninja.html', ninja=ninja)

# @app.route('/ninjas/update/<dojo_id>', methods=["POST"])
# def update_ninja(dojo_id):
#     print("Updating ninja information: ", request.form)
#     return redirect(f'/dojos/{dojo_id}')