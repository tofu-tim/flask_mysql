from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import Dojo, Ninja

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos_main.html', dojos=dojos)

@app.route('/add/dojo', methods=['POST'])
def add_dojo():
    add_dojo = Dojo(request.form)
    add_dojo.save()
    return redirect('/')