# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:24:10 2022

@author: Akshatha
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp  
                swapped = True # to break out if the array is already sorted
        if not swapped:
            break

def bubble_sort_key(arr, key='name'):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1-i):
            if arr[j][key] > arr[j+1][key]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp  
                swapped = True # to break out if the array is already sorted
        if not swapped:
            break

if __name__ =='__main__':
    arr = [3,6,1,8,4,9,45,12,34,21,15,27]
    list_of_dics =[
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(arr)
    print(arr)
    bubble_sort_key(list_of_dics,key='name')
    print(list_of_dics)