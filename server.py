import zerorpc
from quantlibserver.calculator import Calculator

s = zerorpc.Server(Calculator())
s.bind("tcp://0.0.0.0:4242")
s.run()
