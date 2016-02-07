from __future__ import print_function
import numpy as np
import pyopencl as cl
import pyopencl.array
from pyopencl.reduction import ReductionKernel
from numpy.random import RandomState

expr = {"+" : lambda x, y: x + y,
        "-" : lambda x, y: x - y,
        "*" : lambda x, y: x * y,
        "/" : lambda x, y: x / y}

def PyOpenCLSumReduce():
    '''
    Prooof of concept for PyOpenCL to guide testing
    '''
    rand = RandomState(seed=42)
    vals = rand.randint(-10, 10, 1024)

    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    a = pyopencl.array.Array(cqa=queue, shape=vals.shape, dtype=vals.dtype)
    a.set(ary=vals)
    queue.finish()

    kernel = ReductionKernel(ctx=ctx,
                             dtype_out=np.int32,
                             neutral="0",
                             reduce_expr="a+b",
                             map_expr="x[i]",
                             arguments="__global int *x")

    clresult = kernel(a).get()
    queue.finish()

    pyresult = reduce(lambda x, y: x + y, vals)  # could also use np.sum(vals) for this case
    print("clresult: {0}, pyresult: {1}".format(clresult, pyresult))
    assert clresult == pyresult


def main():
    PyOpenCLSumReduce()


if __name__ == '__main__':
    main()
