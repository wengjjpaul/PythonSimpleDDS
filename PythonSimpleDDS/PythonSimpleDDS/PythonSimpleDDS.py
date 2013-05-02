import PyPubSub
import xml.etree.ElementTree as ET
import threading

def subscriberService(service):
    service.hostSubscribeService()

tree = ET.parse('DDSConfigFile.xml')
tree = tree.find("ServerInformation").find("ServerIPV4")
print(tree.text)

SubscriberHostIPV4 = ''
SubscriberHostPort = 5555
PublisherHostIPV4 = ''
PublisherHostPort = 5556

PubSubService = PyPubSub.PyPubSub(SubscriberHostIPV4, SubscriberHostPort, PublisherHostIPV4, PublisherHostPort)
PubSubService.startSubscriberHostService()
PubSubService.startPublisherHostService()

while 1:
    pass

print("End of Code")

