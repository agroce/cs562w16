from __future__ import print_function
import math
import numpy as np
import pyopencl as cl
import pyopencl.array
import pyopencl.reduction

reduction_actions = {"a+b": lambda x, y: x + y,
                     "a*b": lambda x, y: x * y}


map_functions = {"sin": lambda x: math.sin(x)}


reduction_accumulators = {"a+b": "0",
                          "a*b": "1"}



def array_len(n):
    return 1 << n


def get_cpu_data(seed=42, min_endpoint=-10, max_endpoint=10, length=1024):
    return np.random.RandomState(seed=seed).randint(min_endpoint, max_endpoint, length).astype(np.int32)


def python_zip_with(cpu_data, func="a+b"):
    return reduction_actions[func](cpu_data, cpu_data)


def pyopencl_map_with(cpu_data, func="sin"):
    #TODO: implement me!
    pass


def pyopencl_zip_with(cpu_data, func="a+b"):
    platforms = cl.get_platforms()
    ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    queue = cl.CommandQueue(ctx)
    gpu_data_a = pyopencl.array.to_device(queue, cpu_data)
    gpu_data_b = pyopencl.array.to_device(queue, cpu_data)
    return reduction_actions[func](gpu_data_a, gpu_data_b).get()


def python_fold_with(cpu_data, func="a+b"):
    try:
        return reduce(reduction_actions[func], cpu_data)
    except TypeError:
        print("TypeError using {0} on {1}".format(func, cpu_data))


def pyopencl_fold_with(cpu_data, func="a+b"):
    platforms = cl.get_platforms()
    ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    queue = cl.CommandQueue(ctx)
    gpu_data = pyopencl.array.to_device(queue, cpu_data)
    kernel = pyopencl.reduction.ReductionKernel(ctx=ctx,
                                                dtype_out=np.int32,
                                                neutral=reduction_accumulators[func],
                                                reduce_expr=func,
                                                map_expr="x[i]",
                                                arguments="__global int *x")
    clresult = kernel(gpu_data).get()
    queue.finish()
    return clresult


def compare_reductions(seed=42, func="a+b", min_endpoint=-10, max_endpoint=10, length=32):
    print("Beginning {0} test on seed: {1}".format(func, seed))
    arr = get_cpu_data(seed, min_endpoint, max_endpoint, length)

    clresult = pyopencl_fold_with(arr, func)
    pyresult = python_fold_with(arr, func)
    print("reduce")
    print("original: {0}\nclresult: {1}\npyresult: {2}\nequivalent: {3}\n".format(arr, clresult, pyresult,
                                                                               clresult == pyresult))

    clresult = pyopencl_zip_with(arr, func=func)
    pyresult = python_zip_with(arr, func=func)
    print("zip")
    print("original: {0}\nclresult: {1}\npyresult: {2}\nequivalent: {3}\n".format(arr, clresult, pyresult,
                                                                               (clresult == pyresult).all()))


def main():
    compare_reductions()


if __name__ == '__main__':
    main()
