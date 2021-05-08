from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')


@app.route('/hello/<name>')
def hello_name(name):
    return "<h1>Hello {}!<h1>".format(name)


if __name__ == '__main__':
    app.run(debug=True)

