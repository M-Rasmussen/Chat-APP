import unittest
import sys
sys.path.append('../')
import botMessage as validMessage
from botMessage import KEY_IS_BOT, KEY_BOT_COMMAND, KEY_MESSAGE


KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_LENGTH = "length"
KEY_FIRST_WORD = "first_word"
KEY_SECOND_WORD = "second_word"

class BotbuildTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
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
            },
            {
                KEY_INPUT: "!! help",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: "help",
                    KEY_MESSAGE: "",
                }
            },
            {
                KEY_INPUT: "!!funtranslate abced",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: "funtranslate",
                    KEY_MESSAGE: "abced",
                }
            },
            {
                KEY_INPUT: "!!joke",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: "joke",
                    KEY_MESSAGE: "",
                }
            }
        ]
        
        self.failure_test_params = [
                        {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: "help",
                    KEY_MESSAGE: "",
                }
            },
            {
                KEY_INPUT: "!about me",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: None,
                    KEY_MESSAGE: "!about me",
                }
            },
            {
                KEY_INPUT: "!!HELP",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: "help",
                    KEY_MESSAGE: "abe",
                }
            },
            {
                KEY_INPUT: "!!funtranslate abced",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: "funtranslate",
                    KEY_MESSAGE: "",
                }
            },
            {
                KEY_INPUT: "!!joke",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: "joke",
                    KEY_MESSAGE: "",
                }
            }
        ]


    def test_parse_message_success(self):
        for test in self.success_test_params:
            response = validMessage.validMessage(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response[KEY_IS_BOT], expected[KEY_IS_BOT])
            self.assertEqual(response[KEY_BOT_COMMAND], expected[KEY_BOT_COMMAND])
            self.assertEqual(response[KEY_MESSAGE], expected[KEY_MESSAGE])
            
    # def test_parse_message_failure(self):
    #     for test in self.failure_test_params:
    #         response = validMessage.validMessage(test[KEY_INPUT])
    #         expected = test[KEY_EXPECTED]
            
    #         self.assertNotEqual(response[KEY_IS_BOT], expected[KEY_IS_BOT])
    #         self.assertNotEqual(response[KEY_BOT_COMMAND], expected[KEY_BOT_COMMAND])
    #         self.assertNotEqual(response[KEY_MESSAGE], expected[KEY_MESSAGE])


if __name__ == '__main__':
    unittest.main()