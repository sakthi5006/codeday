from flask import Flask
import os

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/')
def index():
    return 'Index page'

@app.route('/username/<username>')
def user(username):
    return 'User %s' % username

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
