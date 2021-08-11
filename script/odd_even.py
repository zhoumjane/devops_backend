# -*- coding: utf-8 -*-
import random
import time
def sort(nums):
    odd = None
    even = None
    for i in range(len(nums)-1):
        if nums[i]%2 == 1:
            if not odd:
                if even:
                    nums[i], nums[even] = nums[even], nums[i]
                    odd = even
                else:
                    odd = i
            elif even:
                nums[i], nums[even] = nums[even], nums[i]
                odd = even
                even = odd + 1
            else:
                pass
        else:
            if not even:
                even = i


# def sort(alist):
#     if int(len(alist)) <= 1:
#         print('1111111')
#         return 0
#     m = 0
#     n = int(len(alist))
#     i = 0
#     result = []
#     for i in range(0, n):
#         result.append(alist[i])
#         i += 1
#     for i in range(0, n):
#         if (alist[i] % 2) == 0:
#             result[n-1] = int(alist[i])
#             n -= 1
#         else:
#             result[m] = int(alist[i])
#             m += 1
#     print(result)
#     return 0

if __name__ == "__main__":
    # nums = [1,2,3,4,5,3,6,9,2,4,6,9,1,0,12]
    nums = []
    for i in range(1000000):
        nums.append(random.randint(1, 100))
    start_time = time.time()
    sort(nums)
    end_time = time.time() - start_time
    print("cost time: %ss" % (end_time))

