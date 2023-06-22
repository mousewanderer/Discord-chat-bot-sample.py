#Built in modules
import random,time,os
from random import choice
import json, time
from bs4 import BeautifulSoup
import requests
#adding math
import randfacts

def add_spacing(expression):
    operators = ['+', '-', '*', '/']
    spaced_expression = ""
    for char in expression:
        if char.isdigit() or char in operators:
            spaced_expression += " " + char + " "
        elif char != " ":
            spaced_expression += char
    return spaced_expression.strip()

def calculate(expression):
    parts = expression.split()
    result = 0
    operator = "+"
    pending_operation = None

    for part in parts:
        if part.isdigit():
            if operator == "+":
                result += int(part)
            elif operator == "-":
                result -= int(part)
            elif operator == "*":
                if pending_operation is not None:
                    result = pending_operation(result, int(part))
                    pending_operation = None
                else:
                    result *= int(part)
            elif operator == "/":
                if pending_operation is not None:
                    result = pending_operation(result, int(part))
                    pending_operation = None
                else:
                    result /= int(part)
        else:
            if part == "*":
                pending_operation = lambda x, y: x * y
            elif part == "/":
                pending_operation = lambda x, y: x / y
            else:
                operator = part

    return result



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
        try: # adding this to pass errors
            something= calculate(expr)
        except ValueError:
            something = "Error: Invalid value. Cannot convert the given string to an integer."
        except ZeroDivisionError:
            something= "Error: Division by zero is not allowed."
        except:
            something= "Errorsomething went wrong" #add something wrong
            
        return something
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

    
    
    
    
