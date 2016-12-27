import zerorpc

client = zerorpc.Client()
client.connect("tcp://localhost:4242")
print(client.price(96.2, 57.20, 0.0006, 0.1567, 0, (2016,11,29), (2016,11,24)))
