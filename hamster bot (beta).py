#________________________________________________
                                         #      |   
#Api or Built in modules by multiple     #      |
import random,time, json                 #      |
import discord                           #     /
import requests                          #    /
from random import choice                #   /
from random import shuffle               #  |
from discord.ext import commands         #  |
import datetime                          #  |
from urllib import parse, request        # /
#________________________________________#/
#
#
#
#
#
#
#
#_______________________________________________________________________________________________________________
                                                                                                                #
#made modules by the programmer                                                                                 #
import remeber                                                                                                  #
from remeber  import greet_user,  get_stored_username, get_username, Explict_stored                             #
from remeber import get_stored_age, countdown, badWords ,goodWords, neutralWords                                #
#---------------------------------------------------------------------------------------------------------------#
#character's purpose to import command lines                                                                    #                                                           
import char                                                                                                      #
from char import hamster                                                                                         #
#adding another character name mush                                                                              #
import mush                                                                                                      #
from mush import mushroom                                                                                        #
                                                                                                                 #
#adding another another character name Timmy                                                                     #
import Timmy                                                                                                     #
from Timmy import roboTim                                                                                       #
#---------------------------------------------------------------------------------------------------------------#
#important and setted info for the correct request                                                              #
username=  get_stored_username()                                                                                #
age= get_stored_age()                                                                                           #
player=hamster(name= username,age=age,recieve='neutral')                                                        #
                                                                                                                #
addon=mushroom()
robo=roboTim()                                                                                                  #
#_______________________________________________________________________________________________________________#



#____________________________________________________________________________________________
#Boolean stuff                                                                               #
# masterkey is the name change                                                               #
masterkey=True                                                                               #
#rororo is the favorite number change                                                        #
rororo=True                                                                                 #
# mathematics used to notify string to math                                                 #
mathematics=True                                                                            #******
# turn used for the game rock paper scissors                                                #******-------
turn=True                                                                                   #****** 
#passgen                                                                                    #******
passgenerator=True                                                                          #******+++++++
#filter content                                                                             #******
notexplict = True                                                                           #
#math operation while loop                                                                  #
creeet=True                                                                                 #
#Russian Roullete                                                            _______________#
RussianRoullete= True                                                       #
Summaries=True                                                              #
#___________________________________________________________________________#



# The bottom line is the discord bot running code for commands 
bot = commands.Bot(command_prefix="!",intents=discord.Intents.default())
#used to notify the 
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
global previous_message
previous_message = ""
global message_count
message_count = {}

    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # Create a dictionary to store the message count


# Create a variable to store the previous message for spams

    # Clear the message_count dictionary if the previous message is different from the current message
    global previous_message
    global message_count 
    if previous_message != message.content:
        message_count.clear()
        previous_message = message.content

    # Check if the message is in the message_count dictionary
    if message.content in message_count:
        message_count[message.content] += 1
    else:
        message_count[message.content] = 1

    # Check if the message has been repeated 10 times
    if message_count[message.content] >= 10:
        await message.channel.send("Stop Spamming please")

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
        #global function used to change details in if_else
        global rororo
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
        await message.channel.send(" + : addition \n- : subtraction\n* : multiplication\n/ : division\n^: raise to the power of ")
        await message.channel.send("Example: 8 + 3 / 1 - 2 * 12")
        

    elif message.content==message.content and mathematics==False:
        if message.content=="q" or message.content=="Q" and mathematics==False:
            mathematics= True
            await message.channel.send("Exitted Math Operation")
            
        else:
            await message.channel.send(f'The answer of {message.content} is')
            value= message.content
            await message.channel.send(addon.mathcommand(insert=value))
            await message.channel.send('What else do you want to calculate \nType "q" to quit')
        
        
        
#Time management start
    elif message.content=='?pomodoro':
        await message.channel.send("Your 25 minute work time have been started ")
        base= 25
        mins= 1
        given= base* mins #turning 25 sec to 25 minutes
        #intial of 25 minutes of work and +5 minutes in every break
        await message.channel.send(countdown(given=given,logic='y'))
        breaktime=given + 5* mins #25 minutes + 5 minutes = total 30 minutes
        #30 minutes - 25 minutes(intial given)= 5 minute break time
        await message.channel.send(countdown(given=breaktime,logic='n'))
        given2= given + breaktime #25 minutes + 30 minutes = 55 minutes
        #55 minutes - 30 minutes(break time) -= 25 minutes of work
        await message.channel.send(countdown(given=given2,logic='y'))
        breaktime=given2 + 10*mins #55 minutes + 10 minutes = 65 minutes
        #65 minutes - 55 minutes(given2)= 10 minute break
        await message.channel.send(countdown(given=breaktime,logic='n'))
        given3 = given +breaktime #25 minutes  + 65 minutes = 90 minutes
        #90 minutes - 65 minutes = 25 minutes of work
        await message.channel.send(countdown(given=given3,logic='y'))
        breaktime=given3 + 15* mins #90 minutes +15 minutes= 105 minutes
        await message.channel.send(countdown(given=breaktime,logic='stop'))

    elif message.content=='?5217':
         await message.channel.send("Your 52 minute work time have been started ")
         base=52
         mins=60
         given=52*60 #turning 52 sec to 52 minutes
         await message.channel.send(countdown(given=given,logic='y'))
         breaktime=given + 17*mins #52 minutes + 17 minutes= 69 minutes
         await message.channel.send(countdown(given=breaktime,logic='n'))
         given2= given + breaktime # 52 minutes + 69 minutes = 121 minutes 
         await message.channel.send(countdown(given=given2,logic='y'))
         breaktime=given2 + 17*mins# 121 minutes + 17 minutes = 138 minutes
         await message.channel.send(countdown(given=breaktime,logic='stop'))

