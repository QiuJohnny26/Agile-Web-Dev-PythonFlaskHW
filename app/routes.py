from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return("Hello, World !");

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1,num2):
    return '{} * {} = {}'.format(num1,num2,num1*num2)
@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1,num2):
    return '{} / {} = {}'.format(num1,num2,num1/num2);
@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1,num2):
    return '{} - {} = {}'.format(num1,num2,num1-num2)
@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return '{} + {} = {}'.format(num1,num2,num1+num2);




##print("1 + 2 = ....")
##print(calculator.add(1,2))
##print("1 - 2 = ....")
##print(calculator.subtract(1,2))
##print("1 * 3 = ....")
##print(calculator.multiply(1,3))
##print("10 / 5 = ....")
##print(calculator.division(10,5))
##