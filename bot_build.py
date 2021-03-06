"""all functions that are going to be called"""
from os.path import join, dirname
from dotenv import load_dotenv
import random
import json
import os
import requests


DOTENV_PATH = join(dirname(__file__), "project2.env")
load_dotenv(DOTENV_PATH)
JOKE_URL = "https://joke3.p.rapidapi.com/v1/joke"
RAPID_API_HOST = os.environ["RAPID_URL_HOST"]
RAPID_API_KEY = os.environ["RAPID_URL_KEY"]
JOKE_HEADER = {"x-rapidapi-host": RAPID_API_HOST, "x-rapidapi-key": RAPID_API_KEY}
KEY_BOT_RESPONSE = "bot_response"
KEY_RESPONSE = "response"
FUN_URL = "http://api.funtranslations.com/translate/valyrian?text="


def bot_command_parse(bot_command_input, bot_command_message):
    """Get the message that will be added to the database."""
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
            x = get_joke(JOKE_URL, JOKE_HEADER)
            bot_return_message = x.get(KEY_RESPONSE)
    else:
        if bot_command_input == "funtranslate":
            bot_return_message = funtranslate(bot_command_message)
        elif bot_command_input == "coin":
            bot_return_message = flipcoins()
    return bot_return_message


def get_joke(joke_url, joke_header):
    """Get api Joke."""
    joke_response = requests.get(joke_url, headers=joke_header).json()
    joke = joke_response.get("content")
    return {KEY_RESPONSE: joke}


# Use fun translate API
def fun_translate_concat(translate_words):
    fun_url= FUN_URL
    fun_url= fun_url+translate_words
    return fun_url


def funtranslate(translate_words):
    """API translate of words."""
    funurl = fun_translate_concat(translate_words)
    funresponse = requests.get(funurl).json()
    fun_pirate = funresponse['contents']['translated']
    return fun_pirate


# FOR COIN FLIP
def flipcoins():
    """coin flips"""
    head_or_tail = random.randint(0, 1)
    if head_or_tail == 1:
        return "heads"
    return "tails"


def concat_messages(all_messages, all_names):
    """concat all the messages"""
    arrayList = []
    for x in range(len(all_messages)):
        messageOp = all_names[x]
        messageOp += ": "
        messageOp += all_messages[x]
        arrayList.append(messageOp)
    return arrayList
