import unittest
import sys
sys.path.append('../')
from bot_build import get_joke, bot_command_parse 
from bot_build import JOKE_URL, JOKE_HEADER, KEY_RESPONSE

#from bot_build import MESSAGE_TO_RETURN, KEY_RESPONSE
from bot_build import RAPID_API_HOST, RAPID_API_KEY

import unittest.mock as mock
from unittest.mock import MagicMock
from dotenv import load_dotenv
import requests
import os
import json
from os.path import join, dirname

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

# joke_response = requests.get(JOKE_URL, headers=JOKE_HEADER)
# joke_response.raise_for_status()
# print (joke_response.content)


class MockedBotInput:
    def __init__(self, bot_command_input, bot_command_message):
        self.bot_command_input = bot_command_input
        self.bot_command_message = bot_command_message

class MockedBotResponse:
    def __init__(self, bot_response):
        self.bot_response = bot_response

    
class MockedGetJokeResponse:
    def __init__(self, text):
        self.text= text
        
class get_joke_test_case(unittest.TestCase):
    def setUp(self):
        self.fail_test_params = [
            {
              KEY_EXPECTED:{
                  KEY_RESPONSE:"the world is flat NOT"
              }
            }
            ]
    def mocked_requests_get(self, joke_url, headers):
        return mock.MagicMock()
    def test_get_joke(self):
        for test_case in self.fail_test_params:
            with mock.patch('requests.get',self.mocked_requests_get):
                joke_response = get_joke(
                    joke_url = JOKE_URL,
                    joke_header = JOKE_HEADER)
            

            
            expected = test_case[KEY_EXPECTED]
                
            
            self.assertNotEqual(joke_response,expected)

if __name__ == '__main__':
    unittest.main()