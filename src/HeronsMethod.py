#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import math
import decimal


def sqrt_approximate(number, guess):
    global iter
    new_guess = (guess + (decimal.Decimal(number) / guess)) / 2

    if args.verbose:
        decimal.getcontext().prec = int(round(math.pow(2, args.prec - iter) + \
                            math.pow(2, args.prec - iter - 1), 0))
        if decimal.getcontext().prec < 1:
            decimal.getcontext().prec = 1
        print('[%02d]' % (args.prec - iter)),
        print(new_guess)

    if iter == 0:
        return new_guess

    iter = iter - 1
    return sqrt_approximate(number, new_guess)


parser = argparse.ArgumentParser(description='Calculate the approximate \
                    square root of a number, using Herons method.')
parser.add_argument('number', type=int, help='the number for the square root \
                    calculation')
parser.add_argument('-p', '--prec', action='store', dest='prec',
                    default=7, type=int, help='set the precision (default=7).\
                    Higher numbers require a higher precision.')
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose',
                    default=False, help='display calculation steps')
args = parser.parse_args()

iter = args.prec
number = args.number
decimal.getcontext().prec = int(round(math.pow(2, args.prec - 1) + \
                    math.pow(2, args.prec - 2)))

print('approximate square root of %d:' % number)
sqrt = sqrt_approximate(number, (number + 1) / 2)
if args.verbose:
    print('----')
print(sqrt)
print('absolute error: %f' % (math.sqrt(number) - float(sqrt)))
print('relative error: %f' % (float(sqrt) / math.sqrt(number) - 1))
