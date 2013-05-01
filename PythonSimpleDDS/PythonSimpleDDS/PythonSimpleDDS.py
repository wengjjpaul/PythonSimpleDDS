import Filter
import SubscribeService
import xml.etree.ElementTree as ET
import threading

def subscriberService(service):
    service.hostSubscribeService()

tree = ET.parse('DDSConfigFile.xml')
tree = tree.find("ServerInformation").find("ServerIPV4")
print(tree.text)

newFilter = Filter.Filter()
subscriber = ("192.168.1.1", 5555)
newFilter.addSubscriber("hello", subscriber)

newsub = SubscribeService.SubscribeService(newFilter)
t = threading.Thread(target=subscriberService, args = (newsub,))
#wont keep the thread up if main thread die
t.daemon = True
t.start()

subscriber = ("192.168.1.2", 5555)
newFilter.addSubscriber("hello", subscriber)
newsub.testFilter("hello")
while 1:
    pass
print("aa")

