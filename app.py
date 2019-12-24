from bson.int64 import Int64
from bson import json_util, ObjectId
from pymongo import MongoClient, CursorType, ASCENDING, DESCENDING
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
import requests
import json
import re

app = Flask(__name__)


# DB links for pokedexDB collection
client = MongoClient("mongodb://localhost:27017")
database = client["local"]
collection = database["pokedexDB"]


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


def createNewCategoryInDB():
    # Get last category number
    results = collection.find({})

    for k in results[0]["data"]["new"].keys():
        cat = k
    cat = [int(s) for s in re.findall(r'-?\d+\.?\d*', cat)][0]

    collection.update_one(
        {"user": "user1"},
        {"$set": {f"data.new.category{cat+1}": []}}
    )


@app.route('/')
def index():
    r = getAllPokemons()
    # return render_template('index.html', things=things)
    return jsonify(r)


@app.route('/createNewCategory')
def createNewCategory():
    createNewCategoryInDB()
    # return render_template('index.html', things=things)
    return jsonify("success")


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
