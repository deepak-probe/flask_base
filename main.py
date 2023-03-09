# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/base')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello World test5'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name



# main driver function
if __name__ == '__main__':
	app.run(host =  '0.0.0.0', port=5001, debug=True)
	# run() method of Flask class runs the application
	# on the local development server.
	# app.run()
