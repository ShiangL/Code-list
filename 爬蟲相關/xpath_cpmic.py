from lxml import etree
import re
import requests

hea = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko)Chrome/51.0.2704.63 Safari/537.36'}  
r = requests.get('http://jp.tingroom.com/yuedu/yd300p/', headers = hea)

url='https://www.jkforum.net/thread-10168523-1-1.html'
html=requests.get(url)
S1=etree.HTML(html.text)
p=0
print(html.text)
print(S1)
for quote in S1.xpath('//*[@id="postmessage_122350027"]/img'): #Xpath取值
    print (quote.attrib)
    print ("Downloading:"+quote.attrib['src'])
    pic=requests.get(quote.attrib['src'])
    fp = open('source\\' + str(p)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    p+=1
print("載入完成")
