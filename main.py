from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return 'Hello world'
    def index():
        return "<h1>Hello Earth!</h1>"

