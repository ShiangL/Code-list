## 時間

import time as t 

t=t.localtime(t.time())
print(t.tm_year);
print(t.tm_mon);
print(t.tm_mday);

print("%d:%d:%d" % (t.tm_hour, t.tm_min, t.tm_sec))

#星期

import time as t 

t=t.localtime(t.time())
w=t.tm_wday

if (w==0):
    print("今天是星期一");

if (w==1):
    print("今天是星期二");
    
if (w==2):
    print("今天是星期三");
    
if (w==3):
    print("今天是星期四");
    
if (w==4):
    print("今天是星期五");
    
if (w==5):
    print("今天是星期六");
    
if (w==6):
    print("今天是星期日");
    
##本月天數

import time as t
import calendar as c

time1=t.localtime(t.time());
y=time1.tm_year
m=time1.tm_mon

print("%d年%d月" % (y,m))

mrange=c.monthrange(y,m)

num=mrange[1]
print("共有%d 天" % num)


























    

