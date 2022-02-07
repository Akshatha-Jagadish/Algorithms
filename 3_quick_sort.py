# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:47:18 2022

@author: Akshatha
"""

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]
   
# divide and conquer - Hoare partition
def quick_sort_hoare(arr,pivot,limit):
    start = pivot
    end = limit
    while True:
        while arr[start] <= arr[pivot]:
            if start >= limit:
                break
            start = start + 1
        while arr[end] > arr[pivot]:
            if end <= 0:
                break
            end = end-1
        if start >= end:
            swap(end,pivot,arr)
            break
        swap(start,end,arr)
    
    if end-1 > pivot:
        quick_sort_hoare(arr,pivot,end-1) # left partition
    if limit > start:
        quick_sort_hoare(arr,start,limit) # right partition

if __name__ == '__main__':
    arr = [11, 9, 29, 7, 2, 15, 28, 14, 3, 56, 5]
    # arr = [5,10,12,15,20]
    # arr = [10]
    quick_sort_hoare(arr,0,len(arr)-1)
    print(arr)