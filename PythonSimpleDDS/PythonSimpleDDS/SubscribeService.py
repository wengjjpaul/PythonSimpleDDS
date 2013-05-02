import socket

class SubscribeService:
    def __init__(self, aDDSFilter, aHostIPV4, aHostPort):
        self.mServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = aHostIPV4
        self.port = aHostPort
        self.mDDSFilter = aDDSFilter
    def testFilter(self, what):
        print(self.mDDSFilter.getSubscribers(what))
    def hostSubscribeService(self):
        self.mServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mServer.bind((self.host, self.port))
        self.startListening()
    def startListening(self):
        while 1:
            message, address = self.mServer.recvfrom(8192)
            messageSendFromClient = message.decode("utf-8")
            messageParts = messageSendFromClient.split(',')
            stripedMessageParts =  [item.strip() for item in messageParts]
            if(stripedMessageParts):
                if(stripedMessageParts[0] == "subscribe"):
                    if(stripedMessageParts[1]):                                                
                        self.mDDSFilter.addSubscriber(stripedMessageParts[1], address)
                elif(stripedMessageParts[0] == "unsubscribe"):
                    if(stripedMessageParts[1]):
                        self.mDDSFilter.removeSubscriber(stripedMessageParts[1], address)
                else:
                    pass
