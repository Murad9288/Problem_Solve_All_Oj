#!/bin/python3

import math
import os
import random
import re
import sys



from collections import Counter
for i in Counter(sorted(input())).most_common(3):
    print(*i)
