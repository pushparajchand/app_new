import os
from flask import Flask
app = Flask(_name_)

@app.route("/")
def main():
	return "Welcome!"

@app.route('/how are you')
def hello():
  return 'I am good, how about you?'


if_name_""_name_":
app.run()
