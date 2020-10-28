import unittest
import sys
sys.path.append('../')
import bot_build
from bot_build import get_joke, funtranslate, bot_command_parse, flipcoins
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




class MockedBotInput:
    def __init__(self, bot_command_input, bot_command_message):
        self.bot_command_input = bot_command_input
        self.bot_command_message = bot_command_message

class MockedBotResponse:
    def __init__(self, bot_response):
        self.bot_response = bot_response

class MockFunTranslate:
    def __init__(self, text):
        self.text=text
    
class MockedGetJokeResponse:
    def __init__(self, text):
        self.text= text
        
class get_joke_test_case(unittest.TestCase):
    def setUp(self):
        self.fail_test_params_get_joke = [
            {
              KEY_EXPECTED:{
                  KEY_RESPONSE:"the world is flat NOT"
              }
            }
            ]
            
        self.fail_test_params_funtranslate = [
            {
            KEY_INPUT: "this is nice",
            KEY_EXPECTED:{
                KEY_RESPONSE:"bisa iksos nice"
            }
            }
            ]
            
        self.success_coin_flip_params = [{
            KEY_EXPECTED:"heads"
        }]
        
    def mocked_requests_get(self, joke_url, headers):
        return mock.MagicMock()
    def test_get_joke(self):
        for test_case in self.fail_test_params_get_joke:
            with mock.patch('requests.get',self.mocked_requests_get):
                joke_response = get_joke(
                    joke_url = JOKE_URL,
                    joke_header = JOKE_HEADER)
            expected = test_case[KEY_EXPECTED]
            self.assertNotEqual(joke_response,expected)
            
    # def mocked_requests_get_fun(self, translatewords):
    #     return mock.MagicMock()
    # def test_get_funtranslate(self):
    #     for test_case in self.fail_test_params_funtranslate:
    #         with mock.patch('requests.get',self.mocked_requests_get_fun):
    #             fun_response = funtranslate(test_case[KEY_INPUT])
    #         expected = test_case[KEY_EXPECTED][KEY_RESPONSE]
    #         self.assertNotEqual(fun_response,expected)
            
    def mocked_random_int(self, a, b):
        return 1
    def test_coin_flip(self):
        for test_case in self.success_coin_flip_params:
            with mock.patch('bot_build.random.randint', self.mocked_random_int):
                coinflip_return=flipcoins()
        expected = test_case[KEY_EXPECTED]
        self.assertEqual(coinflip_return, expected)
            
if __name__ == '__main__':
    unittest.main()