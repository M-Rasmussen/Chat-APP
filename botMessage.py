BOT_PREFIX = "!!"
KEY_IS_BOT = "is_bot"
KEY_BOT_COMMAND = "bot_command"
KEY_MESSAGE = "message"
def validMessage(message):
    if not message.startswith(BOT_PREFIX):
        return{
            KEY_IS_BOT: False,
            KEY_BOT_COMMAND: None,
            KEY_MESSAGE: message
    }
    message = message[2:]
    message = message.strip()
    message_components = message.split(" ",1)
    if len(message_components) == 1:
        possible_bot_cmd, rest_of_message = message_components[0],""
    else:
        possible_bot_cmd, rest_of_message = message_components[0], message_components[1]
        
    return{
        KEY_IS_BOT: True,
        KEY_BOT_COMMAND: possible_bot_cmd,
        KEY_MESSAGE: rest_of_message
    }