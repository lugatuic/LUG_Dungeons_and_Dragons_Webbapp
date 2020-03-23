"""Routing functions for Flask"""

from flask import Flask, flash, redirect, render_template, request, url_for
#from flask_mysqldb import MySQL
from dnd_app import app, mysql
from dnd_app.account_forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    """Homepage"""
    #return render_template('index.html', title='Home')
    return redirect(url_for('account_create'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login form"""
    form = LoginForm()  # username +password
    if request.method == 'POST':  # TODO
        print("yes")
    return render_template('login.html', title='Sign In', form=form)


@app.route('/createAccount', methods=['POST', 'GET'])
def account_create():  # needs Username password, email
    """Account creation form"""
    # mysql cursor
    cursor = mysql.connection.cursor()
    # TODO: escape strings(prevent mysql injection) 
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash password and insert into database
        password = generate_password_hash(form.password.data)
        cursor.execute('''INSERT INTO account(accountName, password, email)
        VALUES (%s,%s,%s)''', (form.username.data, password, form.email.data))
        mysql.connection.commit()
        cursor.close()
        flash("Done. WELCOME!!!!!")
        return redirect(url_for('login'))
    return render_template(
        'accountCreation.html', title='Create Account', form=form)


@app.route('/<user>/createCharacter', methods=['POST', 'GET'])
def character_create(user):
    """Character creation form"""
    # TODO
    return render_template('characterCreation.html', title='Create Character')


@app.route('/<user>/createItem', methods=['POST', 'GET'])
def item_create(user):  # Name, cost, wieght, Availabity +flavor text/ability/uses
    """Item creation form"""
    # TODO
    return render_template('itemCreation.html', title='Create item')


@app.route('/<user>/createWeapon', methods=['POST', 'GET'])
def weapon_create(user):  # Name, Class, Range, Damage, Penetration, Special, Weight, Cost, Availabity, Flavor
    """Weapon creation form"""
    # TODO
    return render_template('weaponCreation.html', title='Create Weapon')


@app.route('/<user>/createGame', methods=['POST', 'GET'])
def game_create(user):
    """Game creation form"""
    if request.method == 'POST':
        gameFile = {
            "game_name": "",
            "Dungeon_Master": "",
            "gameID": 4,
            "Users": [],
            "msgLog": []
        }
    # TODO
    return render_template('gameCreation.html', title='Create game')


@app.route('/<user>/modifyGame', methods=['POST', 'GET'])
def game_modify(user, game):
    """Modify a game"""
    # TODO
    return render_template('modifyGame.html', title='Create game')
