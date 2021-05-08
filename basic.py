from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!<h1>"


@app.route('/hello/<name>')
def hello_name(name):
    return "<h1>Hello {}!<h1>".format(name)


if __name__ == '__main__':
    app.run()

