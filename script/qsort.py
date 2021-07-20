# -*- coding: utf-8 -*-
import time, random
def qsort(q_list):
    if len(q_list) < 2:
        return q_list
    mid = len(q_list) // 2
    mid_value = q_list[mid]
    del q_list[mid]
    left = []
    right = []
    for i in q_list:
        if i <= mid_value:
            left.append(i)
        else:
            right.append(i)
    return qsort(left) + [mid_value] + qsort(right)




if __name__ == "__main__":
    alist = []
    for i in range(50000):
        alist.append(random.randint(1, 100))
    start_time = time.time()
    new_list = qsort(alist)
    end_time = time.time() - start_time
    print("cost time: %ss" % (end_time))
