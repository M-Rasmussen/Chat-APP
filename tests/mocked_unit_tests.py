import unittest
import sys
sys.path.append("../")
import bot_build
import app
from bot_build import get_joke, funtranslate, bot_command_parse, flipcoins
from bot_build import JOKE_URL, JOKE_HEADER, KEY_RESPONSE, FUN_URL
from app import emit_num_users, emit_all_messages,add_to_db, on_disconnect
from app import LIST_OF_CONNECTED_USERS, MESSAGE_RECEIVED_CHANNEL
# from bot_build import MESSAGE_TO_RETURN, KEY_RESPONSE
from bot_build import RAPID_API_HOST, RAPID_API_KEY
import unmocked_unit_tests
import unittest.mock as mock
from unittest.mock import MagicMock
from dotenv import load_dotenv
import requests
import os
import json
from os.path import join, dirname
import connected_users
LIST_OF_CONNECTED_USERS = connected_users.Connected()
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
        self.text = text


class MockedGetJokeResponse:
    def __init__(self, status_code, json):
        self.status_code = status_code
        self.json = json
class mocked_Data_base:
    def __init__(self, name, message):
        self.name = name
        self.message= message


class moked_Unit_tests(unittest.TestCase):
    
    def setUp(self):
        self.fail_test_params_get_joke = [
            {KEY_EXPECTED: "the world is flat NOT"}
        ]

        self.fail_test_params_funtranslate = [
            { 
                KEY_INPUT:"that is nice",
                KEY_EXPECTED: "bisa iksos nice"}
        ]

        self.success_coin_flip_params = [{KEY_EXPECTED: "heads"}]
        self.sucess_message_added=[{KEY_EXPECTED: ""}]

    def mocked_requests_get_joke(self, joke_url, headers):
        return mock.MagicMock(return_value="{the world is flat NOT}")
    def mocked_requests_get_funtranslate(self, translate_words):
        return mock.MagicMock(return_value="{bisa iksos nice}")
        
    def mocked_request_sid(self):
        return mock.MagicMock(return_value=1)
    
    def mocked_random_int(self, a, b):
        return 1
        
    def mocked_check_for_user(self, a):
        if a == 1:
            return "bob"
        else:
            return ""

    def mocked_emit_num_users(self, channel):
        return 5
        
    def mocked_get_all_messages_from_db(self):
        return ['abcd', 'efg']
    
    def mocked_get_all_names_from_db(self):
        return ['matt','frank']
    def mocked_add_to_db(self, username, message):
        return None
    def mocked_delete_user(self,userid):
        return None
    
    def test_get_joke(self):
        for test_case in self.fail_test_params_get_joke:
            with mock.patch("requests.get", self.mocked_requests_get_joke):
                joke_response = get_joke(joke_url=JOKE_URL, joke_header=JOKE_HEADER)
            expected = test_case[KEY_EXPECTED]
            self.assertNotEqual(joke_response, expected)

    def test_get_funtranslate(self):
         for test_case in self.fail_test_params_funtranslate:
            with mock.patch('requests.get',self.mocked_requests_get_funtranslate):
                 fun_response = funtranslate(
                     translate_words = test_case[KEY_INPUT]
                     )
            expected= test_case[KEY_EXPECTED]
            self.assertNotEqual(fun_response, expected)

    def test_coin_flip(self):
        for test_case in self.success_coin_flip_params:
            with mock.patch("bot_build.random.randint", self.mocked_random_int):
                coinflip_return = flipcoins()
        expected = test_case[KEY_EXPECTED]
        self.assertEqual(coinflip_return, expected)
    
    def test_emit_num_users(self):
        with mock.patch("app.emit_num_users",self.mocked_emit_num_users):
            number_users= emit_num_users(LIST_OF_CONNECTED_USERS)
        self.assertNotEqual(number_users, 3)
    
    def test_emit_all_messages(self):
        with mock.patch('app.get_all_messages_from_db',self.mocked_get_all_messages_from_db):
            with mock.patch('app.get_all_names_from_db',self.mocked_get_all_names_from_db):
                allMessages=emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
        self.assertNotEqual(allMessages, ['matt: abcd', 'frank: efg'])
    
    def test_on_new_google_user(self):
        with mock.patch('app.LIST_OF_CONNECTED_USERS.add_user'):
            with mock.patch("app.emit_num_users",self.mocked_emit_num_users):
                number_users= emit_num_users(LIST_OF_CONNECTED_USERS)
        self.assertNotEqual= (number_users, 0)
    def test_on_disconnect(self):
        with mock.patch("app.LIST_OF_CONNECTED_USERS.delete_user", self.mocked_delete_user):
            with mock.patch("app.emit_num_users",self.mocked_emit_num_users):
                number_users= emit_num_users(LIST_OF_CONNECTED_USERS)
        self.assertNotEqual= (number_users, 0)

if __name__ == "__main__":
    unittest.main()
