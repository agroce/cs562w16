from __future__ import print_function
import math
import numpy as np
import pyopencl as cl
import pyopencl.array
import pyopencl.reduction
from pyopencl.algorithm import partition
from pyopencl.algorithm import unique
from pyopencl.algorithm import RadixSort                                          


reduction_actions = {"a+b": lambda x, y: x + y,
                     "a*b": lambda x, y: x * y}


map_functions = {"sin": lambda x: math.sin(x)}


reduction_accumulators = {"a+b": "0",
                          "a*b": "1"}

filter_preds = {"ary[i] > val": lambda val, t: t > val,
                "ary[i] < val": lambda val, t: t < val,
                "ary[i] >= val": lambda val, t: t >= val,
                "ary[i] <= val": lambda val, t: t <= val,
                "ary[i] == val": lambda val, t: t == val}

def array_len(n):
    return 1 << n


def get_cpu_data(seed=42, min_endpoint=-10, max_endpoint=10, length=1024):
    return np.random.RandomState(seed=seed).randint(min_endpoint, max_endpoint, length).astype(np.int32)


def python_zip_with(cpu_data, func="a+b"):
    return reduction_actions[func](cpu_data, cpu_data)


def pyopencl_unique(cpu_data):
    platforms = cl.get_platforms()
    ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    queue = cl.CommandQueue(ctx)

    cpu_data.sort()
    gpu_data = pyopencl.array.to_device(queue, cpu_data)

    unique_gpu, count_unique_gpu, evt = unique(gpu_data)
    unique_cpu = sorted(list(set(cpu_data)))

    count_unique_gpu = count_unique_gpu.get()
    unique_gpu = unique_gpu.get()

    return (unique_gpu[:count_unique_gpu] == unique_cpu).all()


def pyopencl_filter(cpu_data, func="ary[i] == val", target=None):
    platforms = cl.get_platforms()
    ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    queue = cl.CommandQueue(ctx)
    gpu_data = pyopencl.array.to_device(queue, cpu_data)

    target = target if target else cpu_data[0]
    true_cpu = [v for v in cpu_data if filter_preds[func](target, v)]
    false_cpu = [v for v in cpu_data if not filter_preds[func](target, v)]

    true_gpu, false_gpu, n_gpu_true, evt = partition(gpu_data, func, [("val", target)])
    n_gpu_true = n_gpu_true.get()

    return (true_gpu.get()[:n_gpu_true] == true_cpu).all() and \
           (false_gpu.get()[:len(cpu_data) - n_gpu_true] == false_cpu).all()


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


def compare_reductions(seed=42, func="a+b", min_endpoint=-2, max_endpoint=2, length=16):
    arr = get_cpu_data(seed, min_endpoint, max_endpoint, length)

    pyopencl_unique(arr)

    for k in filter_preds.keys():
        pyopencl_filter(arr, k)

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
