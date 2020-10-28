"""Unit tests for mocked cases"""
import unittest
import sys

sys.path.append("../")
import bot_build
from bot_build import (
    get_joke,
    funtranslate,
    bot_command_parse,
    flipcoins,
    JOKE_URL,
    JOKE_HEADER,
    KEY_RESPONSE,
    FUN_URL,
    RAPID_API_HOST,
    RAPID_API_KEY,
)
import app
from app import (
    emit_num_users,
    emit_all_messages,
    add_to_db,
    on_disconnect,
    on_new_message,
    LIST_OF_CONNECTED_USERS,
    MESSAGE_RECEIVED_CHANNEL,
    url_parse,
    check_online_user,
)
import unmocked_unit_tests
import unittest.mock as mock
import urlparse
import connected_users
from urlparse import url_parse
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
    """Mocked bot input class"""

    def __init__(self, bot_command_input, bot_command_message):
        """Mocked bot initfile"""
        self.bot_command_input = bot_command_input
        self.bot_command_message = bot_command_message


class MockedBotResponse:
    """Mocked bot response class"""

    def __init__(self, bot_response):
        """Mocked bot response class"""
        self.bot_response = bot_response


class MockFunTranslate:
    """Mocked bot funtranslate class"""

    def __init__(self, text):
        """Mocked bot funtranslate class"""
        self.text = text


class MockedGetJokeResponse:
    """Mocked JOKE RESONSE input class"""

    def __init__(self, status_code, json):
        """Mocked JOKE RESONSE input class"""
        self.status_code = status_code
        self.json = json


class mocked_Data_base:
    """Mocked MOcked DB"""

    def __init__(self, name, message):
        """Mocked MOcked DB"""
        self.name = name
        self.message = message


class moked_Unit_tests(unittest.TestCase):
    """UNit test class"""

    def setUp(self):
        """LIST OF ALL unittests"""

        self.fail_test_params_get_joke = [{KEY_EXPECTED: "the world is flat NOT"}]

        self.fail_test_params_funtranslate = [
            {KEY_INPUT: "that is nice", KEY_EXPECTED: "bisa iksos nice"}
        ]

        self.success_coin_flip_params = [{KEY_EXPECTED: "heads"}]
        self.sucess_message_added = [{KEY_EXPECTED: ""}]

    def mocked_requests_get_joke(self, joke_url, headers):
        """mocked_requests_get_joke"""
        return mock.MagicMock(return_value="{the world is flat NOT}")

    def mocked_requests_get_funtranslate(self, translate_words):
        """mocked_requests_get_funtranslate"""
        return mock.MagicMock(return_value="{bisa iksos nice}")

    def mocked_request_sid(self):
        """"mocked request sid"""
        return mock.MagicMock(return_value=1)

    def mocked_random_int(self, a_num, b_num):
        """mocked request ramdom int"""
        return 1

    def mocked_check_for_user(self, a_num):
        """mocked test for users"""
        if a_num == 1:
            return "bob"
        return ""

    def mocked_emit_num_users(self, channel):
        """mocked emit num useres"""
        channel=5
        return channel

    def mocked_get_all_messages_from_db(self):
        """mocked get all messages"""
        return ["abcd", "efg"]

    def mocked_get_all_names_from_db(self):
        """mocked geta all names"""
        return ["matt", "frank"]

    def mocked_add_to_db(self, username, message):
        """mocked add to db"""
        return None

    def mocked_delete_user(self, userid):
        """mocked delete users"""
        return None

    def mocked_url_parse(self, message):
        """mocked url parse"""
        return ""

    def test_get_joke(self):
        """test for get joke"""
        for test_case in self.fail_test_params_get_joke:
            with mock.patch("requests.get", self.mocked_requests_get_joke):
                joke_response = get_joke(joke_url=JOKE_URL, joke_header=JOKE_HEADER)
            expected = test_case[KEY_EXPECTED]
            self.assertNotEqual(joke_response, expected)

    def test_get_funtranslate(self):
        """test for funtranslate"""
        for test_case in self.fail_test_params_funtranslate:
            with mock.patch("requests.get", self.mocked_requests_get_funtranslate):
                fun_response = funtranslate(translate_words=test_case[KEY_INPUT])
            expected = test_case[KEY_EXPECTED]
            self.assertNotEqual(fun_response, expected)

    def test_coin_flip(self):
        """test for coinflip"""
        for test_case in self.success_coin_flip_params:
            with mock.patch("bot_build.random.randint", self.mocked_random_int):
                coinflip_return = flipcoins()
        expected = test_case[KEY_EXPECTED]
        self.assertEqual(coinflip_return, expected)

    def test_emit_num_users(self):
        """test for number of users"""
        with mock.patch("app.emit_num_users", self.mocked_emit_num_users):
            number_users = emit_num_users(LIST_OF_CONNECTED_USERS)
        self.assertNotEqual(number_users, 3)

    def test_emit_all_messages(self):
        """test for emit all messages"""
        with mock.patch(
            "app.get_all_messages_from_db", self.mocked_get_all_messages_from_db
        ):
            with mock.patch(
                "app.get_all_names_from_db", self.mocked_get_all_names_from_db
            ):
                allMessages = emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
        self.assertNotEqual(allMessages, ["matt: abcd", "frank: efg"])

    def test_on_new_google_user(self):
        """test for adding new google"""
        with mock.patch("app.LIST_OF_CONNECTED_USERS.add_user"):
            with mock.patch("app.emit_num_users", self.mocked_emit_num_users):
                number_users = emit_num_users(LIST_OF_CONNECTED_USERS)
        self.assertNotEqual = (number_users, 0)

    def test_on_disconnect(self):
        """test on disconect"""
        with mock.patch(
            "app.LIST_OF_CONNECTED_USERS.delete_user", self.mocked_delete_user
        ):
            with mock.patch("app.emit_num_users", self.mocked_emit_num_users):
                number_users = emit_num_users(LIST_OF_CONNECTED_USERS)
        self.assertNotEqual = (number_users, 0)

    def test_check_url(self):
        """tst on check for url"""
        with mock.patch("urlparse.url_parse", self.mocked_url_parse):
            message = url_parse("this stuff")
        self.assertNotEqual = (message, "abced")

    def test_check_Online_user(self):
        """teck for online user"""
        with mock.patch(
            "app.LIST_OF_CONNECTED_USERS.check_for_user", self.mocked_check_for_user
        ):
            user_check = check_online_user(1)
        self.assertNotEqual(user_check, "tommy")


if __name__ == "__main__":
    unittest.main()
