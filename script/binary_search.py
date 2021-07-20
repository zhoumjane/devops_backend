# -*- coding: utf-8 -*-

def binary_search(b_list, value):
    if len(b_list) == 1:
        if b_list[0] == value:
            return True
        else:
            return False
    mid = len(b_list) // 2
    if b_list[mid] > value:
        b_list = b_list[:mid]
        return binary_search(b_list, value)
    elif b_list[mid] < value:
        b_list = b_list[mid+1:]
        return binary_search(b_list, value)
    else:
        return True

if __name__ == "__main__":
    b_list = [1, 2, 3, 4, 8, 3, 1, 4, 9, 12, 55, 23, 49, 5, 21, 33]
    value = 8
    IsFound = binary_search(b_list, value)
    print(IsFound)
    print(value)

