#!/bin/sh

rm -rf sut.py
tstl pyopencl.tstl
python2.7 ~/tstl/generators/randomtester.py --maxtests=50 --nocover --depth=25