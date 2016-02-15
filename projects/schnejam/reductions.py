from __future__ import print_function
import math
import numpy as np
import pyopencl as cl
import pyopencl.array
import pyopencl.reduction

reduction_actions = {"+": lambda x, y: x + y,
                     "-": lambda x, y: x - y,
                     "*": lambda x, y: x * y,
                     "/": lambda x, y: x / y}


def get_array_length(seed):
    return int(math.pow(2, 1 + seed % 12))


def get_cpu_data(seed=42, min_endpoint=-10, max_endpoint=10, exponent=10, maxlength=None):
    length = maxlength if maxlength else get_array_length(exponent)
    return np.random.RandomState(seed=seed).randint(min_endpoint, max_endpoint, length).astype(np.int32)


def python_reduction(cpu_data, reduction="+"):
    return reduce(reduction_actions[reduction], cpu_data)


def pyopencl_reduction(cpu_data, reduction="+"):
    platforms = cl.get_platforms()
    ctx = cl.Context(dev_type=cl.device_type.ALL, properties=[(cl.context_properties.PLATFORM, platforms[0])])
    queue = cl.CommandQueue(ctx)
    gpu_data = pyopencl.array.to_device(queue, cpu_data)

    expr = "a{0}b".format(reduction)
    kernel = pyopencl.reduction.ReductionKernel(ctx=ctx,
                                                dtype_out=np.int32,
                                                neutral="0",
                                                reduce_expr=expr,
                                                map_expr="x[i]",
                                                arguments="__global int *x")
    clresult = kernel(gpu_data).get()
    queue.finish()
    return clresult


def compare_reductions(seed=42, reduction="+", min_endpoint=-1024, max_endpoint=1024, maxlength=None):
    arr = get_cpu_data(seed, min_endpoint, max_endpoint, maxlength)
    print(arr)

    clresult = pyopencl_reduction(arr, reduction)
    pyresult = python_reduction(arr, reduction)

    print("clresult: {0}, pyresult: {1}".format(clresult, pyresult))
    return clresult == pyresult


def main():
    compare_reductions(seed=246, reduction="-", maxlength=10)


if __name__ == '__main__':
    main()
