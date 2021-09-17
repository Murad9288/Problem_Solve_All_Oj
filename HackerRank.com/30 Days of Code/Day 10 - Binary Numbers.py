#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    c_node = 0
    max_node = 0
    
    while (n>0):
        res = n%2
        if res == 1:
            c_node += 1
            if c_node > max_node:
                max_node = c_node
        else:
            c_node = 0
        n //= 2
    print(max_node)
                
