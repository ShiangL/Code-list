# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:17:25 2019

@author: USER

66. Plus One

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.

構思: +1 進位
"""
#x=[9,9,9]
#str1=""
#list2=[]
#for i in range (len(x)):
#    str1=str1+str(x[i])
#list1=list(str(int(str1)+1))
#for j in range (len(list1)):
#    list2.append(int(list1[j]))
#print(list2)

#class Solution():
#    def plusOne(self,x):
#        str1=""
#        list2=[]
#        for i in range (len(x)):
#            str1=str1+str(x[i])
#        list1=list(str(int(str1)+1))
#        for j in range (len(list1)):
#            list2.append(int(list1[j]))
#        return list2
###_____________________________________________
#x=[9,9,9]  #任意輸入測試值
#callFun=Solution();
#test= callFun.plusOne(x)
#print(test)

##(另解)__________________________________

class Solution():
    def plusOne(digits):
        num = 0
        for i in range(len(digits)):
        	num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]

#x=[1,9,9]  #任意輸入測試值
callFun=Solution();
test= callFun.plusOne("123456")
print(test)


