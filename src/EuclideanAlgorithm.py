#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import math


def gcd(a, b):
    if b == 0:
        return a

    if args.verbose:
        global iter
        print('[%02d] a=%d, b=%d' % (iter, a, b))
        iter = iter + 1

    return gcd(b, a % b)


def max_iterations(b):
    return 2 * math.log(2 * b, 2)


parser = argparse.ArgumentParser(description='Calculate the greatest common \
                    divisor for two numbers, using the Euclidean algorithm.')
parser.add_argument('a', type=int, help='the first integer')
parser.add_argument('b', type=int, help='the second integer')
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose',
                    default=False, help='display calculation steps')
args = parser.parse_args()

a = max(args.a, args.b)
b = min(args.a, args.b)
iter = 0
print('a: %d' % a)
print('b: %d' % b)
print('Maximum iterations: %d' % max_iterations(b))
print('Greatest common divisor: %d' % gcd(a, b))
