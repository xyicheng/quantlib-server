# quantlib-server
expose quantlib via zerorpc on python

# Dependencies
pytest (3.0.5)
zerorpc (0.6.0)

pip install zerorpc
pip install pytest

# To run tests
pytest

# To install Quantlib on your linux box:
wget https://sourceforge.net/projects/quantlib/files/QuantLib/1.9/QuantLib-1.9.tar.gz/download -O QuantLib-1.9.tar.gz
wget https://sourceforge.net/projects/quantlib/files/QuantLib/1.9/other%20languages/QuantLib-SWIG-1.9.tar.gz/download -O QuantLib-SWIG-1.9.tar.gz

then follow instruction from http://www.cs.utah.edu/~cxiong/Files/Misc/QuantLib_Python.html
