## CS 562 Project ##
### Part 1: Proposal ###

#### System Under Test - PyOpenCL ####
The library I am propsing as my system under test (sut) is PyOpenCL.
This library provides access in python to the entire OpenCL API while removing a significant amount of setup required when implementing directly in C++. 
From a testing perspective parallelization can be interesting because it is significantly more difficult to write and test [1].
TSTL could prove useful in this setting as automating the construction of tests may help poke holes in the parallel implementation of these algorithms.

Some algorithms to test are: map, reduce, radix sort, and list generation.
Additionally, a large amount of mathematical functions can be applied to elements in arrays in PyOpenCL, but these may not be as interesting as the functions that deal with communication between separate threads.

#### Testing PyOpenCL ####
I am currently planning to test two aspects of the PyOpenCL API: correctness and performance.

##### Correctness #####
Ensuring correctness is key, this can be achieved by using the built in serial implementations of the respective parallel algorithms as oracles.
The serial implementation of these is as trivial as:
- Map: list(map(fun, somelist))
- Reduce (sum): sum(somelist)
- Sort: somelist.sort() 

##### Performance #####
In addition to correctness we can verify that PyOpenCL is providing the speedup that we are expecting.
The performance of the oracles (listed above) can be compared to the implementations found in PyOpenCL.
It should be noted though that expected performance depends on the size of the work load, to warrant the context switches and other overhead associated with GPU computing.

#### Description of PyOpenCL ####
The PyOpenCL libraries can be found here: https://pypi.python.org/pypi/pyopencl
It requires the presence of gcc/g++ (on a linux system), numpy, and OpenCL capable drivers.

OpenCL itself requires a significant amount of setup with a large amount of room for error. 
Unfortunately, wrapping C++ libraries within Python can also be a source of issues, this might be a result of developers incorrectly interfacing two separate systems.
All of these moving parts in conjunction presents an excellent opportunity for testing both a parallel library as well as the integration of two independent systems.

#### Citations ####
[1] Junfeng Yang, Heming Cui, Jingyue Wu, Yang Tang, and Gang Hu. 2014. Making parallel programs reliable with stable multithreading. Commun. ACM 57, 3 (March 2014), 58-69. DOI=http://dx.doi.org/10.1145/2500875

