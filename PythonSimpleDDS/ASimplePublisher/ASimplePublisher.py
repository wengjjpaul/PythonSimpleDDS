import socket
import time
import Publisher
import xml.etree.ElementTree as ET

tree = ET.parse('DDSConfigFile.xml')
PublisherHostIPV4 = tree.find("ServerInformation").find("PublisherHostIPV4").text
PublisherHostPort = int(tree.find("ServerInformation").find("PublisherHostPort").text)

firstPublisher = Publisher.Publisher(PublisherHostIPV4, PublisherHostPort)
firstPublisher.setTopic("topicOne")

while 1:
    firstPublisher.publishOnce("topicOne_Data")
    time.sleep(1)

print("End of program")