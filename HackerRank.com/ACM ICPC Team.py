#!/bin/python3

import math
import os
import random
import re
import sys


def acmTeam(topic):
    li_1 = []
    for i in range(len(topic)):
        t = set()
        for j in range(len(topic[i])):
            if topic[i][j] == '1':
                t.add(j)
        li_1.append(t)

    li_2 = []
    for i in range(len(li_1)):
        for j in range(i + 1, len(li_1)):
            t = li_1[i] | li_1[j]
            li_2.append(len(t))
    m = max(li_2)
    return (m, li_2.count(m))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)
    for res in result:
        print(res)
