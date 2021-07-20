# -*- coding: utf-8 -*-

import random
import time
def shell_sort(alist):
    n = len(alist)
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap
        gap = gap // 2

if __name__ == "__main__":
    alist = []
    for i in range(50000):
        alist.append(random.randint(1, 100))
    start_time = time.time()
    shell_sort(alist)
    end_time = time.time() - start_time
    print("cost time: %ss" % (end_time))

