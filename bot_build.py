'''all functions that are going to be called'''
from os.path import join, dirname
from dotenv import load_dotenv
import random
import json
import os
import requests


DOTENV_PATH = join(dirname(__file__), 'project2.env')
load_dotenv(DOTENV_PATH)
RAPID_API_HOST = os.environ['RAPID_URL_HOST']
RAPID_API_KEY = os.environ['RAPID_URL_KEY']
MESSAGE_TO_RETURN = "RETURN MESSAGE"

def bot_command_parse(bot_command_input, bot_command_message):
    '''Get the message that will be added to the database.'''
    MESSAGE_TO_RETURN = "I did not understand you please enter !! help for all of \
    the inputs I respond to"
    if bot_command_message == "":
        if bot_command_input == "about":
            MESSAGE_TO_RETURN = "I tell jokes, flip coins, and translate your language \
            into high valyrian. Just put !! infront of the commands and I will \
            return as you please. For more information enter !!help"
        elif bot_command_input == "help":
            MESSAGE_TO_RETURN = "!! about and I will tell you about me. !! funtranslate \
            (words), will translate anything after that into high valyrian. \
            !! joke and I will tell you a joke. !! coin flip will result me \
            in flipping a coin and I will tell you the results. "
        elif bot_command_input == "joke":
            MESSAGE_TO_RETURN = get_joke()
    else:
        if bot_command_input == "funtranslate":
            MESSAGE_TO_RETURN = funtranslate(bot_command_message)
        elif bot_command_input == "coin":
            MESSAGE_TO_RETURN = flipcoins()
    return MESSAGE_TO_RETURN

def get_joke():
    '''Get api Joke.'''
    urledz = "https://joke3.p.rapidapi.com/v1/joke"
    headerzed = {
        'x-rapidapi-host': RAPID_API_HOST,
        'x-rapidapi-key': RAPID_API_KEY
    }
    responsezed = requests.request("GET", urledz, headers=headerzed)
    jokereturn = responsezed.json()
    fun_joke = (json.dumps(jokereturn["content"], indent=2))
    return fun_joke
#Use fun translate API
def funtranslate(translate_words):
    '''API translate of words.'''
    funurl = "http://api.funtranslations.com/translate/valyrian?text="
    funurl += translate_words
    funpayload = {}
    funheaders = {}
    funresponse = requests.request("GET", funurl, headers=funheaders, data=funpayload)
    funreturn = funresponse.json()
    fun_pirate = (json.dumps(funreturn["contents"]["translated"], indent=2))
    return fun_pirate

# FOR COIN FLIP
def flipcoins():
    '''coin flips'''
    head_or_tail = random.randint(0, 1)
    if head_or_tail == 1:
        return "heads"
    return "tails"
