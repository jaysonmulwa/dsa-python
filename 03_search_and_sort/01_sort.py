"""
Sorting Algorithms
========================
Sorting algorithms are used to arrange the elements of a list or array in a specific order, typically in ascending or descending order. The efficiency of sorting algorithms is often analyzed using Big O notation, which describes their time complexity.
Common sorting algorithms include:
- Bubble Sort: 
    A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    It has a time complexity of O(n^2).

- Selection Sort: 
    Another simple comparison-based algorithm that divides the list into a sorted and an unsorted part. 
    It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part. 
    It also has a time complexity of O(n^2).

- Insertion Sort: 
    A comparison-based algorithm that builds a sorted array one element at a time. 
    It works by taking an element from the unsorted part and inserting it into the correct position in the sorted part. Its time complexity is O(n^2).

- Merge Sort: 
    A divide-and-conquer algorithm that divides the list into two halves, sorts each half recursively, and then merges the sorted halves. 
    It has a time complexity of O(n log n).

- Quick Sort: 
    Another divide-and-conquer algorithm that selects a 'pivot' element and partitions the list into two parts: elements less than the pivot and elements greater than the pivot. 
    It then sorts each part recursively. Its average time complexity is O(n log n), but in the worst case, it can degrade to O(n^2).

- Heap Sort: 
    A comparison-based algorithm that uses a binary heap data structure to sort the elements. 
    It first builds a max heap from the input data and then repeatedly extracts the maximum element to build the sorted array. 
    Its time complexity is O(n log n).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array using Bubble Sort:", arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array using Selection Sort:", arr)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array using Insertion Sort:", arr)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Sorted array using Merge Sort:", arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Sorted array using Quick Sort:", sorted_arr)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) 

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
