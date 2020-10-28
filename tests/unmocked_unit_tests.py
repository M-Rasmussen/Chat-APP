"""Unmocked unittesting"""
import unittest
import sys

sys.path.append("../")
import bot_message as valid_message
from bot_message import KEY_IS_BOT, KEY_BOT_COMMAND, KEY_MESSAGE
import urlparse as url_parse
import bot_build as bot_command_parse
import connected_users

LIST_OF_CONNECTED_USERS = connected_users.Connected()

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_LENGTH = "length"
KEY_FIRST_WORD = "first_word"
KEY_SECOND_WORD = "second_word"
BOT_COMMAND_INPUT = "input"
BOT_COMMAND_MESSAGE = ""


class BotbuildTestCase(unittest.TestCase):
    """Unit Testing for all fo the cases unmocked"""

    def setUp(self):
        """List of all testing paramaters"""
        self.success_test_params_bot_message = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: "help",
                    KEY_MESSAGE: "",
                },
            },
            {
                KEY_INPUT: "!!about",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: "about",
                    KEY_MESSAGE: "",
                },
            },
        ]

        self.failure_test_params_bot_message = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: "hel",
                    KEY_MESSAGE: "a",
                },
            },
            {
                KEY_INPUT: "!!about me",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: "about",
                    KEY_MESSAGE: "me",
                },
            },
        ]
        self.check_url_success = [
            {
                KEY_INPUT: "https://www.google.com/",
                KEY_EXPECTED: "<ahref=https://www.google.com/ ",
            }
        ]
        self.check_url_fail = [
            {
                KEY_INPUT: "https://gutsytechster.files.wordpress.com/2019/05/see-you-soon\
                -jenna-bell.png?w=810&h=1&crop=1 dadf",
                KEY_EXPECTED: "<img[42 chars]com/2019/05/see-you-soon-jenna-bell.png?w=810&h\
                =1&crop=1 dadf",
            }
        ]
        self.correct_bot_command_sucess = [
            {
                KEY_INPUT: {BOT_COMMAND_INPUT: "about", BOT_COMMAND_MESSAGE: ""},
                KEY_EXPECTED: "I tell jokes, flip coins, and translate your language \
            into high valyrian. Just put !! infront of the commands and I will \
            return as you please. For more information enter !!help",
            },
            {
                KEY_INPUT: {BOT_COMMAND_INPUT: "help", BOT_COMMAND_MESSAGE: ""},
                KEY_EXPECTED: "!! about and I will tell you about me. !! funtranslate \
            (words), will translate anything after that into high valyrian. \
            !! joke and I will tell you a joke. !! coin flip will result me \
            in flipping a coin and I will tell you the results. ",
            },
        ]
        self.correct_bot_command_fail = [
            {
                KEY_INPUT: {BOT_COMMAND_INPUT: "about", BOT_COMMAND_MESSAGE: ""},
                KEY_EXPECTED: "",
            }
        ]
        self.test_app_concat_pass = [
            {
                KEY_INPUT: ["abcd", "message", "message2"],
                KEY_SECOND_WORD: ["matt", "dough", "frank"],
                KEY_EXPECTED: ["matt: abcd", "dough: message", "frank: message2"],
            }
        ]
        self.test_app_concat_failed = [
            {
                KEY_INPUT: ['abcd' , 'message', 'message2'],
                KEY_SECOND_WORD: ['matt' , 'dough', 'frank'],
                KEY_EXPECTED:['matt: abcd', 'frank: message2']
                }
            ]
        self.test_fun_translate_concat = [
            {
                KEY_INPUT: "http://api.funtranslations.com/translate/valyrian?text=",
                KEY_EXPECTED:"http://api.funtranslations.com/translate/valyrian?text=This is nice"
                }
            ]

    def test_parse_message_success(self):
        """Test if function valid_message is correct with correct input"""
        for test in self.success_test_params_bot_message:
            response = valid_message.valid_message(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertDictEqual(response, expected)

    def test_parse_message_failure(self):
        """Test if function valid_message is incorrect with incorrect input"""
        for test in self.failure_test_params_bot_message:
            response = valid_message.valid_message(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertNotEqual(response[KEY_IS_BOT], expected[KEY_IS_BOT])

    def test_check_url_success(self):
        """Test if funciton url_parse is used correctly for correct imports"""
        for test in self.check_url_success:
            response = url_parse.url_parse(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertEqual(response, expected)

    def test_check_url_fail(self):
        """Test if funciton url_parse is used incorrectly for incorrect imports"""
        for test in self.check_url_fail:
            response = url_parse.url_parse(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertNotEqual(response, expected)

    def test_bot_command(self):
        """Test if funciton bot_command_parse is used correctly for correct imports"""
        for test in self.correct_bot_command_sucess:
            response = bot_command_parse.bot_command_parse(
                test[KEY_INPUT][BOT_COMMAND_INPUT], test[KEY_INPUT][BOT_COMMAND_MESSAGE]
            )
            expected = test[KEY_EXPECTED]
            self.assertEqual(response, expected)

    def test_bot_command_fail(self):
        """Test if funciton bot_command_parse is used incorrectly for incorrect imports"""
        for test in self.correct_bot_command_fail:
            response = bot_command_parse.bot_command_parse(
                test[KEY_INPUT][BOT_COMMAND_INPUT], test[KEY_INPUT][BOT_COMMAND_MESSAGE]
            )
            expected = test[KEY_EXPECTED]
            self.assertNotEqual(response, expected)

    def test_app_concat(self):
        """Test if funciton concat_message is used correctly for correct imports"""
        for test in self.test_app_concat_pass:
            response = bot_command_parse.concat_messages(
                test[KEY_INPUT], test[KEY_SECOND_WORD]
            )
            expected = test[KEY_EXPECTED]
            self.assertEqual(response, expected)

    def test_app_concat_fail(self):
        """Test if funciton concat_message is used incorrectly for incorrect imports"""
        for test in self.test_app_concat_failed:
            response = bot_command_parse.concat_messages(
                test[KEY_INPUT], test[KEY_SECOND_WORD]
            )
            expected = test[KEY_EXPECTED]
            self.assertNotEqual(response, expected)

    def test_num_users(self):
        """Test the nubmer of users"""
        response = LIST_OF_CONNECTED_USERS.number_of_users()
        expected = 0
        self.assertEqual(response, expected)

    def test_num_users_added(self):
        """test the number of users after adding one"""
        LIST_OF_CONNECTED_USERS.add_user(1234, "name")
        response = LIST_OF_CONNECTED_USERS.number_of_users()
        expected = 1
        self.assertEqual(response,expected)
    
    def fun_translate_concat(self):
        '''Test if funciton concat funtranslate'''
        for test in self.test_fun_translate_concat:
            response = bot_command_parse.fun_translate_concat(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertEqual(response,expected)


if __name__ == "__main__":
    unittest.main()
