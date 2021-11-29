'''
 1. Given a sorted integer arr $nums$ and three integers $a$, $b$ and $c$, apply a quadratic function of the form $f(x) = ax2 + bx + c$ to each element $nums[i]$ in the arr, and return the arr in a sorted order.


 **Example 1:**
 ```
 Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
 Output: [3,9,15,33]
 ```

 **Example 2:**
 ```
 Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
 Output: [-23,-5,1,7]

```
'''
import ctypes


class Array(object):
    """
    Implementation of the array data structure
    """

    def __init__(self, n, values=None):
        self.item_count = 0
        self.n = n
        self.arr = self._create_array(self.n)
        if values:
            self.initialize_array(values)

    def _create_array(self, n):
        """
        Creates a new array of capacity n
        """
        return (n * ctypes.py_object)()

    def initialize_array(self, values):
        """
        Initialize array
        """
        if self.n != len(values):
            raise ValueError("element count different than capacity")
        for item in values:
            self.arr[self.item_count] = item
            self.item_count += 1

    def list_array(self):
        """
        List elements of the array
        """
        return ", ".join(str(x) if x is not None else '_' for x in self.arr)


def binary_search(arr, val, start, end):
    '''
    Do a binary search to order an array
    '''
    if start == end:
        if arr.arr[start] > val:
            return start
        else:
            return start+1
    if start > end:
        return start

    mid = int((start+end)/2)
    if arr.arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr.arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid


def insertion_sort(arr):
    '''
    Insertion sort that calls binary search to order an array
    '''
    for i in range(1, arr.n):
        val = arr.arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr.arr = arr.arr[:j] + [val] + arr.arr[j:i] + arr.arr[i+1:]
    return arr


def cuadratic_function(self, a, b, c):
    '''
    Calculate the cuadratic value of each element in an array 
    '''
    if self.n == 0:
        return []
    if self.n == 1:
        return [c]
    result = Array(self.n)
    for i in range(self.n):
        result.arr[i] = a*(self.arr[i])**2 + b*(self.arr[i]) + c
    result = insertion_sort(result)
    return result
