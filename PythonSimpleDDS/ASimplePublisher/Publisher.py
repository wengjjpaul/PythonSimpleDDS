class Publisher:
    def __init__(self, aPublisherServiceIPV4, aPublisherServicePort):
        self.mPublisherServiceIPV4 = aPublisherServiceIPV4
        self.mPublisherServicePort = aPublisherServicePort
        self.mTopic = None
    def setTopic(self, aTopic):
        self.mTopic = aTopic
    def publishOnce(self, aData):
        if(self.mTopic = None):
            return False
        else:
            mServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tMESSAGE = "publish," + self.mTopic + ", " + aData
            tMessageInBytes = bytes(tMESSAGE, 'UTF-8')
            mServer.sendto(tMessageInBytes, (self.mPublisherServiceIPV4, self.mPublisherServicePort))
            return True
    def getTopic(self):
        return self.mTopic
