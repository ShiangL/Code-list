# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:44:14 2019

@author: USER

Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
click to show spoilers.
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 
when the reversed integer overflows.
構思:字串逆迴圈輸出
"""
#x=1234
#s=str(x)
#b=""
#
#if (x>0):
#    print(s[::-1])
#else:
#    for i in range (len(s)-1,0, -1 ):
#        b=b+str(s[i])
#    print("-" +b)

#class reversed1:
#    def __init__(self, x):
#        self.__x=x;
#        self.__s=str(self.__x);
#        self.__b="";
#        
#    def revfun(self):
#        if (self.__x>0):
#            self.__b=(self.__s[::-1])
#            return self.__b;
#        else:
#            for i in range (len(self.__s)-1,0, -1 ): 
#               self.__b=self.__b+str(self.__s[i])
#            return str("-")+self.__b;
#
#if reversed1.__module__=="__main__":     
#    a=reversed1(123)
#    c=a.revfun()
#    print(c)

##_____________________________________________________________________________    
#            for i in range (0,len(self.__s)): 
#               self.__b=self.__b+str(self.__s[i])
#            return self.__b;  
## 判斷是否溢位
#class Solution(object):
#    def reverse(self, x):
#        """
#        :type x: int
#        :rtype: int
#        """
#      
#        y = int(x) if x > 0 else -x
#        z = 0
#
#        while y > 0:
#            z = z * 10 + y % 10
#            y /= 10
#
#        z = z if x > 0 else -z
#        if z > 0xffffffff or z < -0xffffffff:
#            return 0
#        else:
#            return z    
#if Solution.__module__=="__main__":
#    a=Solution();
#    test=a.reverse(-1234)
#    print(test)       
    
   
##________________________________________________   
    
#x=-1234
#j=""
#if (x>=0):
#    for i in range (len(str(x))):
#        if(int(x/(10**i))>0): 
#            y=x/(10**i) 
#            z=int(y)%10
#            j=j+str(z)
#    print(j)
#else:
#    k=str(x).strip("-")
#    for i in range (len(str(k))):
#        if(int(int(k)/(10**i))>0): 
#            y=int(k)/(10**i) 
#            z=int(y)%10
#            j=j+str(z)
#    print("-"+j)

##_____________________________

#x=-1234
#i=0;
#j=""
##if
#len1=len(str(x));
#while (i<len1):
#    if(int(x/(10**i))>0): 
#        y=x/(10**i) 
#        z=int(y)%10
#        j=j+str(z)
#        i=i+1
#print(j)  
    
##__________________________________
class Solution():
    def reversed1 (self, x):
        self.__x=x;
        self.__j="";
        if (self.__x>=0):
            for i in range (len(str(self.__x))):
                if(int(self.__x/(10**i))>0): 
                    self.__y=self.__x/(10**i) 
                    self.__z=int(self.__y)%10
                    self.__j=self.__j+str(self.__z)
            return self.__j
        else:
            self.__k=str(self.__x).strip("-")
            for i in range (len(str(self.__k))):
                if(int(int(self.__k)/(10**i))>0): 
                    self.__y=int(self.__k)/(10**i) 
                    self.__z=int(self.__y)%10
                    self.__j=self.__j+str(self.__z)
            return "-"+self.__j
        
if Solution.__module__=="__main__":
    a=Solution();
    test=a.reversed1(-1234)
    print(test)     
            

    
    


        
      
        
        
        
        

