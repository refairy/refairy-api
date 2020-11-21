import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, ReFairy!"


def main():
    filename = os.path.abspath(__file__)
    os.environ['FLASK_APP'] = filename
    os.system("flask run")

if __name__ == "__main__":
    main()
