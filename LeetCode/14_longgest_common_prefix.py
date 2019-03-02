# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:36:05 2019

@author: USER

14_longgest_common_prefix.py
題目: Write a function to find the longest common prefix string amongst an array of strings.
構思: 找出字串中最常共同的自首
     1.設定空串列比對，比對完存入
"""
x=["abcggh", "abcttyu", "abcppo"];
a1=[]
#for i in range (4):
print(str(x[0]))
s=str(x[0])
b=str(x[1])
if (str(s[i])=str(b[i])):
a1.append(str(x[0]))

print(len(str(x[0])))  

    print(a1);
    
print(x[0])
print(x[1])
print(x[2])

##______________________________________

#class Solution:
#    def longestCommonPrefix(self, strs):
#        """
#        :type strs: List[str]
#        :rtype: str
#        """
#        if len(strs) == 0:
#            return '' 
#        res = ''
#        strs = sorted(strs)
#        print(strs)
#        for i in strs[0]:
#            if strs[-1].startswith(res+i):
#                res += i
#                print(res)
#                print(strs[-1].startswith(res+i))
#            else:
#                break
#        return res
#    
#callFun=Solution();
#a=["abcggh", "abcttyu", "abcppo"]
#test=callFun.longestCommonPrefix(a);
#print(test)





















