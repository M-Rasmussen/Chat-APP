from os.path import join, dirname
from dotenv import load_dotenv
import random
import json
import os
import requests

class chatBot():
    dotenv_path = join(dirname(__file__), 'project2.env')
    load_dotenv(dotenv_path)
    
    def __init__(self,inputmessage):
        self.message=inputmessage
        self.rapidapihost = os.environ['RAPID_URL_HOST']
        self.rapidapikey= os.environ['RAPID_URL_KEY']
    #Use Rapid host API
    def getJoke(self):
        urledz = "https://joke3.p.rapidapi.com/v1/joke"
        headerzed = {
            'x-rapidapi-host': self.rapidapihost,
            'x-rapidapi-key': self.rapidapikey
        }
        responsezed = requests.request("GET", urledz, headers=headerzed)
        jokereturn=responsezed.json()
        funJoke=(json.dumps(jokereturn["content"],indent=2))
        return funJoke
    #Use fun translate API    
    def funtranslate(self, translateWords):
        funurl = "http://api.funtranslations.com/translate/valyrian?text="
        funurl +=translateWords
        funpayload = {}
        funheaders= {}
        funresponse = requests.request("GET", funurl, headers=funheaders, data = funpayload)
        funreturn=funresponse.json()
        funPirate=(json.dumps(funreturn["contents"]["translated"],indent=2))
        return(funPirate)

    # FOR COIN FLIP
    def flipcoins(self):
        ht=random.randint(0,1)
        if (ht==1):
            return "heads"
        else:
            return "tails"
            
    #Parser to decide what the comand is    
    def botStuff(self):
        rtnMessage=""
        if(self.message[:8]=="!! about" or self.message[:7]=="!!about"):
            rtnMessage= "I tell jokes, flip coins, and translate your language into high valyrian. just put !! infront of the commands and I will return as you please. For more information enter !!help"
        elif(self.message[:7]=="!! help" or self.message[:6]=="!!help"):
            rtnMessage=" !! about and I will tell you about me. !! funtranslate (words), will translate anything after that into high valyrian. !! joke and I will tell you a joke. !! coin flip will result me in flipping a coin and I will tell you the results. "
        elif(self.message[:15]=="!! funtranslate" or self.message[:14]=="!!funtranslate"):
            rtnMessage=self.funtranslate(self.message[15:])
        elif(self.message[:7]=="!! joke" or self.message[:6]=="!!joke"):
            rtnMessage=self.getJoke()
        elif(self.message[:12]=="!! coin flip" or self.message[:11]=="!!coin flip"):
            rtnMessage=self.flipcoins()
        else:
            rtnMessage="I did not understand you please enter !! help for all of the inputs I respond to"
        return(rtnMessage)