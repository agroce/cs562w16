#!/bin/bash
sudo apt-get install opencl-headers python-pip python-dev python-numpy python-mako virtualenv libffi-dev
virtualenv pythonopencl-testing
source pyopencl-testing/bin/activate
cd pyopencl-testing
git clone https://github.com/pyopencl/pyopencl.git
python pyopencl/setup.py
