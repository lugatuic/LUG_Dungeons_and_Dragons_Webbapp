"""Routing functions for Flask"""

from flask import Flask, flash, redirect, render_template, request, url_for
from dnd_app import app
from dnd_app.account_forms import RegistrationForm


@app.route('/')
def home():
    """Homepage"""
    return render_template('index.html', title='Home')


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
    # TODO
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account Creation Requested for user {}'.format(
            form.username.data))
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
