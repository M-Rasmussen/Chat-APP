from os.path import join, dirname
from dotenv import load_dotenv
import random
import json
import os
import requests


dotenv_path = join(dirname(__file__), 'project2.env')
load_dotenv(dotenv_path)
    

rapidapihost = os.environ['RAPID_URL_HOST']
rapidapikey= os.environ['RAPID_URL_KEY']


def botCommandParse(botcommandinput, botcommandinput2):
    rtnMessage="I did not understand you please enter !! help for all of the inputs I respond to"
    if(botcommandinput2==""):
        if(botcommandinput== "about"):
            rtnMessage= "I tell jokes, flip coins, and translate your language into high valyrian. just put !! infront of the commands and I will return as you please. For more information enter !!help"
        elif(botcommandinput== "help"):
            rtnMessage=" !! about and I will tell you about me. !! funtranslate (words), will translate anything after that into high valyrian. !! joke and I will tell you a joke. !! coin flip will result me in flipping a coin and I will tell you the results. "
        elif(botcommandinput=="joke"):
            rtnMessage= getJoke()
    else:
        if(botcommandinput=="funtranslate"):
            rtnMessage= funtranslate(botcommandinput2)
        elif(botcommandinput=="coin"):
            rtnMessage=flipcoins();
    return(rtnMessage)

def getJoke():
    urledz = "https://joke3.p.rapidapi.com/v1/joke"
    headerzed = {
        'x-rapidapi-host': rapidapihost,
        'x-rapidapi-key': rapidapikey
    }
    responsezed = requests.request("GET", urledz, headers=headerzed)
    jokereturn=responsezed.json()
    funJoke=(json.dumps(jokereturn["content"],indent=2))
    return funJoke
#Use fun translate API    
def funtranslate(translateWords):
    funurl = "http://api.funtranslations.com/translate/valyrian?text="
    funurl +=translateWords
    funpayload = {}
    funheaders= {}
    funresponse = requests.request("GET", funurl, headers=funheaders, data = funpayload)
    funreturn=funresponse.json()
    funPirate=(json.dumps(funreturn["contents"]["translated"],indent=2))
    return(funPirate)

# FOR COIN FLIP
def flipcoins():
    ht=random.randint(0,1)
    if (ht==1):
        return "heads"
    else:
        return "tails"
        
  
