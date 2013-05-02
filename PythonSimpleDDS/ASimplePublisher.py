import socket
import time
import Subscriber
import xml.etree.ElementTree as ET

tree = ET.parse('DDSConfigFile.xml')
SubscriberHostIPV4 = tree.find("ServerInformation").find("SubscriberHostIPV4").text
SubscriberHostPort = int(tree.find("ServerInformation").find("SubscriberHostPort").text)


while 1:
    pass

print("End of program")
