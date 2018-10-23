# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:24:26 2018

@author: Aman Gupta
"""

import firebase_admin
from firebase_admin import db
import flask

app = flask.Flask(__name__)

firebase_admin.initialize_app(options={
    'databaseURL': 'https://<DB_NAME>.firebaseio.com'
})
SUPERHEROES = db.reference('superheroes')

@app.route('/heroes', methods=['POST'])
def create_hero():
    req = flask.request.json
    hero = SUPERHEROES.push(req)
    return flask.jsonify({'id': hero.key}), 201

@app.route('/heroes/<id>')
def read_hero(id):
    return flask.jsonify(_ensure_hero(id))

@app.route('/heroes/<id>', methods=['PUT'])
def update_hero(id):
    _ensure_hero(id)
    req = flask.request.json
    SUPERHEROES.child(id).update(req)
    return flask.jsonify({'success': True})

@app.route('/heroes/<id>', methods=['DELETE'])
def delete_hero(id):
    _ensure_hero(id)
    SUPERHEROES.child(id).delete()
    return flask.jsonify({'success': True})

def _ensure_hero(id):
    hero = SUPERHEROES.child(id).get()
    if not hero:
        flask.abort(404)
    return hero