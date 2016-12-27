import zerorpc

client = zerorpc.Client()
client.connect("tcp://localhost:4242")
print(client.price(1))