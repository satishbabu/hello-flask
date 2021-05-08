from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/puppy/<name>')
def hello_name(name):
    return render_template('puppy.html', name=name)

@app.route('/puppies')
def display_puppies():
    puppies = ['Fluffy', 'Mowgli', 'Clifford']
    return render_template('puppies.html', puppies=puppies)


if __name__ == '__main__':
    app.run(debug=True)

