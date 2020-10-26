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
KEY_BOT_RESPONSE = "bot_response"

def bot_command_parse(bot_command_input, bot_command_message):
    '''Get the message that will be added to the database.'''
    bot_return_message = "I did not understand you please enter !! help for all of \
    the inputs I respond to"
    if bot_command_message == "":
        if bot_command_input == "about":
            bot_return_message = "I tell jokes, flip coins, and translate your language \
            into high valyrian. Just put !! infront of the commands and I will \
            return as you please. For more information enter !!help"
        elif bot_command_input == "help":
            bot_return_message = "!! about and I will tell you about me. !! funtranslate \
            (words), will translate anything after that into high valyrian. \
            !! joke and I will tell you a joke. !! coin flip will result me \
            in flipping a coin and I will tell you the results. "
        elif bot_command_input == "joke":
            bot_return_message = get_joke()
    else:
        if bot_command_input == "funtranslate":
            bot_return_message = funtranslate(bot_command_message)
        elif bot_command_input == "coin":
            bot_return_message = flipcoins()
    return{
        KEY_BOT_RESPONSE: bot_return_message}

def get_joke():
    '''Get api Joke.'''
    joke_url = "https://joke3.p.rapidapi.com/v1/joke"
    joke_header = {
        'x-rapidapi-host': RAPID_API_HOST,
        'x-rapidapi-key': RAPID_API_KEY
    }
    joke_response = requests.request("GET", joke_url, headers=joke_header)
    joke_parsed = joke_response.json()
    fun_joke = (json.dumps(joke_parsed["content"], indent=2))
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
