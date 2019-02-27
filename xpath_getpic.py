from lxml import etree
import re
import requests
url='https://order-system-9527.firebaseapp.com/indexRice.html'
html=requests.get(url)
S1=etree.HTML(html.text)
p=0
# print(html.text)
# print(S1)
for quote in S1.xpath('//*[@id="divRicPic"]/a/img'): #正則表達式
    print (quote.attrib)
    print ("Downloading:"+quote.attrib['src'])
    pic=requests.get("https://order-system-9527.firebaseapp.com//"+quote.attrib['src'])
    fp = open('source\\' + str(p)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    p+=1
print("載入完成")
