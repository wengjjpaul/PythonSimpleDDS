import socket

class SubscribeService:
    def __init__(self, aDDSFilter):
        self.mServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = ''
        self.port = 5555
        #need a better method to do this
        self.mDDSFilter = aDDSFilter

    def testFilter(self, what):
        self.mDDSFilterList[0].getSubscribers(what)
    def hostSubscribeService(self):
        self.mServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mServer.bind((host, port))
        self.startListening()
    def startListening(self):
        message, address = self.mServer.recvfrom(8192)
        messageSendFromClient = message.decode("utf-8")
        messageParts = messageSendFromClient.split(',')
        if(messageParts):
            if(messageParts[0] == "Subscribe"):
                if(messageParts[1]):
                    pass
