import math
import os
import random
import re
import sys

def flippingBits(n):
    example = 4294967295
    # ^ = bitwise XOR
    return n ^ example
if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(flippingBits(n))
        
