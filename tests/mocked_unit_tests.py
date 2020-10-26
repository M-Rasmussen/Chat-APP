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

KEY_INPUT="input"
KEY_EXPECTED="expected"

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
                KEY_INPUT:
            }
            ]