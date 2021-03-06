from __future__ import print_function
import math
import numpy as np
import pyopencl as cl
import pyopencl.array
import pyopencl.reduction
from pyopencl.algorithm import partition
from pyopencl.algorithm import unique
from pyopencl.algorithm import RadixSort                                          


#region Text : Expression dictionaries
# The pyopencl library accepts the stringified equivalent of an expression
# so we can have a mapping to the actual function here!d

# Associative actions that can be attempted in a reduction on the GPU
reduction_actions = {"a+b": lambda x, y: x + y,
                     "a*b": lambda x, y: x * y}

# The accumulators for the appropriate reductions
reduction_accumulators = {"a+b": "0",
                          "a*b": "1"}

# Functions to execute a test against two values fore equality in filtering
filter_preds = {"ary[i] > val": lambda val, t: t > val,
                "ary[i] < val": lambda val, t: t < val,
                "ary[i] >= val": lambda val, t: t >= val,
                "ary[i] <= val": lambda val, t: t <= val,
                "ary[i] == val": lambda val, t: t == val}

#endregion

#region Helper Methods

def get_queue_and_context():
    """
    Get a queue and a context for a gpu job
    :return: A tuple queue, context
    """
    platforms = cl.get_platforms()
    ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    queue = cl.CommandQueue(ctx)
    return queue, ctx

def get_queue():
    """
    Get a queue for a gpu job
    :return: A queue for the gpu
    """
    queue, _ = get_queue_and_context()
    return queue

def array_len(n):
    """
    Returns the value for the function 2^n where n is the input value
    These values can get reasonably large and make sense for testing on a GPU
    :param n: The exponent value in the function 2^floor(n)
    :return: A value that is a power of 2, where the exponent is the floored value of n
    """
    return 1 << int(n)


def get_cpu_data(seed=42, min_endpoint=-10, max_endpoint=10, length=1024):
    """
    Generates a numpy array of values with several constraints for relatively easily generating a list for moving to the GPU
    :param seed: The random seed so we can re-execute a test later on
    :param min_endpoint: The minimum value allowed in the array
    :param max_endpoint: The maximum value allowed in the array
    :param length: The length of the resulting array
    :return: A deterministic "random" numpy array
    """
    return np.random.RandomState(seed=seed).randint(min_endpoint, max_endpoint, length).astype(np.int32)


def evaluate(success, arr):
    """
    Evaluates the success and prints the array if the "test" failed
    :param success: The result of the test
    :param arr: The array the test acted on
    :return: Nothing
    """
    if not success: print(arr)
    assert success

#endregion

#region Oracle Methods

def python_zip_with(cpu_data, func="a+b"):
    """
    Oracle
    Serially executes the zip between two copies of cpu_data based on some function
    :param cpu_data: An array to duplicate and zip between
    :param func: The function to zip the two arrays
    :return: An array resulting from the zip function on two of the cpu_data arrays
    """
    return reduction_actions[func](cpu_data, cpu_data)


def python_unique(cpu_data):
    """
    Oracle
    Gets a sorted list of the unique values in the input array, it uses the nature of a set to get rid of duplicate values
    We sort to match what the pyopencl_unique test method is expecting
    :param cpu_data: An array of values
    :return: The list of sorted unique values from the original array.
    """
    return sorted(list(set(cpu_data)))


def python_filter(cpu_data, target, func="ary[i] == val"):
    """
    Oracle
    Executes a list comprehension that filters against the predicate in filter_preds matching func
    :param cpu_data: An array of values
    :param func: The predicate used to determine if a value should show up in the resulting array
    :param target: The value to filter the list against
    :return: A tuple representing: the filtered list of values, and it's compliment
    """
    filtered = [v for v in cpu_data if filter_preds[func](target, v)]
    compliment = [v for v in cpu_data if not filter_preds[func](target, v)]
    return filtered, compliment


def python_fold_with(cpu_data, func="a+b"):
    """
    Oracle
    :param cpu_data:
    :param func:
    :return:
    """
    try:
        return reduce(reduction_actions[func], cpu_data)
    except TypeError:
        print("TypeError using {0} on {1}".format(func, cpu_data))

#endregion

#region SUT Methods

def pyopencl_unique(cpu_data):
    """
    SUT
    This is a function that sets up a GPU context and exposes the pyopencl algorithm uniqe to the TSTL random tester
    The Unique function resembles the UNIX command uniq,
    and requires that values must be sorted to get a list of "unique" values.
    Therefore, this method sorts the cpu_data array before transferring it to the GPU.

    It executes the method python_unique as its oracle.
    :param cpu_data: A numpy array to execute the pyopencl unique algorithm on.
    :return: A boolean that describes if the CPU oracle and the SUT results match
    """
    # platforms = cl.get_platforms()
    # ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    # queue = cl.CommandQueue(ctx)
    queue = get_queue()

    cpu_data.sort()
    gpu_data = pyopencl.array.to_device(queue, cpu_data)

    unique_gpu, count_unique_gpu, evt = unique(gpu_data)
    unique_cpu = python_unique(cpu_data)

    count_unique_gpu = count_unique_gpu.get()
    unique_gpu = unique_gpu.get()

    return (unique_gpu[:count_unique_gpu] == unique_cpu).all()


