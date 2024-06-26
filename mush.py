#Built in modules
import random,time,os
from random import choice
import json, time
from bs4 import BeautifulSoup
import requests
import randfacts
#adding math
import math
# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize



#class part of the module

class mushroom:
    '''Character mouse mush'''
    species='Apodemus Flavicollis'


    def __int__(self,quotes,insert,fact,change,passgen,changers,text):
        self.quotes= quotes
        self.insert =insert
        self.fact = fact
        self.change= change
        self.passgen= passgen
        self.changers= changers
        self.text=text

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

    def Summarizer(self,text):
        text=f"""{text}"""
        # Tokenizing the text
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)
        # Creating a frequency table to keep the
        # score of each word
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
            # Creating a dictionary to keep the score
            # of each sentence
        sentences = sent_tokenize(text)
        sentenceValue = dict()
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
            # Average value of a sentence from the original text
        average = int(sumValues / len(sentenceValue))
        # Storing sentences into our summary.
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence
        return summary

    

    
    
    
    
