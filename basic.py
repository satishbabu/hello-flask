from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')


@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', p_name=name)

@app.route('/puppies')
def display_puppies():
    puppies = ['Fluffy', 'Mowgli', 'Clifford']
    return render_template('puppies.html', puppies=puppies)


if __name__ == '__main__':
    app.run(debug=True)

