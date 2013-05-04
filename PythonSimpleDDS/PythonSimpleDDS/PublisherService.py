import socket
import threading
class PublisherService:
    def __init__(self, aDDSFilter, aHostIPV4, aHostPort):
        self.mServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = aHostIPV4
        self.port = aHostPort
        self.mDDSFilter = aDDSFilter
    def HostPublisherService(self):
        self.mServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mServer.bind(('', self.port))
        self._startListening()
    def _startListening(self):
        while 1:
            message, address = self.mServer.recvfrom(8192)
            messageSendFromClient = message.decode("utf-8")
            messageParts = messageSendFromClient.split(',')
            tCommand = messageParts[0].strip()
            tTopic = messageParts[1].strip()
            if(tCommand):
                if(tCommand == "publish"):
                    if(tTopic):
                        #remove command and topic from message
                        messageParts = messageParts[2:]
                        #Make a comma separated string from list
                        messageToSend = ",".join(messageParts)
                        stripedMessage = messageToSend.strip()
                        tSubscriberListForThisTopic = self.mDDSFilter.getSubscribers(tTopic)
                        t = threading.Thread(target=self._publish, args = (self.mServer, stripedMessage, tSubscriberListForThisTopic))
                        #wont keep the thread up if main thread die
                        t.daemon = True
                        try:
                            t.start()
                        except: #catch all errors
                            pass
                else:
                    pass
    def _publish(self, aServer, aMessage, aSubscriberList):
        tMessageInBytes = bytes(aMessage, 'UTF-8')
        if(aSubscriberList):
            for tSubscriber in aSubscriberList:
                aServer.sendto(tMessageInBytes, tSubscriber)
