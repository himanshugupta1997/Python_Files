# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 00:48:34 2018

@author: Devanshu
"""
def qsort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    l = [x for x in arr if x<pivot]
    e = [x for x in arr if x==pivot]
    r = [x for x in arr if x>pivot]
    return qsort(l)+e+qsort(r)

arr = [4,2,1,3]
print([(i,x) in enumerate(arr)])
