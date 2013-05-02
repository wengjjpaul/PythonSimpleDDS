import socket
import time
import Subscriber
import xml.etree.ElementTree as ET

def onDataAvailableTopicOne(aData):
    print(aData)

tree = ET.parse('DDSConfigFile.xml')
SubscriberHostIPV4 = tree.find("ServerInformation").find("SubscriberHostIPV4").text
SubscriberHostPort = int(tree.find("ServerInformation").find("SubscriberHostPort").text)

firstSubscriber = Subscriber.Subscriber(SubscriberHostIPV4, SubscriberHostPort)
firstSubscriber.subscribeTo("topicOne", onDataAvailableTopicOne)
print(firstSubscriber.getTopic)

while 1:
    pass

print("End of program")
