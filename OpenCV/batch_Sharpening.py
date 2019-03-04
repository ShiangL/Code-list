##影像銳利化
import os
import cv2
import numpy as np

def sharpening():
    
    for i in range (len(In)):
        img= cv2.imdecode(np.fromfile(Inpath+"\\"+str(In[i]), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        winName="PreView press ESC to exit"
        cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
        kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], np.float32)
        dst=cv2.filter2D(img,-1, kernel=kernel)
        oPath1=Oupath+"\\"+"sharpening"+str(In[i])
        cv_imwrite(oPath1, dst)
    print("批次處裡完成")
    selection() 

def blurry():
    
    for i in range (len(In)):
        img= cv2.imdecode(np.fromfile(Inpath+"\\"+str(In[i]), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        winName="PreView press ESC to exit"
        cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
        kernel=np.ones((5,5),np.float32)/25
        dst=cv2.filter2D(img,-1, kernel=kernel)
        oPath1=Oupath+"\\"+"blurry"+str(In[i])
        cv_imwrite(oPath1, dst)
    print("批次處裡完成")
    selection() 
    
def cv_imwrite(oPath1, dst):
    cv2.imencode('.jpg', dst)[1].tofile(oPath1)

def selection():
    ch=int(input("(1)影像銳利化(2)影像模糊化(3)離開\n"))
    if (ch==1): 
        sharpening()
        
    elif (ch==2):
        blurry()
    
    elif (ch==3):
        quit()
        
if __name__=="__main__":
    Inpath=input("請輸入圖檔路徑 (ex:C:\\image2):\n")
    Oupath=input("請輸入欲存檔路徑 (ex:C:\\image2):\n")
    In=os.listdir(Inpath)
    out=os.listdir(Oupath)
    selection()