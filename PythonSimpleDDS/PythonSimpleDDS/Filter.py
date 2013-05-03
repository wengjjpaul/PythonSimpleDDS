class Filter:
    def __init__(self):
        self.mSubscribersList = dict()
    def getSubscribers(self, aTopicName):
        if(aTopicName in self.mSubscribersList):
            return self.mSubscribersList[aTopicName]
    def addSubscriber(self, aTopicName, aSubscriberEndPoint):
        if(aTopicName in self.mSubscribersList):
            if(not(aSubscriberEndPoint in self.mSubscribersList[aTopicName])):
                #add the new subscriber to the front of the list
                self.mSubscribersList[aTopicName].append(aSubscriberEndPoint)
        else:
            #add a new topic to subscriber list with the new subscriber end point
            self.mSubscribersList[aTopicName] =[aSubscriberEndPoint]
    def removeSubscriber(self, aTopicName, aSubscriberEndPoint):
        if(aTopicName in self.mSubscribersList):
            if(aSubscriberEndPoint in self.mSubscribersList[aTopicName]):
                #remove the subscriber from the list
                self.mSubscribersList[aTopicName].remove(aSubscriberEndPoint)
