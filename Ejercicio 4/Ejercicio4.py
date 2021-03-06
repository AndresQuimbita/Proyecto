'''
4. You have observations of  ๐+๐  6-sided dice rolls with each face numbered from  1  to  6 .  ๐  of the observations went missing, and you only have the observations of  ๐  rolls. Fortunately, you have also calculated the average value of the  ๐+๐  rolls.
You are given an integer array rolls of length  ๐  where  ๐๐๐๐๐ [๐]  is the value of the  ๐๐กโ  observation. You are also given the two integers  ๐๐๐๐  and  ๐ .

Return an array of length  ๐  containing the missing observations such that the average value of the  ๐+๐  rolls is exactly  ๐๐๐๐ . If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of  ๐  numbers is the sum of the numbers divided by  ๐ .

Note that  ๐๐๐๐  is an integer, so the sum of the  ๐+๐  rolls should be divisible by  ๐+๐ .

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
'''


def find_observations(array, m, n):
    '''
    Calculate the lost observation of a python list with length n from a python list with length m and a mean
    '''
    result = []
    sum_lost_observation = m*(len(array)+n) - sum(array)
    if sum_lost_observation > 6*n or sum_lost_observation < n:
        if sum_lost_observation == 0:
            return [0 for i in range(n)]
        return []
    for i in range(n):
        a = int(sum_lost_observation/n)
        result.append(a)
    if sum_lost_observation % n != 0:
        result[-1] += sum_lost_observation % n
    return result
