'''
6. Given an array of integers  𝑎𝑟𝑟 , return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo  109+7 .

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
'''


def impar_odd_sum(array):
    '''
    Calculate and return the number of all the impar odd sum from sublist of a python list []
    '''
    odd = 0
    arr = []
    result = []
    for i in range(len(array)+1):
        for j in range(i):
            arr.append(array[j:i])
    for i in arr:
        odd = 0
        for j in range(len(i)):
            odd += i[j]
        if (odd % 2) != 0:
            result.append(i)
    ans = len(result)
    return ans % (10**9 + 7)
