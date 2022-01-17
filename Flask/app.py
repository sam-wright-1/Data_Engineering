# from flask import Flask

# app = Flask(__name__)
# @app.route('/hello/', methods=['GET', 'POST'])
# def welcome():
#     return "Hello World!"
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=105)
    
    

    
    
from flask import Flask
from flask import jsonify    
from flask import request
from flask import Blueprint    
from home import home_bp
from contact import contact_bp
    
app = Flask(__name__)

@app.before_request
def before():
    print("This is executed BEFORE each request.")

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)
@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name
@app.route('/person/')
def json():
    return jsonify({'name':'Jimit',
                    'address':'India'})

@app.route('/home/')
def home():
    return "Home page"

# Will give you an error if you go to the url "/contact/" and not"/contact"
@app.route('/contact')
def contact():
    return "Contact page"


@app.route('/teapot/')
def teapot():
    return "Would you like some tea?", 69

app.register_blueprint(home_bp, url_prefix='/home')
#http://localhost:5000/contact/hello/
app.register_blueprint(contact_bp, url_prefix='/contact')

# app.logger.debug('This is a DEBUG message')
# app.logger.info('This is an INFO message')
# app.logger.warning('This is a WARNING message')
# app.logger.error('This is an ERROR message')

app.run()
