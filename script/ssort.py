# -*- coding: utf-8 -*-

def sbort(s_list):
    for i in range(1, len(s_list)):
        min = i - 1
        for j in range(i-1, len(s_list)):
            if s_list[min] > s_list[j]:
                s_list[min], s_list[j] = s_list[j], s_list[min]

if __name__ == "__main__":
    s_list = [1, 2, 3, 4, 8, 3, 1, 4, 9, 12, 55, 23, 49, 5, 21, 33]
    sbort(s_list)
    print(s_list)
