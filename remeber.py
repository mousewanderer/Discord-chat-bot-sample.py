import json
import time

# stored files for remembering 
def get_stored_username():
    file= 'username.json'
    try:
        with open(file) as f:
            username=  json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_stored_age():
    agefile= 'hamster age.json'
    try:
        with open(agefile) as a:
            age=  json.load(a)
    except FileNotFoundError:
        return None
    else:
        return age


# introduction, change username for remembering the username
def get_username():
            username= input('what is your name:')
            file= 'username.json'
            with open(file, 'w') as f:
                json.dump(username,f)
            age=int(input('what is your favorite number:'))
            agefile='hamster age.json'
            with open(agefile, 'w') as a:
                json.dump(age,a)
            print(f"We'll remember you {username}")
            
def Explict_stored():
    file= "Explict.json"
    try:
        with open(file) as f:
            explict=  json.load(f)
    except FileNotFoundError:
        return True
    else:
        return explict

#greeting
def greet_user():
    username = get_stored_username()
    age = get_stored_age()
    if username and age:
        given= f'welcome back {username} '
        return given
    else:
        username= get_username()

#COUNTDOWN by time management tools related
def countdown(given,logic):
    #time to take a break
    while given:
        mins, secs = divmod(given, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        given -= 1

    if logic == 'y':
        nano= 'Times up for your work time and now it is break time!!!'
    elif logic=='n':
        nano='break time is ended and now go back to work!!!'
    else:
        nano='The productivity have been Increase, Time to take a rest'
    return nano


#word files for the selective words that trigger the response

badWords=['crap','f you','bullcrap','prostitute','retard','idiot','porn'
          'rape','loving loli']

base=['animals','animal','hamster','hamsters','rodent','rodents']

goodWords=["your cool",'God bless','your great','be well','well',
               'you are special', 'be kind']

neutralWords=['idc','irl','stfu','stop it']


