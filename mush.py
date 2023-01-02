#Built in modules
import random,time,os
from random import choice
import json, time
from bs4 import BeautifulSoup
import requests
#adding math
import operator

#setting digits to recognize the numerical value 
DIGITS = set('0123456789')
# Using operators to define the value of the symbols
OPERATIONS = {
    '+' : operator.add, #addition
    '-' : operator.sub, #subtraction
    '*' : operator.mul, #multiplication
    '/' : operator.floordiv, #division with + 1
    '^' : operator.pow, #raise to the power of 
}

#used to return to digits
def is_digit(var):
    return var in DIGITS

#used to collect numbers available to the string (scanning phase)
def get_number(varstr):
    s = ""
    if varstr[0] == '-':
        s += "-"
        varstr = varstr[1:]
    for c in varstr:
        if not is_digit(c):
            break
        s += c
    return (int(s), len(s))
# performing the math stuff
def perform_operation(string, num1, num2):
    op = OPERATIONS.get(string, None)
    if op is not None:
        return op(num1, num2)
    else:
        return None
# Handle things to evade possible errors of the calculations

def eval_math_expr(expr):
    while True:
        try: 
            number1, end_number1 = get_number(expr)
            expr = expr[end_number1:]
            if expr == '':
                return number1
            op = expr[0]
            expr = expr[1:]
            number2, end_number2 = get_number(expr)
            number1 = perform_operation(op, number1, number2)
            expr = str(number1) + expr[end_number2:]
        except Exception as e:
            print(e)
            break
    return number1

#class part of the module

class mushroom:
    '''Character mouse mush'''
    species='Apodemus Flavicollis'


    def __int__(self,quotes,insert):
        self.quotes= quotes
        self.insert =insert

# used to get quotes 
    def get_quote(self):
        response = requests.get('https://zenquotes.io/api/quotes') #adding request to get from the website 
        json_data = json.loads(response.text) #loads from json file
        quote = json_data[0]['q'] + " -" + json_data[0]['a'] #quote line + space + author of the quote
        return quote
#used to perfrom math using strings
    def mathcommand(self,insert):
        expr = insert #insert the string
        try: # adding this to pass errors
            something= eval_math_expr(expr)
        except:
            something= "something went wrong" #add something wrong
        else: #other errors
            for expr, res in {"2": 2, "2*4": 8, "4+8": 12, "100/3": 33, "2^3": 8, "-2": -2, "-2-3": -5}.items():
                result = eval_math_expr(expr)
                if res != result:
                    something= "Computing", expr, "got", result, "instead of", res
        return something


    
    
    
