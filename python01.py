from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/world')
def world():
    return 'Hello World!'

@app.route("/login")
def login():
    pass


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
    # /user/test => User test


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    # /post/1 => Post 1


if __name__ == '__main__':
    app.run(debug=True)
