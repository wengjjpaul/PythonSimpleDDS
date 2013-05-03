import Filter
import PublisherService
import SubscribeService
import threading

class PyPubSub:
    def __init__(self, aSubscriberHostIPV4, aSubscriberHostPort, aPublisherHostIPV4, aPublisherHostPort):
        """Both host IPV4 should be '' to receive from all host"""
        self.mMainFilter = Filter.Filter()
        self.mSubscriberHostService = SubscribeService.SubscribeService(self.mMainFilter, '', aSubscriberHostPort)
        self.mPublisherHostService = PublisherService.PublisherService(self.mMainFilter, '', aPublisherHostPort)
        self.mSubscriberServiceRunning = False
        self.mPublisherServiceRunning = False
        self.mSubscriberServiceThread = threading.Thread(target=self._publisherService, args = (self.mPublisherHostService,))
        self.mPublisherServiceThread = threading.Thread(target=self._subscriberService, args = (self.mSubscriberHostService,))
    def startSubscriberHostService(self):
        if(self.mSubscriberServiceRunning == False):
            #wont keep the thread up if main thread die
            self.mSubscriberServiceThread.daemon = True
            self.mSubscriberServiceThread.start()
            self.mSubscriberServiceRunning = True
    def startPublisherHostService(self):
        if(self.mPublisherServiceRunning == False):
            #wont keep the thread up if main thread die
            self.mPublisherServiceThread.daemon = True
            self.mPublisherServiceThread.start()
            self.mPublisherServiceRunning = True
    def _subscriberService(self, service):
        service.hostSubscribeService()
    def _publisherService(self, service):
        service.HostPublisherService()
    def stopSubscriberHostService(self):
        if self.mSubscriberServiceThread.isAlive():
            try:
                self.mSubscriberServiceThread._stop()
            except:
                pass
    def stopPublisherHostService(self):
        if self.mPublisherServiceThread.isAlive():
            try:
                self.mPublisherServiceThread._stop()
            except:
                pass
