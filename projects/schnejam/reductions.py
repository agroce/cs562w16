from __future__ import print_function
import numpy as np
import pyopencl as cl
import pyopencl.array
import pyopencl.reduction

reduction_actions = {"+": lambda x, y: x + y,
                     "-": lambda x, y: x - y,
                     "*": lambda x, y: x * y,
                     "/": lambda x, y: x / y}


def pyopencl_reduction(seed=42, length=3, reduction="+", min_endpoint=0, max_endpoint=5):
    """
    Proof of concept for PyOpenCL to guide testing
    :param seed: Seed for repeatability
    :param length: Length of test array
    :param reduction: Type of reduction to be performed, see expr
    :param min_endpoint: Lower bound of random values
    :param max_endpoint: Upper bound of random values
    :return: Nothing
    """
    assert isinstance(seed, int) and isinstance(length, int)
    assert isinstance(min_endpoint, int) and isinstance(max_endpoint, int)
    assert reduction in reduction_actions.keys()

    rand = np.random.RandomState(seed=seed)
    cpu_data = rand.randint(min_endpoint, max_endpoint, length).astype(np.int32)

    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)
    gpu_data = pyopencl.array.to_device(queue, cpu_data)

    kernel = pyopencl.reduction.ReductionKernel(ctx=ctx,
                                                dtype_out=np.int32,
                                                neutral="0",
                                                reduce_expr="a+b".format(reduction),
                                                map_expr="x[i]",
                                                arguments="__global int *x")
    clresult = kernel(gpu_data).get()
    queue.finish()

    pyresult = reduce(reduction_actions[reduction], cpu_data)
    print("clresult: {0}, pyresult: {1}".format(clresult, pyresult))
    return clresult == pyresult


def main():
    print(pyopencl_reduction(seed=42))


if __name__ == '__main__':
    main()
