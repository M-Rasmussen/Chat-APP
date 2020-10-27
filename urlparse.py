from rfc3987 import parse

    
def url_parse(usermessage):
    messageList=usermessage.split()
    picimages=["jpg","png","gif"]
    rtnMessage=''
    for message in messageList:
        try:
            parsedinfo=parse(message,rule='IRI')
            print(parsedinfo.get('scheme'))
            urlpic=parsedinfo.get('path')
            if (any(pic in urlpic for pic in picimages)):
                picRtn='<imgsrc='
                picRtn+=message
                rtnMessage+=picRtn
                rtnMessage+=" "
            else:
                atag='<ahref='
                atag+=message
                rtnMessage+=atag
                rtnMessage+=" "
        except:
            rtnMessage+=message
            rtnMessage+= " "
    return rtnMessage
            