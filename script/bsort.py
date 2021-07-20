# -*- coding: utf-8 -*-

def bsort(b_list):
    for i in range(1,len(b_list)):
        for j in range(len(b_list)-i):
            if b_list[j] > b_list[j+1]:
                b_list[j], b_list[j+1] = b_list[j+1], b_list[j]

if __name__ == "__main__":
    b_list = [1, 2, 3, 4, 8, 3, 1, 4, 9, 12, 55, 23, 49, 5, 21, 33]
    bsort(b_list)
    print(b_list)