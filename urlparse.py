'''parse the file to see if there is any url or picture in it'''
from rfc3987 import parse


def url_parse(usermessage):
    '''pars the message to see if any url or pic is in it'''
    messageList = usermessage.split()
    picimages = ["jpg", "png", "gif"]
    rtnMessage = ""
    for message in messageList:
        try:
            parsedinfo = parse(message, rule="IRI")
            print(parsedinfo.get("scheme"))
            urlpic = parsedinfo.get("path")
            if any(pic in urlpic for pic in picimages):
                picRtn = "<imgsrc="
                picRtn += message
                rtnMessage += picRtn
                rtnMessage += " "
            else:
                atag = "<ahref="
                atag += message
                rtnMessage += atag
                rtnMessage += " "
        except:
            rtnMessage += message
            rtnMessage += " "
    return rtnMessage
