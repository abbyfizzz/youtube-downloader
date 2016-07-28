import os,re
import urllib.request as ur

data =ur.urlopen("http://www.youtube.com/get_video_info?&video_id=WEeqHj3Nj2c")
text=data.read()
text=str(text)
dt=re.split(r'[&]',text)
#print(type(text))
for f in dt:
    print(f,"\n")



#fil = open("text.txt", "rb+")
#st =fil.read()
#print(st)
#fil.close()