#stock price crypto
    elif '?cryptoprice' in message.content:
        value= message.content
        #removing cryptoprice in the message
        msg=value.replace('?cryptoprice', '')
        await message.channel.send(f'The price of {msg} is')
        await message.channel.send(player.cryptoPrice(recieve=msg))
        
# adding quotes function
    elif '?quote' in message.content:
        await message.channel.send(addon.get_quote())

    elif '?cointoss' in message.content:
        cointoss=['The coin landed on heads', 'The coin landed on tails']
        coinrange=choice(cointoss)
        await message.channel.send(coinrange)
# rock paper scissors 
    elif message.content == '?rps':
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
        
#Generating facts
    elif '?fact' == message.content:
        change= Explict_stored()
        global notexplict
        if notexplict == False:
            await message.channel.send("Explict Deactivated")
        else:
            await message.channel.send("Explict Activated")
        await message.channel.send(addon.facts(change))

    elif '?factchange' == message.content:
        await message.channel.send('Do you want to turn on explict(yes/no)?')
        notexplict = False
#turning off and on the explict content
    elif notexplict == False  and message.content== message.content:
         if "yes" == message.content.lower():
             change = False
         elif "no" == message.content.lower():
             change = True
         else:
             change = True
         file= 'Explict.json' #open the file of the username
         with open(file, 'w') as f:
             json.dump(change,f) #dumped in json file
         await message.channel.send(' ?')

         notexplict = True
         
#Generating passwords    
    elif '?passgen' == message.content:
         await message.channel.send('How many characters needed in the password?')
         await message.channel.send('(default 8 characters) (cannot generate more than 1000 characters')
         global passgenerator
         passgenerator=False
    elif message.content== message.content and passgenerator==False:
        try:
            trial = int(message.content)
        except ValueError:
            trial = 8
        await message.channel.send(addon.passgenerate(trial))
        passgenerator= True

 #Russian Roullete Game    
    elif message.content in '?russianroullete':
        await message.channel.send('*Charlie suddenly changes his appearance into more sinister look')
        await message.channel.send("I always bring my revolver around me. \nIn 1 bullet in 6 chambers, \nsay spin if you want it to spin. \nsay anything else then it is a shoot")
        global RussianRoullete #global function used to activate russian roullete in if_else
        RussianRoullete= False

    elif message.content=="spin" and RussianRoullete==False or message.content=="Spin" and RussianRoullete==False:
        cartidge = ["empty","empty","empty","empty","empty","bullet"]
        def shuffle_list(lst):
            lst2 = lst.copy()
            random.shuffle(lst2)
            return lst2
        S_cartidge = shuffle_list(cartidge)
        if S_cartidge[0] == "empty":
            await message.channel.send("You did not die")
        elif S_cartidge[0] == "bullet":
            await message.channel.send("You are dead")
        else:
            await message.channel.send("My gun is broken")
        RussianRoullete= True
    elif message.content==message.content and RussianRoullete==False:
        cartidge = ["empty","empty","empty","empty","empty","bullet"]
        value= choice(cartidge)
        if value == "empty":
            await message.channel.send("You did not die")
        elif value == "bullet":
            await message.channel.send("You are dead")
        else:
            await message.channel.send("My Gun is broken")
        RussianRoullete= True
#sends random memes
    elif message.content=="?meme" :
        content = requests.get("https://meme-api.com/gimme").text
        data = json.loads(content)
        embed = discord.Embed(title=f"{data['title']}", color=discord.Colour.random()).set_image(url=f"{data['url']}")
        await message.channel.send(embed=embed)

#summarizer
    elif message.content== "?summary":
        await message.channel.send("What do you want to summarize.\nMake sure it is 2 paragraphs long")
        global Summaries
        Summaries = False

    elif message.content==message.content and Summaries==False:
        long= message.content
        await message.channel.send(addon.Summarizer(long))
        Summaries = False

    elif message.content== "?identity":
        await message.channel.send("loading")
        await message.channel.send(robo.Isubmit())


    
    
        
#add a discord token this line of code
bot.run('Insert token here')



    

