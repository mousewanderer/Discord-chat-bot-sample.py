#Gui or Built in modules
import random,time
from random import choice
import requests
from bs4 import BeautifulSoup 


    #Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
    #Get the URL
    url = "https://www.google.com/search?q="+coin+"+price"
    #Make a request to the website
    HTML = requests.get(url)
    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')
    #Find the current price
    try:
        text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
        text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    except AttributeError:
        text="Invalid cryptocurrency"
    #Return the text
    return text

class hamster:
    '''Character hamster Charlie'''
    species = "Phodopus Sungorus"


    def __init__(self, name, age,recieve):
        self.name = name
        self.age = age
        self.recieve= recieve
        
        
    def intro(self):
        given=f' Hello {self.name}, my name is Charlie the hamster and {self.age} is your favorite number'
        return given
                
        
# bots' lines
    def casual(self):
        def mix():
            casual1 = 'Squeak Pardon me'
            casual2 = 'H..H..HiI...Hi!'
            casual3 = 'well what do you know'
            casual4 = 'Hello I am Rordrigo Charlineus Carrotino JB. Delijamous'
            casual5 = 'munch'
            casual6 = 'Do you like carrots'
            casual7 = "how do sweet corn grow?"
            casual8 = 'Do you know somebody named mush?'
            casual9 = 'Bucketz protect me from falling'
            casual10 = "I'm just a gentlehamster"
            secretword='My creator is the mouse the wanders around that likes hamsters'
            secretword2="I am coded with something called python "
            secretword3="My friend named mush quotes are all searched up in the internet"
            gona=[secretword2,casual1,casual9,secretword3]
            gonan= choice(gona)
            lineer1=[casual10,casual1,casual9,secretword,gonan]
            lineer= choice(lineer1)
            lines= [casual2,casual3,casual4,casual5, casual6,casual7,casual8,casual10,lineer]
            mix=choice(lines)
            return mix
        
        for num in range(0,1):
            time.sleep(1)
            given=mix()
            return given

    def infoReference(self):
        q="Sadi doesn't know that hamsters' live only for 2 years"
        q1='My favorite song is the hamster song'
        q2='Wild life hamsters are endangered than domesticated'
        q3="I don't want to be near someone named meowbah, I don't need to explain"
        
           
#good
    def respond(self,recieve):
        good1="Those are kind words my friend"
        good2='Thanks human, for being well mannered '
        good3='Those are uplifting words'
        good4='you are also cool too'
        good5='Same thing goes to you too thank you'

        respond_good=[good1,good2,good3]
        def r_g():
            mix=choice(respond_good)
            return mix
#neutral
        neutral1='hmmmm.....'
        neutral2='Ummm...???'
        neutral3='Huuhh????'

        respond_neutral=[neutral1,neutral2,neutral3]
        def r_n():
            mix=choice(respond_neutral)
#bad            
            return mix
        bad1='My friend Mush said that bad words are bad manners'
        bad2='Please Mind your words'
        bad3='Well those words are\'nt elegant '
        bad4='Improper mouth goes to an improper place'

        respond_bad=[bad1,bad2,bad3]
        def r_b():
            mix=choice(respond_bad)
            return mix
        
        if recieve== 'good':
            time.sleep(1)
            given=r_g()
            return given
        elif recieve=='bad':
            time.sleep(1.5)
            given=r_b()
            return given
        elif recieve=='neutral' :
            given=r_n()
            return given

    def help(self):
        words = ' HERE ARE THE LIST OF COMMANDS BE SURE TO ON NOTIFICATIONS FOR BETTER EXPERIENCE \n \n'
        words1 = '?help - for the list of commands \n \n'
        words2 = '?math- for perform calculation \n \n'
        words4 = '?change - changes the username \n \n'
        words5 = '?cointoss - flip a coin\n\n'
        words6 = '?rps - rock paper scissors\n\n'
        words7 = '?casual - random casual talk \n \n'
        words8='?dice - rolling numbers from 1 to 6 \n \n'
        words9='?pomodoro - This sets the pomodoro technique \n \n'
        words10='?5217 - This sets the 52/17 technique \n \n'
        words11='?quotes - Giving random inspirational quotes \n \n'
        words12='?cryptoprice (coins) - Get the price of the cryptocurrency \n \n'
        full_text=words + words1 + words2+ words4 + words5
        second_text= words6 + words7 + words8 + words9 + words10 + words11
        third_text = words12
        whole= full_text + second_text +third_text
        return whole


    def cryptoPrice(self,recieve):
    #Choose the cryptocurrency that you want to get the price of (e.g. bitcoin, litecoin)
        crypto = recieve
        #Get the price of the crypto currency
        price = get_crypto_price(coin=crypto)
        return price

