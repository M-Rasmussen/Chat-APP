import unittest
import sys
sys.path.append("../")
import bot_build
from bot_build import get_joke, funtranslate, bot_command_parse, flipcoins
from bot_build import JOKE_URL, JOKE_HEADER, KEY_RESPONSE, FUN_URL

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


class moked_Unit_tests(unittest.TestCase):
    def setUp(self):
        self.fail_test_params_get_joke = [
            {KEY_EXPECTED: {KEY_RESPONSE: "the world is flat NOT"}}
        ]

        self.fail_test_params_funtranslate = [
            {KEY_INPUT: "this is nice", KEY_EXPECTED: {KEY_RESPONSE: "bisa iksos nice"}}
        ]

        self.success_coin_flip_params = [{KEY_EXPECTED: "heads"}]

    def mocked_requests_get(self, joke_url, headers):
        return mock.MagicMock()


    def test_get_joke(self):
        for test_case in self.fail_test_params_get_joke:
            with mock.patch("requests.get", self.mocked_requests_get):
                joke_response = get_joke(joke_url=JOKE_URL, joke_header=JOKE_HEADER)
            expected = test_case[KEY_EXPECTED]
            self.assertNotEqual(joke_response, expected)

    # def test_get_funtranslate(self):
    #     for test_case in self.fail_test_params_funtranslate:
    #         with mock.patch('requests.get',self.mocked_requests_get):
    #             fun_response = funtranslate(test_case[KEY_INPUT],FUN_URL)
    #         expected = test_case[KEY_EXPECTED][KEY_RESPONSE]
    #         self.assertNotEqual(fun_response,expected)

    def mocked_random_int(self, a, b):
        return 1

    def test_coin_flip(self):
        for test_case in self.success_coin_flip_params:
            with mock.patch("bot_build.random.randint", self.mocked_random_int):
                coinflip_return = flipcoins()
        expected = test_case[KEY_EXPECTED]
        self.assertEqual(coinflip_return, expected)


    @mock.patch('app.flask')
    def test_print_request_side(self, mock_flask):
        mock_flask.request.sid = 'mock_sid'
        result= app.print_request_sid()
        self.assertEqual(result,'mock_sid')
    # def mocked_check_for_user(self):      

    #     LIST_OF_CONNECTED_USERS.add_user(1234, "name")
    #     user_name=LIST_OF_CONNECTED_USERS.check_for_user(1234)
    #     self.assertEqual(user_name,"name")
    # def mocked_delete_user(self):
    #     self.assertIsNone(LIST_OF_CONNECTED_USERS.delete_user(1234)


if __name__ == "__main__":
    unittest.main()
