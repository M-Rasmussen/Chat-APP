class Connected:
    def __init__(self):
        self.CONNECTED_LIST = []
    def addUser(self, USER_ID, USER_NAME):
        self.CONNECTED_LIST.append({'USER_ID': USER_ID, 'USER_NAME': USER_NAME })
    def deleteUser(self, USER_ID):
        for USER_LIST in range(len(self.CONNECTED_LIST)):
            if self.CONNECTED_LIST[USER_LIST]['USER_ID'] == USER_ID:
                del self.CONNECTED_LIST[USER_LIST]
                break
    def numberOfUsers(self):
        return len(self.CONNECTED_LIST)
    def checkForUser(self, USER_ID):
        for USER_LIST in range(len(self.CONNECTED_LIST)):
            if self.CONNECTED_LIST[USER_LIST]['USER_ID'] == USER_ID:
                USER_NAME=self.CONNECTED_LIST[USER_LIST]['USER_NAME']
                return USER_NAME
        return ""
        