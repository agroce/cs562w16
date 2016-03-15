## CS 562 Project ##
### Table of Contents ###
+ Part 0: VirtualEnv Setup
+ Part 4: Final Report
+ Part 3: Progress Report
+ Part 1: Proposal

__Disclaimer:__ In an effort to show the evolution of this project, I have maintained the other two writing portions assigned earlier in the quarter. Therefore, there may be sections in Part 4 that disagree with Parts 1 and 3.

## Part 0: VirtualEnv Setup ##
Setup a virtualenv using the requirements file like this (see the requirements.txt file in this directory):
```
pip install -r requirements.txt
```

You may need to install PyOpenCL directly from its repo like so:
```
pip install git+https://github.com/pyopencl/pyopencl.git
```

## Part 4: Final Report ##

#### Accomplishments ####
The testing effort here has succeeded on one front that was unexpected (runtime errors), and another that was part of the original plan (correctness), but performance testing ultimately seemed to be unnecessary next to the possibility of uncovered runtime issues.
The runtime error is discussed in detail in the "bugs found" section.

##### Correctness #####
The most obvious methods to target for correctness were to pick things that could be trivially represented using python constructs like list comprehensions and lambda expressions.
To that end I successfully tested the correctness for the high order functions like: zip, fold, and filter.
The arbitrary python code included and executed from TSTL includes the following test methods:
+ pyopencl_fold_with - Folds an array of values that has been transmitted using a given function.
+ pyopencl_zip_with - Zips two arrays of values that has been transmitted using a given function.
+ pyopencl_filter - Filters an array of values based on a given predicate.
+ pyopencl_unique - Sorts (on the CPU) an array of values and then returns the unique values.

All of the above listed PyOpenCL wrapper functions have trivial serial implementations that at the most complex use a list comprehension like:
```python
return [v for v in cpu_data if filter_preds[func](target, v)]
```
to the simplest which makes use of clever data structure constructors:
```python
return sorted(list(set(cpu_data)))
```
and finally easy lambda expressions:
```python
return reduce(lambda x, y: x + y, cpu_data)
```

Out of all the tests executed, all passed the correctness testing but were ultimately interrupted by the runtime error discussed below.


##### Performance #####
I abandoned the performance testing in favor of pursuing issues relating to the transmission of stringified code to the GPU compiler or perhaps issues communicating with the GPU itself; the power of the GPU is not in question nor is the efficacy of OpenCL compilers, and testing performance on a GPU is not trivial because of the time it takes to transmit data over the bus, etc.


#### Bugs Found ####
The runtime error experienced
`ERROR: (<class 'pyopencl.cffi_cl.RuntimeError'>, RuntimeError(<pyopencl.cffi_cl._ErrorRecord object at 0x7f3dfa50ed88>,)`
in most of the test cases. Preventing all test operations save pyopencl_fold_with from executing seems to prevent the error (as far as 500 tests with a depth of 50), however there is no issue resulting from correctness.
This error seems to be related with the GPU context, and I suspect that it might be corrupt state on the graphics card after executing several tests in a row since part of the traceback includes the line

```python
platforms = cl.get_platforms()
```

