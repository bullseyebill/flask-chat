import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>') 
def user(username):
    return "Hi " + username  


if __name__ == "__main__":
    app.run(host=os.getenv('IP', "0.0.0.0"),
            port=int(os.getenv('PORT', 8000)),
            debug=True)



@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}:  {1}".format(username,message)