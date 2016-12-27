import zerorpc
from calculator import calculator

s = zerorpc.Server(calculator())
s.bind("tcp://0.0.0.0:4242")
s.run()
