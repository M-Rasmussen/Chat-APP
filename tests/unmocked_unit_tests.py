import unittest
import sys
sys.path.append('../')
import bot_message as valid_message
from bot_message import KEY_IS_BOT, KEY_BOT_COMMAND, KEY_MESSAGE
import urlparse as url_parse

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_LENGTH = "length"
KEY_FIRST_WORD = "first_word"
KEY_SECOND_WORD = "second_word"

class BotbuildTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params_bot_message = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: "help",
                    KEY_MESSAGE: "",
                }
            },
            {
                KEY_INPUT: "!about me",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: None,
                    KEY_MESSAGE: "!about me",
                }
            }
        ]
        
        self.failure_test_params_bot_message = [
                        {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: "hel",
                    KEY_MESSAGE: "a",
                }
            },
            {
                KEY_INPUT: "!!about me",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: "about",
                    KEY_MESSAGE: "me",
                }
            },
        ]
        self.check_url_success = [
            {
                KEY_INPUT: "https://www.google.com/",
                KEY_EXPECTED:"<ahref=https://www.google.com/ "
                }
            ]
        self.check_url_fail = [
            {
                KEY_INPUT: "https://gutsytechster.files.wordpress.com/2019/05/see-you-soon-jenna-bell.png?w=810&h=1&crop=1 dadf",
                KEY_EXPECTED:"<img[42 chars]com/2019/05/see-you-soon-jenna-bell.png?w=810&h=1&crop=1 dadf"
                }
        ]
    def test_parse_message_success(self):
        for test in self.success_test_params_bot_message:
            response = valid_message.valid_message(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertDictEqual(response,expected)
            
    def test_parse_message_failure(self):
        for test in self.failure_test_params_bot_message:
            response = valid_message.valid_message(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]

            self.assertNotEqual(response[KEY_IS_BOT], expected[KEY_IS_BOT])

    def test_checkURl_success(self):
        for test in self.check_url_success:
            response= url_parse.url_parse(test[KEY_INPUT])
            expected= test[KEY_EXPECTED]
            self.assertEqual(response,expected)
    def test_checkURl_fail(self):
        for test in self.check_url_fail:
            response= url_parse.url_parse(test[KEY_INPUT])
            expected= test[KEY_EXPECTED]
            self.assertNotEqual(response,expected)
            
    
            
            
            
if __name__ == '__main__':
    unittest.main()