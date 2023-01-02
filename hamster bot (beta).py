#Api or Built in modules by multiple 
import random,time,json, discord
from random import choice
from discord.ext import commands
import datetime 
from urllib import parse, request
from dotenv import load_dotenv


#made modules by the programmer
import remeber
from remeber  import greet_user,  get_stored_username, get_username 
from remeber import get_stored_age, countdown, badWords ,goodWords, neutralWords


#character's purpose to import command lines
import char
from char import hamster
#adding another character name mush
import mush
from mush import mushroom


#Boolean stuff
# masterkey is the name change
masterkey=True
#rororo is the favorite number change
rororo=True
# mathematics used to notify string to math
mathematics=True
# turn used for the game rock paper scissors
turn=True

#important and setted info for the correct request
username=  get_stored_username()
age= get_stored_age()
player=hamster(name= username,age=age,recieve='neutral')

addon=mushroom()

# The bottom line is the discord bot running code for commands 

bot = commands.Bot(command_prefix="!")
#used to notify the 
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
#change user name command line
    elif message.content.lower()=='?change':
        await message.channel.send('what is your name?') #request the name
        global masterkey #global function used to change details in if_else
        masterkey= False #turning it false to obey the elif line below

    elif message.content==message.content and masterkey==False:
        username=message.content
        file= 'username.json' #open the file of the username
        with open(file, 'w') as f:
                json.dump(username,f) #dumped in json file
        await message.channel.send(str('what is your favorite number?')) #request favorite number
        global rororo #global function used to change details in if_else
        rororo= False # turning it false to obey the elif line below
        masterkey=True #setting back to true to prevent line conflict
        
#change user's favorite number
    elif message.content==message.content and rororo==False:
        age=message.content 
        agefile='hamster age.json' #open the file of the favorite number
        with open(agefile, 'w') as a:
                json.dump(age,a)
        await message.channel.send(f'We will remember your name and your favorite number')
        rororo= True #setting back to true to prevent line conflict



#chatting line for specific keywords given in this line and any support
    if message.content.startswith('hello'):
        await message.channel.send('Hello, I am Charlie the hamster')

#adding introduction of the bot
    elif message.content.lower() =='intro' :
        await message.channel.send(player.intro())
        
#for saying vulgar words which it can respond
    for element in range(len(badWords)):
        if badWords[element] in message.content or badWords[element].upper() in message.content or badWords[element].lower() in message.content:
            await message.channel.send(player.respond(recieve='bad'))

#for saying kind words or compliment which also can respond
    for element1 in range(len(goodWords)):
        if goodWords[element1] in message.content or goodWords[element1].upper() in message.content or goodWords[element1].lower() in message.content:
            await message.channel.send(player.respond(recieve='good'))

#for saying questionable words that can also respond
    for element2 in range(len(neutralWords)):
        if neutralWords[element2] in message.content or neutralWords[element2].upper() in message.content:
            await message.channel.send(player.respond(recieve='neutral'))

#random message sending 
    if message.content == '?casual':
        await message.channel.send(player.casual())

#dice roll 1 to 6 sides 
    elif message.content =='?dice':
        dice=[1,2,3,4,5,6]
        diceroll= choice(dice)
        await message.channel.send(diceroll)

    elif message.content =='?help':
        await message.channel.send(player.help())

#making the bot doing math

    elif  "?math" in message.content:
        global mathematics
        mathematics= False
        await message.channel.send('What do you want to calculate?')
        await message.channel.send("I can't do parenthesis and please use numerical symbols")
        await message.channel.send(" + : addition \n- : subtraction\n * : multiplication\n/ : division with + 1\n^: raise to the power of ")

    elif message.content==message.content and mathematics==False:
        await message.channel.send(f'The answer of {message.content} is')
        value= message.content
        await message.channel.send(addon.mathcommand(insert=value))
        mathematics= True
        
        
#Time management start
    elif message.content=='?pomodoro':
        await message.channel.send("Your 25 minute work time have been started ")
        base= 25 
        given= base*60 #turning 25 sec to 25 minutes
        #intial of 25 minutes of work and +5 minutes in every break
        await message.channel.send(countdown(given=given,logic='y'))
        breaktime=given + 5*60 #25 minutes + 5 minutes = total 30 minutes
        #30 minutes - 25 minutes(intial given)= 5 minute break time
        await message.channel.send(countdown(given=breaktime,logic='n'))
        given2= given + breaktime #25 minutes + 30 minutes = 55 minutes
        #55 minutes - 30 minutes(break time) -= 25 minutes of work
        await message.channel.send(countdown(given=given2,logic='y'))
        breaktime=given2 + 10*60 #55 minutes + 10 minutes = 65 minutes
        #65 minutes - 55 minutes(given2)= 10 minute break
        await message.channel.send(countdown(given=breaktime,logic='n'))
        given3 = given +breaktime #25 minutes  + 65 minutes = 90 minutes
        #90 minutes - 65 minutes = 25 minutes of work
        await message.channel.send(countdown(given=given3,logic='y'))
        breaktime=given3 + 15*60 #90 minutes +15 minutes= 105 minutes
        await message.channel.send(countdown(given=breaktime,logic='stop'))

    elif message.content=='?5217':
         await message.channel.send("Your 52 minute work time have been started ")
         base=52
         given=52*60 #turning 52 sec to 52 minutes
         await message.channel.send(countdown(given=given,logic='y'))
         breaktime=given + 17*60 #52 minutes + 17 minutes= 69 minutes
         await message.channel.send(countdown(given=breaktime,logic='n'))
         given2= given + breaktime # 52 minutes + 69 minutes = 121 minutes 
         await message.channel.send(countdown(given=given2,logic='y'))
         breaktime=given2 + 17*60 # 121 minutes + 17 minutes = 138 minutes
         await message.channel.send(countdown(given=breaktime,logic='stop'))

#stock price crypto
    elif '?cryptoprice' in message.content:
        value= message.content
        await message.channel.send(f'The price of {value}')
        #removing cryptoprice in the message
        msg=value.replace('?cryptoprice', '')
        await message.channel.send(player.cryptoPrice(recieve=msg))
        
# adding quotes function
    elif '?quote' in message.content:
        await message.channel.send(addon.get_quote())

    elif '?cointoss' in message.content:
        cointoss=['The coin landed on heads', 'The coin landed on tails']
        coinrange=choice(cointoss)
        await message.channel.send(coinrange)
# rock paper scissors 
    elif message.content in '?rps':
        await message.channel.send('okay I will play')
        await message.channel.send('What do you choose?  \nrock\npaper\nscissor')
        global turn
        turn= False

    elif message.content== message.content and turn==False:
        winner="you win this round"
        loser="you lose this round"
        draw="This is a draw"
        target= message.content.lower()
        Item=['rock','paper','scissor']
        aibet=choice(Item)
        if aibet == 'scissor':
            if target== 'rock' and target in Item:
                result=winner
            elif target =="scissor" and target in Item:
                result=draw
            else: result= loser
        elif aibet== "rock":
            if target=="paper" and target in Item:
                result= winner
            elif target== "rock" and target in Item:
                result= draw
            else: result =loser
        elif aibet=="paper":
            if target=="scissor" and target in Item:
                result=winner
            elif target=="paper" and target in Item:
                result=draw
            else: result= loser
        else: result="sorry invalid item"
        await message.channel.send(result)
        turn= True
        
        

bot.run('Insert token')



    

