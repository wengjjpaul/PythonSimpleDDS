import socket
import threading
class Subscriber:
    def __init__(self, aSubscriberServiceIPV4, aSubscriberServicePort):
        self.mSubscriberServiceIPV4 = aSubscriberServiceIPV4
        self.mSubscriberServicePort = aSubscriberServicePort
        self.mFunction = None
        self.mSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.mListeningPort = self.mSock.getsockname()[1]
        self.mAlreadySubscribed = False
        self.mThread = threading.Thread(target=_SubscribedThreadFunction, args = (,))
        self.mListeningSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.mTopic = None
    def subscribeTo(self, aTopic, aFunctionBindTo):
        """FunctionBindTo require a parameter to accept incoming data"""
        if(self.mAlreadySubscribed == False):
            self.mFunction = aFunctionBindTo
            self.mTopic = aTopic
            
            tMESSAGE = "subscribe" + aTopic
            tMessageInBytes = bytes(tMESSAGE, 'UTF-8')
            self.mSock.sendto(tMessageInBytes, (self.mSubscriberServiceIPV4, self.mSubscriberServicePort))
            self.mAlreadySubscribed = True
            
            self.mListeningSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.mListeningSocket.bind(('', self.mListeningPort))
            #wont keep the thread up if main thread die
            self.mThread.daemon = True
            try:
                self.mThread.start()
            except: #catch all errors
                pass
            return True
        else:
            return False
    def _SubscribedThreadFunction(self):
        while 1:
            message, address = self.mListeningSocket.recvfrom(8192)
            messageSendFromService = message.decode("utf-8")
            self.mFunction(messageSendFromService)
    def unSubscribe(self):
        if(self.mAlreadySubscribed == True):
            if self.mThread.isAlive():
                try:
                    self.mThread._stop()
                    self.mAlreadySubscribed = False
                    self.mFunction = None
                    self.mTopic = None
                except:
                    pass
            return True
        else:
            return False
    def getTopic(self):
        return self.mTopic
