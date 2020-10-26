import unittest
import sys
sys.path.append('../')
from bot_build import bot_command_parse
from bot_build import MESSAGE_TO_RETURN
from bot_build import RAPID_API_HOST, RAPID_API_KEY

import unittest.mock as mock
from dotenv import load_dotenv
import os
from os.path import join, dirname

KEY_INPUT = "input"
KEY_BOT_RESPONSE = "expected"

class MockedBotInput:
    def __init__(self, bot_command_input, bot_command_message):
        self.bot_command_input = bot_command_input
        self.bot_command_message = bot_command_message

class MockedBotResponse:
    def __init__(self, bot_response):
        self.bot_response = bot_response
        
class BotBuildTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED:{
                    KEY_BOT_RESPONSE: "I tell jokes, flip coins, and translate your language \
                                        into high valyrian. Just put !! infront of the commands and I will \
                                        return as you please. For more information enter !!help"
                    
                }
            }
            ]