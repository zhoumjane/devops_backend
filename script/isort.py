# -*- coding: utf-8 -*-

import time, random
def isort(i_list):
    for i in range(1, len(i_list)):
        for j in range(i,0, -1):
            if i_list[j] < i_list[j-1]:
                i_list[j], i_list[j-1] = i_list[j-1], i_list[j]
            else:
                break

if __name__ == "__main__":
    alist = []
    for i in range(50000):
        alist.append(random.randint(1, 100))
    start_time = time.time()
    isort(alist)
    end_time = time.time() - start_time
    print("cost time: %ss" % (end_time))