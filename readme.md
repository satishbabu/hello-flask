# hello-flask
Simple flask program

## Python Setup

Craete a pythgon virtual environment to keep the dependencies independent.  Activate the enviornemnt and then install flask in it.

```linux
sudo apt-get install python3-venv
cd ~/projects
python3 -m venv flask-python-venv
source ~/proejcts/bin/activate 
pip3 install flask
```

## Run

```linux
python3 basic.py

```

## Debug
Set the debug to True "app.run(debug=True)".  Note down the PIN from the console and then Python allows debug from the webpage.  Note that this has to be turned off in production.