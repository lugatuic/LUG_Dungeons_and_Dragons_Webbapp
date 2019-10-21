from flask import Flask, flash, redirect, render_template, request, url_for
from dnd_app import app



@app.route('/')
def home():
    return render_template('login.html', title='Home')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()  # username +password
    if request.method == 'POST':  # TODO
        print("yes")
    return render_template('login.html', title='Sign In', form=form)


@app.route('/createAccount', methods=['POST', 'GET'])
def accountCreate():  # needs Username password, email
    # TODO
    form = RegistrationForm()
    return render_template('accountCreation.html', title='Create Account', form=form)


@app.route('/<user>/createCharacter', methods=['POST', 'GET'])
def characterCreate(user):
    # TODO
    return render_template('characterCreation.html', title='Create Character')


@app.route('/<user>/createItem', methods=['POST', 'GET'])
def itemCreate(user):  # Name, cost, wieght, Availabity +flavor text/ability/uses
    # TODO
    return render_template('itemCreation.html', title='Create item')


@app.route('/<user>/createWeapon', methods=['POST', 'GET'])
def weaponCreate(user):  # Name, Class, Range, Damage, Penetration, Special, Weight, Cost, Availabity, Flavor
    # TODO
    return render_template('weaponCreation.html', title='Create Weapon')


@app.route('/<user>/createGame', methods=['POST', 'GET'])
def gameCreate(user):
    if request.method == 'POST':
        gameFile = {"game_name":"","Dungeon_Master":"","gameID": 4,"Users":[],"msgLog":[]}
    # TODO
    return render_template('gameCreation.html', title='Create game')

@app.route('/<user>/modifyGame', methods=['POST', 'GET'])
def gameModify(user, game):
    # TODO
    return render_template('modifyGame.html', title='Create game')
