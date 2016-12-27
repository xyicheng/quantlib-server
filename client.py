import zerorpc

client = zerorpc.Client()
client.connect("tcp://localhost:4242")
print(client.price(96.2, 57.20, 0.06, 15.67, 6, 0))