# This is a simple publisher and subscriber module create with python. <br />
## The communications protocol is using UDP. <br />

There are 3 folders:  <br />
1) PythonSimpleDDS - The server <br />
2) ASimpleSubscriber - A subscriber <br />
3) ASimplePublisher - A publisher <br />

---------------------------------------
To use: <br />
Step 1: Run the server <br />
Step 2: Run the subscriber and publisher (Order does not matter) <br />

---------------------------------------
Example of Server is located in PythonSimpleDDS/PythonSimpleDDS.py <br />
Example of Publisher is located in ASimplePublisher/ASimplePublisher.py <br />
Example of Subscriber is located in ASimpleSubscriber/ASimpleSubscriber.py <br />

---------------------------------------
To use Server, you need the following .py files: <br />
1) PyPubSub.py <br />
2) PublisherService.py <br />
3) SubscribeService.py <br />
4) Filter.py <br />

To use Publisher, you need the following .py files: <br />
1) Publisher.py <br />

To use Subscriber, you need the following .py files: <br />
1) Subscriber.py <br />

---------------------------------------
Note: <br />
Server have to be on before initialising subscriber or publisher. <br />
The examples provided uses xml configuration files to read the server's ipv4 and port. You can hard code the ipv4 and port if you like. <br />

[See wiki for library APIs]("https://github.com/wengjjpaul/PythonSimpleDDS/wiki") <br />
