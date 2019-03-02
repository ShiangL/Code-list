# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 18:58:21 2019

@author: USER
"""

# S = {1 0 -1 0 -2 2}, and target = 0.

def subfourSum(S, target, start):
    
    q = []
    l = len(S)
    q.append((S[start], start, ([S[start]])))
    result = []
    
    while q:
        tmp_sum, index, sum_list = q.pop()
        
        if len(sum_list) < 4:
            for i in range(index + 1, l):
                
                q.append((tmp_sum + S[i], i, sum_list + [S[i]]))
        
        elif len(sum_list) == 4:
            if tmp_sum == target:
                sr = sorted(sum_list)
                if sr not in result:
                    result.append(sr)
            
        
    
    return result   

def fourSum(S, target):
    r = []
    for i in range(len(S)-4):
        r.append(subfourSum(S, target, i))
        
    return r
        
print (fourSum([1, 0, -1, 0, -2, 2], 0))