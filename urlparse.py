"""parse the file to see if there is any url or picture in it"""
from rfc3987 import parse


def url_parse(usermessage):
    '''pars the message to see if any url or pic is in it'''
    message_list = usermessage.split()
    picimages = ["jpg", "png", "gif"]
    rtn_message = ""
    for message in message_list:
        try:
            parsedinfo = parse(message, rule="IRI")
            print(parsedinfo.get("scheme"))
            urlpic = parsedinfo.get("path")
            if any(pic in urlpic for pic in picimages):
                pic_rtn = "<imgsrc="
                pic_rtn += message
                rtn_message += pic_rtn
                rtn_message += " "
            else:
                atag = "<ahref="
                atag += message
                rtn_message += atag
                rtn_message += " "
        except:
            rtn_message += message
            rtn_message += " "
    return rtn_message
