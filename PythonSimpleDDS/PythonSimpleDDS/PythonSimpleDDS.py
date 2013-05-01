import Filter
import SubscribeService
import xml.etree.ElementTree as ET

tree = ET.parse('DDSConfigFile.xml')
tree = tree.find("ServerInformation").find("ServerIPV4")
print(tree.text)
nothing = 5

newFilter = Filter.Filter()
newsub = SubscribeService.SubscribeService(newFilter)
subscriber = [5555, "192.168.1.1"]
newFilter.addSubscriber("Who", subscriber)

subscriber = [5555, "192.168.1.2"]
newFilter.addSubscriber("Who", subscriber)
newsub.testFilter("Who")
#print(newFilter.getSubscribers("Who"))
print("aa")

class PubSub:
    baseFilter = Filter.Filter()