# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:43:29 2022

@author: Akshatha
"""
import numpy as np
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper

@time_it
def linear_search(arr, num):
    for idx,element in enumerate(arr):
        if num == element:
            return idx
    return -1

@time_it
def binary_search(arr, num):
    low_idx = 0
    high_idx = len(arr)-1
    while low_idx <= high_idx:
        mid_idx = (high_idx+low_idx)//2
        if arr[mid_idx] == num:
            return mid_idx
        if num > arr[mid_idx]:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1
    return -1

# try 1 - doesn't handle invalid input
def binary_search_recursion(arr, num):
    low_idx = 0
    high_idx = len(arr)-1
    mid_idx = (high_idx+low_idx)//2
    # if high_idx <= low_idx:
    #     return -1
    if arr[mid_idx] == num:
        return mid_idx
    elif num > arr[mid_idx]:
        return mid_idx + 1+binary_search_recursion(arr[mid_idx+1:], num)
    else:
        return binary_search_recursion(arr[:mid_idx], num)
    
def binary_search_recursive(arr,num,low_idx,high_idx):
    mid_idx = (high_idx+low_idx)//2
    if arr[mid_idx] == num:
        return mid_idx
    if high_idx <= low_idx:
        return -1
    if num > arr[mid_idx]:
        low_idx = mid_idx + 1
    else:
        high_idx = mid_idx - 1
    return binary_search_recursive(arr,num,low_idx,high_idx)

def find_all_occurences(arr, num):
    index = binary_search(arr, num)
    list_idx = [index]
    
    i = index-1
    while i >=0:
        if arr[i] == num:
            list_idx.append(i)
        else:
            break
        i = i-1
    
    i = index +1 
    while i < len(arr):
        if arr[i] == num:
            list_idx.append(i)
        else:
            break
        i = i+1
        
    return sorted(list_idx)
            
if __name__ == '__main__':
    sorted_arr = range(100001)
    num_to_find = 100000
    index = linear_search(sorted_arr, num_to_find)
    print('linear search output:',index)
    index = binary_search(sorted_arr, num_to_find)
    print('binary search output:',index)
    index = binary_search_recursive(sorted_arr,num_to_find,0,len(sorted_arr)-1)
    print('binary search through recursion output:',index)
    # doesn't handle invalid input
    index = binary_search_recursion(sorted_arr, num_to_find)
    print('binary search through recursion output:',index)
    
    arr = [1,3,4,5,8,10,12,14,16,16,16,17,18,20,21,24]
    print('all occurences:',find_all_occurences(arr,16))