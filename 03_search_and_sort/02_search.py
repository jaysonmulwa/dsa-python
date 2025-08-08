"""
Search Algorithms
========================
Search algorithms are used to find a specific element or set of elements within a data structure, such as an array or a list. The efficiency of search algorithms is often analyzed using Big O notation, which describes their time complexity.
Common search algorithms include:
- Linear Search: 
    A simple algorithm that checks each element in the list sequentially until the desired element is found or the end of the list is reached. 
    It has a time complexity of O(n).
- Binary Search: 
    A more efficient algorithm that works on sorted lists. 
    It repeatedly divides the search interval in half until the desired element is found or the interval is empty. 
    It has a time complexity of O(log n).
- Interpolation Search: 
    An improved version of binary search that estimates the position of the desired element based on the values of the elements in the list.
    It works best on uniformly distributed data and has a time complexity of O(log log n)
    in the best case, but can degrade to O(n) in the worst case.
- Exponential Search:
    An algorithm that first finds a range where the desired element may exist and then performs a binary search within that range. 
    It has a time complexity of O(log n).

"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5