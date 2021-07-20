def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二分分解
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    return merge(left, right)
    # 合并
    # return merge(left, right)

def merge(left, right):
    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    #left与right的下标指针
    result = []
    # if left[0] > right[len(right)-1]:
    #     result = right + left
    #     return result
    # if left[len(left)-1] < right[0]:
    #     result = left + right
    #     return result
    r, l = 0, 0
    while r < len(right) and l < len(left):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r +=1
    return result + left[l:] + right[r:]



alist = [54,26,93,17,77,31,44,55,20]
sorted_alist = merge_sort(alist)
print(sorted_alist)