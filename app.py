from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash


app = Flask(__name__)


# Connect to database and create database session
# engine = create_engine('sqlite:///flaskstarter.db')
# Base.metadata.bind = engine


@app.route('/')
def index():
    things = ["thing1", "thing2", "cat-in-the-hat"]
    return render_template('index.html', things=things)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
