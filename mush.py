#Built in modules
import random,time,os
from random import choice
import json, time
from bs4 import BeautifulSoup
import requests
#adding math
import randfacts
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def power(x, y):
    return x ** y


#class part of the module

class mushroom:
    '''Character mouse mush'''
    species='Apodemus Flavicollis'


    def __int__(self,quotes,insert,fact,change,passgen,changers):
        self.quotes= quotes
        self.insert =insert
        self.fact = fact
        self.change= change
        self.passgen= passgen
        self.changers= changers

# used to get quotes 
    def get_quote(self):
        response = requests.get('https://zenquotes.io/api/quotes') #adding request to get from the website 
        json_data = json.loads(response.text) #loads from json file
        quote = json_data[0]['q'] + " -" + json_data[0]['a'] #quote line + space + author of the quote
        return quote

    
#used to perfrom math using strings
    def mathcommand(self,insert):
        expr = insert #insert the string
        try:
            result = eval(expr)
            return result
        except Exception as e:
            return "Error:", str(e)
        
#part where facts are generated 
    def facts(self,change):
        if change == True:
            # explicit content filter 
            x =randfacts.get_fact(True)
        else:
            x =randfacts.get_fact(False)
        return x
    
#password generator
    def passgenerate(self,changers):
        num="1234567890"
        letter="qwertyuiopasdfghjklzxcvbnm"
        symbol="!@#)({}"
        h= changers
        password=""

        content= num + letter + symbol
        #splitting into a list (array)
        content = content.split()
        content = choice(content)
        if h > 1000:
            #setting a word limit
            return "Sorry We cannot make more than 50 characters"
        else:
            for some in range(h):
                password += choice(content)
            return password

    
    
    
    