which is part of the method that generates the GPU context for every other successful test.
Similar bugs have been detected on both a MacBook Pro (Dr. Groce's workstation) as well as a custom built desktop with a GeForce GTX 670 which is accessible using PyOpenCL in the python repl like so:

```python
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
# yields <pyopencl.Device 'GeForce GTX 670' on 'NVIDIA CUDA' at 0x2235150>
```


#### Efficacy of Tester ####
The tester seems to do a good job at testing correctness, since the oracle methods used are well known and almost free in terms of writing.
So if the unique oracle was wrong, it would mean that the set data structure was wrong, or turning the set into a list is wrong which are tested by the many python users daily which seems unlikely.

Finding bugs in terms of runtime errors or during GPU compiling or transport of kernel code to GPU on the other hand is more difficult to test since the exception where PyOpenCL fails to provide a platform properly so we can't get any farther in the test because of it.

__Disclaimer:__ This might be a result of a misunderstanding I have with how to setup a device and context, but this seems unlikely since the same generator method is used for the fairly robust reduction test method.

#### Coverage Summary ####
There are several files in PyOpenCL that have reasonable amounts of coverage in terms of how many methods were tested.

There are 4 high order methods that are under test, three of which come from the algorithm.py file (unique, filter, and zip) the fourth fold uses the ReductionKernel which is its own class and may explain why it is impervious to the bug found in the other three methods.
Upon further thought it might be that using the RAII class `ReductionKernel` is better at cleaning up state than the methods `unique()`, `partition()`, and zip (which is just the execution of a lambda expression against the arrays loaded onto the GPU).
Each call to the python wrapper creates its own queue and context however, which means that these contexts and queues are going out of scope and should be cleaned up...

The full coverage file is included in this directory: `final_coverage.out`.
The highlights of the coverage are:
+ cffi_cl.py - 17% coverage, this isn't too high but might merit more investigation/targeting since this is where the runtime error is.
+ algorithm.py - 8% coverage, which makes sense since approximately that amount of methods were tested from that file. A cursory scroll through this file shows that most of the methods have minimal branching and large portions of code are stringified code and therefore coverage may not mean much here.
+ array.py and dtypes.py - 20% and 18% coverage respectively, I found this surprising since I only knowingly used this code when moving arrays to the GPU.
+ scan.py - 56% coverage, this also has huge amounts of string code. I suspect that a large amount of the algorithms and/or the Reduction kernel uses this code to deal with intelligently assigning work group data.
+ reduction.py - 40% coverage, this is impressive since only one (or two) methods (a class constructor and its call) are being executed for the Fold test.
+ tools.py - 32% coverage, the kernel template is located in here, I suspect the reduction kernel is using some of this code, and this seems like a place for helper methods from other methods as well.

#### Downsides of TSTL ####
I find TSTL to be a rather pleasing way to write tests, having written unit tests in C# at a previous workplace and being displeased with their inefficacy; having said that, however, there is room for improvement.

First and foremost, as I am a huge fan of threading, it would be really cool to have a construct in TSTL to define groups of actions that should be able to act within their own thread.
For example, each of my four actions can and should be able to run independent of each other and I would like to keep attempting to test `zip()` and not stop the entire process if `unique()` throws an exception.
This of course would not work in the case of a data structure test like the sample AVL code, but does lend itself to more one off random test instances like PyOpenCL or perhaps NumPy where the object is to use the built in random facilities to generate a large list based on a random value from TSTL and execute the test.
A way to achieve this (syntactically) might be something like this in TSTL pseudo code:
```
# This brace represents a group of actions that might be executed
# on a new thread and is independent from the other group but is still
# in this API and uses a lot of the same initialization and setup code.
<{
    log: thread_group_a
    <classa>.my_actiona(<int>)
    <classa>.my_actionb(<int>)
    <classa>.my_actionc(<int>)
}>
<{
    log: thread_group_b
    <classb>.my_actionx(<int>)
    <classb>.my_actiony(<int>)
    <classb>.my_actionz(<int>)
}>
```

Additionally, it would be nice for the included random tester and other testers to accept a file path to a TSTL file and compile it on its own or a wrapper (I have provided some bash files in this repo but they are extremely limited).

Finally, a syntax plugin for tools like PyCharm or Atom.io would be most excellent!
This is the reason that the vast majority of my code is in a raw python file and imported directly into the TSTL file since I found that writing tests of any significant complexity became tedious in a raw text file.

#### Upsides of TSTL ####
As I said before, writing tests in TSTL is nice, I can quickly setup constructors and actions and not worry about the order in which the details take place. The compressed syntax like `<[1..20]>` is a treat and a great way to think about things, however I find myself fretting over the possibly resulting bloated python code.
The control constructs like pre and post conditions as well as preservation of state `~<item>` is wonderful as well and lends itself to data structure testing.
The guard construct that is used to verify that items are initialized before a test is executed is fantastic as well.

TSTL certainly lends itself to testing data structures, and with the addition of a few constructs it could be extremely well suited to test large systems and APIs.



## Part 3: Progress Report ##

#### Bugs Found ####
It appears that I have found a runtime error, it appears that executing the filter method on a list of size 1 will result in a runtime error.
The value used in the filter is the first value in the array, which means in both > and < cases should return false and >=, <=, and == should return true, not a runtime error.
The steps to recreate the test were:

```python
FINAL VERSION OF TEST, WITH LOGGED REPLAY:
seed2 = 20                                                               # STEP 0  
length1 = int(red.array_len(10))                                         # STEP 1  
array1 = red.get_cpu_data(seed=seed2, min_endpoint=-10, max_endpoint=10, length=length1)  # STEP 2  
ufunc1 =  "ary[i] < val"                                                 # STEP 3  
compare_predicates(array1, ufunc1)                                       # STEP 4
```

This failure merits further investigation so that it can be discussed in the final report.
I currently have a one-off test for this error, but it does not yield the runtime error.
This might mean that some of the other tests aren't being properly cleaned up and will allow for easier targeting of the issue in further iterations.

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
Given the fact that algorithm.py is just over 1000 lines of code (including doc strings) and 50 function definitions, and only 4 functions are in the test suite (which happen to be just under 8% of the methods in the algorithm file, the reduction method has its own file).
Based on this fact it would seem that the goal of adding more functions to the tstl file would improve coverage, but this would only provide verification to the already impressive test suite.


## Part 1: Proposal ##

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
