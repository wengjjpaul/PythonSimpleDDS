import socket

class SubscribeService:
    def __init__(self, aDDSFilter, aHostIPV4, aHostPort):
        #Create a listening socket for SubscribeService
        self.mServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = aHostIPV4
        self.port = aHostPort
        self.mDDSFilter = aDDSFilter
    #Debug function
    def _testFilter(self, what):
        print(self.mDDSFilter.getSubscribers(what))
    def hostSubscribeService(self):
        self.mServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #Bind to a single port for listening
        self.mServer.bind((self.host, self.port))
        self._startListening()
    def _startListening(self):
        while 1:
            #Incoming message stored in message
            message, address = self.mServer.recvfrom(8192)
            messageSendFromClient = message.decode("utf-8")
            messageParts = messageSendFromClient.split(',')
            #Clean up the message
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