def pyopencl_filter(cpu_data, func="ary[i] == val", target=None):
    """
    SUT
    This is a function that sets up a GPU context and exposes the pyopencl algorithm filter to the TSTL random tester
    The Filter function checks all the values in some list against a given target value and leaves them if they
    agree with evaluation of the predicate, e.g.: 1 > 3 returns false where 1 is the value and 3 is the target

    It executes the method python_filter as its oracle.
    :param cpu_data: A numpy array to execute the pyopencl filter algorithm on.
    :param func: The predicate used to determine if a value should show up in the resulting array
    :param target: The value to filter the list against, if none is given it will filter against the first value in the array
    :return: A boolean that describes if the CPU oracle and the SUT results match
    """
    # platforms = cl.get_platforms()
    # ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    # queue = cl.CommandQueue(ctx)
    queue = get_queue()

    gpu_data = pyopencl.array.to_device(queue, cpu_data)

    target = target if target else cpu_data[0]

    true_cpu, false_cpu = python_filter(cpu_data=cpu_data, target=target, func=func)
    true_gpu, false_gpu, n_gpu_true, evt = partition(gpu_data, func, [("val", target)])

    n_gpu_true = n_gpu_true.get()

    return (true_gpu.get()[:n_gpu_true] == true_cpu).all() and \
           (false_gpu.get()[:len(cpu_data) - n_gpu_true] == false_cpu).all()


def pyopencl_zip_with(cpu_data, func="a+b"):
    """
    SUT
    This is a function that sets up a GPU context and exposes the pyopencl algorithm zip to the TSTL random tester
    The Zip function makes two copies of the cpu_data and moves them to the GPU and executes the function for each value

    It executes the method python_zip_with as its oracle.
    :param cpu_data: A numpy array to execute the pyopencl zip implementation on
    :param func: A function to combine two values
    :return: A boolean that describes if the CPU oracle and the SUT results match
    """
    # platforms = cl.get_platforms()
    # ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    # queue = cl.CommandQueue(ctx)

    queue = get_queue()

    cpu_result = python_zip_with(cpu_data, func)

    gpu_data_a = pyopencl.array.to_device(queue, cpu_data)
    gpu_data_b = pyopencl.array.to_device(queue, cpu_data)
    gpu_result = reduction_actions[func](gpu_data_a, gpu_data_b).get()

    return (gpu_result == cpu_result).all(), cpu_result


def pyopencl_fold_with(cpu_data, func="a+b"):
    """
    SUT
    This is a function that sets up a GPU context and exposes the pyopencl implementation of Reduction

    It executes the method python_fold_with as its oracle.
    :param cpu_data: A numpy array to execute the pyopencl implementation of Reduce on
    :param func: An associative function to combine two values
    :return: A boolean that describes if the CPU oracle and the SUT results match
    """
    # platforms = cl.get_platforms()
    # ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    # queue = cl.CommandQueue(ctx)

    queue, ctx = get_queue_and_context()

    cpu_result = python_fold_with(cpu_data, func)

    gpu_data = pyopencl.array.to_device(queue, cpu_data)
    kernel = pyopencl.reduction.ReductionKernel(ctx=ctx,
                                                dtype_out=np.int32,
                                                neutral=reduction_accumulators[func],
                                                reduce_expr=func,
                                                map_expr="x[i]",
                                                arguments="__global int *x")
    gpu_result = kernel(gpu_data).get()
    queue.finish()

    return gpu_result == cpu_result

#endregion

#region TSTL Wrappers

def compare_zip(arr, func):
    """
    TSTL arbitrary code for zip
    :param arr: TSTL generated numpy array
    :param func: TSTL chosen function
    """
    success, cpu_result = pyopencl_zip_with(arr, func)
    evaluate(success, arr)

def compare_fold(arr, func):
    """
    TSTL arbitrary code for fold
    :param arr: TSTL generated numpy array
    :param func: TSTL chosen function
    """
    success = pyopencl_fold_with(arr, func)
    evaluate(success, arr)

def compare_filters(arr, func):
    """
    TSTL arbitrary code for filter
    :param arr: TSTL generated numpy array
    :param func: TSTL chosen function
    """
    success = pyopencl_filter(arr, func)
    evaluate(success, arr)

def compare_unique(arr):
    """
    TSTL arbitrary code for unique
    :param arr: TSTL generated numpy array
    """
    success = pyopencl_unique(arr)
    evaluate(success, arr)

#endregion

def single_test_case():
    seed0 = 12
    length1 = int(array_len(6))
    array1 = get_cpu_data(seed=seed0, min_endpoint=-10, max_endpoint=10, length=length1)

    compare_unique(array1)
    compare_filters(array1, "ary[i] > val")
    compare_zip(array1, "a+b")
    compare_fold(array1, "a+b")

    # This will most likely succeed because it requires several executions to fail

    print("TEST_FINISHED")

def main():
    single_test_case()


if __name__ == '__main__':
    main()
