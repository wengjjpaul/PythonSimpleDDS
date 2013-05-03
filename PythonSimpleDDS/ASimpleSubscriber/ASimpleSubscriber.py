import socket
import time
import xml.etree.ElementTree as ET
import Subscriber
import atexit
def onDataAvailableTopicOne(aData):
    print(aData)
def exit_handler():
    firstSubscriber.unSubscribe()



tree = ET.parse('DDSConfigFile.xml')
SubscriberHostIPV4 = tree.find("ServerInformation").find("SubscriberHostIPV4").text
SubscriberHostPort = int(tree.find("ServerInformation").find("SubscriberHostPort").text)

firstSubscriber = Subscriber.Subscriber(SubscriberHostIPV4, SubscriberHostPort)
firstSubscriber.subscribeTo("topicOne", onDataAvailableTopicOne)

atexit.register(exit_handler)
print(firstSubscriber.getTopic())

while 1:
    time.sleep(1)
    pass

print("End of program")

