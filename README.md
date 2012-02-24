Mathematics
============

Various algorithms in python for the single purpose of learning.

Euclidean algorithm
------------

Calculate the greatest common divisor of two numbers using the euclidean algorithm.

    $ python EuclideanAlgorithm.py -h
    usage: EuclideanAlgorithm.py [-h] [-v] a b

    Calculate the greatest common divisor for two numbers, using the Euclidean
    algorithm.

    positional arguments:
      a              the first integer
      b              the second integer

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  display calculation steps


    $ python EuclideanAlgorithm.py -v 39088169 24157817
    a: 39088169
    b: 24157817
    Maximum iterations: 51
    [00] a=39088169, b=24157817
    [01] a=24157817, b=14930352
    [02] a=14930352, b=9227465
    [03] a=9227465, b=5702887
    [04] a=5702887, b=3524578
    [05] a=3524578, b=2178309
    [06] a=2178309, b=1346269
    [07] a=1346269, b=832040
    [08] a=832040, b=514229
    [09] a=514229, b=317811
    [10] a=317811, b=196418
    [11] a=196418, b=121393
    [12] a=121393, b=75025
    [13] a=75025, b=46368
    [14] a=46368, b=28657
    [15] a=28657, b=17711
    [16] a=17711, b=10946
    [17] a=10946, b=6765
    [18] a=6765, b=4181
    [19] a=4181, b=2584
    [20] a=2584, b=1597
    [21] a=1597, b=987
    [22] a=987, b=610
    [23] a=610, b=377
    [24] a=377, b=233
    [25] a=233, b=144
    [26] a=144, b=89
    [27] a=89, b=55
    [28] a=55, b=34
    [29] a=34, b=21
    [30] a=21, b=13
    [31] a=13, b=8
    [32] a=8, b=5
    [33] a=5, b=3
    [34] a=3, b=2
    [35] a=2, b=1
    Greatest common divisor: 1



Herons method (Babylonian method)
------------

Calculate the approximate square root of a number using Herons method.

    $ python HeronsMethod.py -h
    usage: HeronsMethod.py [-h] [-p PREC] [-v] number

    Calculate the approximate square root of a number, using Herons method.

    positional arguments:
      number                the number for the square root calculation

    optional arguments:
      -h, --help            show this help message and exit
      -p PREC, --prec PREC  set the precision (default=7). Higher numbers require
                            a higher precision.
      -v, --verbose         display calculation steps


    $ python HeronsMethod.py -v -p 3 144
    approximate square root of 144:
    [00] 37
    [01] 20
    [02] 13.6
    [03] 12.0941
    ----
    12.0941
    absolute error: -0.094100
    relative error: 0.007842



