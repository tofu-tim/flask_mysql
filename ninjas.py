from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import Dojo, Ninja

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    new_ninja = Ninja(request.form)
    new_ninja.save()
    return redirect('/')

@app.route('/ninjas/edit/<ninja_id>')
def edit_page(ninja_id):
    print("Editing ninja id:", ninja_id)
    return render_template('edit_ninja.html', ninja=ninja)

@app.route('/ninjas/delete/<ninja_id>/<dojo_id>')
def delete_ninja(ninja_id, dojo_id):
    print("Deleting ninja id:", ninja_id)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/ninjas/update/<dojo_id>', methods=["POST"])
def update_ninja(dojo_id):
    print("Updating ninja information: ", request.form)
    return redirect(f'/dojos/{dojo_id}')