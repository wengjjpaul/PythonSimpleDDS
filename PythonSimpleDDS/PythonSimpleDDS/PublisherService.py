import socket
import threading
class PublisherService:
    def __init__(self, aDDSFilter, aHostIPV4, aHostPort):
        self.mServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = aHostIPV4
        self.port = aHostPort
        self.mDDSFilter = aDDSFilter
    def HostPublisherService(self):
        #Setup listening socket to hear from publishers
        self.mServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mServer.bind((self.host, self.port))
        self._startListening()
    def _startListening(self):
        while 1:
            #Incoming messages stored in message
            message, address = self.mServer.recvfrom(8192)
            messageSendFromClient = message.decode("utf-8")
            messageParts = messageSendFromClient.split(',')
            tCommand = messageParts[0].strip()
            tTopic = messageParts[1].strip()
            if(tCommand):
                if(tCommand == "publish"):
                    if(tTopic):
                        #remove command and topic segment from message array
                        messageParts = messageParts[2:]
                        #Make a comma separated string from list
                        messageToSend = ",".join(messageParts)
                        #Clean up the message little
                        messageToSend.strip()
                        #Get subscriber list for current topic
                        tSubscriberListForThisTopic = self.mDDSFilter.getSubscribers(tTopic)
                        #Begin thread to publish to all subscribers
                        t = threading.Thread(target=_publish, args = (self.mServer, messageToSend, tSubscriberListForThisTopic))
                        #wont keep the thread up if main thread die
                        t.daemon = True
                        try:
                            t.start()
                        except: #catch all errors
                            pass
                else:
                    pass
    def _publish(self, aServer, aMessage, aSubscriberList):
        #Convert String message into bytes
        tMessageInBytes = bytes(aMessage, 'UTF-8')
        #Check if there are any subscribers
        if(aSubscriberList):
            for tSubscriber in aSubscriberList:
                #Send out the message using UDP using listening socket
                aServer.sendto(tMessageInBytes, tSubscriber)
