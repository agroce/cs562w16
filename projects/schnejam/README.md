## CS 562 Project ##
###Table of Contents
+ Part 0: VirtualEnv Setup
+ Part 3: Progress Report
+ Part 1: Proposal


### Part 0: VirtualEnv Setup ###
Setup a virtualenv using the requirements file like this:
`pip install -r requirements.txt`

You may need to install PyOpenCL directly from it's repo like so:
`pip install git+https://github.com/pyopencl/pyopencl.git`


### Part 3: Progress Report ###

#### Bugs Found ####
It appears that I have found a runtime error, it appears that executing the filter method on a list of size 1 will result in a runtime error.
The value used in the filter is the first value in the array, which means in both > and < cases should return false and >=, <=, and == should return true, not a runtime error.
The steps to recreate the test were:

```FINAL VERSION OF TEST, WITH LOGGED REPLAY:
seed2 = 20                                                               # STEP 0
length1 = int(red.array_len(10))                                         # STEP 1
array1 = red.get_cpu_data(seed=seed2, min_endpoint=-10, max_endpoint=10, length=length1)  # STEP 2
ufunc1 =  "ary[i] < val"                                                 # STEP 3
compare_predicates(array1, ufunc1)                                       # STEP 4 ```

This failure merits further investigation so that it can be discussed in the final report.

#### Testing progress and improvements ####
The improvements made to the test suite include the addition of several more algorithms including the PyOpenCL filter and unique methods.
This has resulted in an improvement to the coverage of the algorithm.py file found in PyOpenCL and will be discussed further in the section on code coverage.

#### Progress by end of term ####
I found that implementing these further tests for algorithm.py was useful in finding a runtime error despite the high quality of the SUT, and I believe that continuing to write tests that exercise the provided GPU algorithms is a good way to test code that will likely be used by the majority of people using this system.
Because these algorithms are pre-built it is relatively reasonable to leverage random testing, what will likely not be possible by the end of the term but still merits some investigation is the custom gpu kernels.
A custom kernel is a program that can be run on GPU stream processors.
These custom kernels are made up of code that can be sent to the compiler within the device driver and a large enough program might be able to flesh out issues in the PyOpenCL layer, but would also be testing the kernel compiler.
Additionally, PyOpenCL contains support for executing tests for each device capable of executing opencl code and might be interesting to expose to tstl.

In short, I think that testing a much larger percentage of the algorithm module within PyOpenCL will be a good way to test predefined logic within the SUT, but will ignore the issues that might show up in converting a user defined program.

#### Quality of SUT ####
Based on my examination, the PyOpenCL library is an extremely high quality piece of software.
It is written and maintained by the same maintainer of PyCUDA and many other python based scientific computing packages.
Additionally it is listed in the SciPy scientific computing software [collection](http://scipy.org/topical-software.html#head-b98ffdb309ccce4e4504a25ea75b5c806e4897b6).

The library itself contains an impressive test suite that gives me confidence in the library:
+ It uses NumPy's serial implementations as its oracle, this is impressive because NumPy itself is highly regarded.
+ It executes all of its tests using the interaction of different NumPy datatypes which yields an extra level of complexity compared to my test suite which only makes use of NumPy's Int32.
+ The test file for the algorithm module is almost 80% the size the actual algorithm module and appears to at least test every method and class in the algorithm module.

#### Code coverage ####
The code coverage for the progress I have made for part 3 unfortunately only results in a 8% coverage of the algorithm.py module.
Given the fact that algorithm.py is just over 1000 lines of code (including doc strings) and 50 function definitions, and only 4 functions are in the test suite (which happen to be 8% of the methods).
Based on this fact it would seem that the goal of adding more functions to the tstl file would improve coverage, but this would only provide verification to the already impressive test suite.


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
The serial implementation of these are as trivial as:
- Map: list(map(fun, somelist))
- Reduce (sum): sum(somelist)
- Sort: somelist.sort()

Some additional targets for testing include predicate copies, for example:  
- "return a list where n > 100 in some list": [i for i in somelist if i > 100]

While these can be trivial to implement in serial, there might be issues associated with translating a predicate to OpenCL.

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
