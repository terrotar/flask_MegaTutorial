
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Musashi"}
    posts = [
        {
            "author": {"username": "Yasuke"},
            "body": "The impossible is possible."
        },
        {
            "author": {"username": "Ieyasu"},
            "body": "The old fox shine with age."
        }
    ]
    return render_template('index.html',
                           title="Home",
                           user=user,
                           posts=posts)
