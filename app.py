from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
import requests
import json

app = Flask(__name__)


# Connect to database and create database session
# engine = create_engine('sqlite:///flaskstarter.db')
# Base.metadata.bind = engine

def getAllPokemons():
    apiPok = "https://5n6ugc33m6.execute-api.us-east-1.amazonaws.com/api/pokedex"
    r = requests.get(
        url=apiPok)
    json_data = json.loads(r.text)

    final_json_data = list()
    for j in json_data:
        t = dict()
        t["name"] = j["name"]
        t["id"] = j["id"]
        final_json_data.append(t)
    return final_json_data


@app.route('/')
def index():
    r = getAllPokemons()
    # return render_template('index.html', things=things)
    return jsonify(r)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
