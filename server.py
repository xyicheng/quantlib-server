import zerorpc
from calculator import Calculator

s = zerorpc.Server(Calculator())
s.bind("tcp://0.0.0.0:4242")
s.run()
