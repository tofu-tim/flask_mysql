from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos_main.html', dojos=dojos)

@app.route('/add/dojo', methods=['POST'])
def add_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_students(id):
    data = {
        "id": id
    }
    dojo = Dojo.dojo_ninjas(id)

    if dojo is not None:
        print(dojo.ninjas)
        return render_template('dojo.html', dojo=dojo)
    else:
        return "Dojo not found"
