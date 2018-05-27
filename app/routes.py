from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'kermitt'}
    posts = [
        {
            'author': {'username': 'drfu'},
            'body': 'Finch'
        },
        {
            'author': {'username': 'Momos'},
            'body': 'Example of a loop w/ flask and jinja2'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)