import PyPubSub
import xml.etree.ElementTree as ET
import threading
import time
def subscriberService(service):
    service.hostSubscribeService()

tree = ET.parse('DDSConfigFile.xml')
SubscriberHostIPV4 = tree.find("ServerInformation").find("SubscriberHostIPV4").text
SubscriberHostPort = int(tree.find("ServerInformation").find("SubscriberHostPort").text)
PublisherHostIPV4 = tree.find("ServerInformation").find("PublisherHostIPV4").text
PublisherHostPort = int(tree.find("ServerInformation").find("PublisherHostPort").text)

PubSubService = PyPubSub.PyPubSub(SubscriberHostIPV4, SubscriberHostPort, PublisherHostIPV4, PublisherHostPort)
PubSubService.startSubscriberHostService()
PubSubService.startPublisherHostService()

while 1:
    time.sleep(1)
    print(PubSubService.mMainFilter.getSubscribers("topicOne"))

print("End of Code")

