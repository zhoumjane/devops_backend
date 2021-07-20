# -*- coding: utf-8 -*-

# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

import time

def compute():
    for a in range(1000):
        for b in range(1000-a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a, b, c)

if __name__ == "__main__":

    start_time = time.time()
    compute()
    cost_time = time.time() - start_time
    print("cost_time: %fs" % cost_time)

