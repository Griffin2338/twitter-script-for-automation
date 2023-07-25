from sys import maxsize
from unicodedata import name
import twint
import os
import pandas as pd
import re 
import csv
import os
import win32com.client
from icrawler.builtin import GoogleImageCrawler
from photoshop import Session
from PIL import Image
import os.path
from os import path


space="❗️"
dict = {"▪": "", "#": "", "â": "", '"': "", "📌": "", "🔥": ":","🚨":"","💢":"","👇":""}
translationTable = str.maketrans(dict)





psApp = win32com.client.Dispatch("Photoshop.Application")
psApp.Open(r"IT SHOULD BE UR .PSD FILE PATH")
doc = psApp.Application.ActiveDocument
layer_facts = doc.ArtLayers["a"]

text_of_layer = layer_facts.TextItem
filePath = 'tweets.csv'
mydict =[]
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")

# Configure
c = twint.Config()
c.Username = "USERNAME OF TWITTER ACCOUNT WHERE U WANT TO GET TWITS"
c.Limit = 1
c.Videos=False
c.Images=False
# Run

c.Output = "tweets.csv"

c.Store_csv=True
c.Custom["tweet"] = ["tweet"]
twint.run.Search(c)


a=0;
b=0;
with open('tweets.csv', encoding="utf8") as file:
    reader = csv.reader(file)

          
    for row in reader:
        if (row[0] != 'tweet'):
          s3 = re.sub(r"http\S+", "", row[0])
          s3 = re.sub(r"http\S+", "", row[0])
          s3 = s3.translate(translationTable)
          s3=s3.replace("❗️","!!!")
          s3=s3.replace("🇹🇷","")
          s3=s3.replace("◾️","")
          s3=s3.replace("▪","")
          s3=s3.replace("▪️","")

          text_of_layer.contents = s3
          text_of_layer.position=[-95,400]
          mydict.append({s3})

          google_Crawler = GoogleImageCrawler(storage = {'root_dir': r''+str(b)+""})
          google_Crawler.crawl(keyword = s3[0:100], max_num = 2,max_size=[1000,1000],min_size=[500,500])
          b=b+1
          
          with Session() as ps:
             for layer in ps.active_document.layers:
                 if layer.name =="000001" or layer.name =="000002":
                     ps.active_document.activeLayer = layer
                     replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
                     desc = ps.ActionDescriptor
                     idnull = ps.app.charIDToTypeID("null")
                     if(path.exists("IT SHOULD BE UR PATH WHERE THIS TWIT.PY FILE EXIST"+str(a)+"/000001.jpg")):
                       new_image = "IT SHOULD BE UR PATH WHERE THIS TWIT.PY FILE EXIST"+str(a)+"/000001.jpg"
                       desc.putPath(idnull, new_image) 
                       ps.app.executeAction(replace_contents, desc) 
                       options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
                       options.Format = 13   # PNG Format
                       options.PNG8 = False  # Sets it to PNG-24 bit                    
                       pngfile = "IT SHOULD BE UR PATH WHERE THIS TWIT.PY FILE EXIST"+str(a)+".png"
                       doc.Export(ExportIn=pngfile, ExportAs=2, Options=options)
                     if(path.exists("IT SHOULD BE UR PATH WHERE THIS TWIT.PY FILE EXIST"+str(a)+"/000002.jpg")):
                       #img=Image.open('C:/Users/YUNUS EMRE KAYA/Desktop/twit/'+str(a)+'/000002.jpg')
                       #d=img.convert("YCbCr",palette=Image.LANCZOS, colors=1)
                       #d.save('C:/Users/YUNUS EMRE KAYA/Desktop/twit/'+str(a)+'/000002.jpg')
                       new_image = "IT SHOULD BE UR PATH WHERE THIS TWIT.PY FILE EXIST"+str(a)+"/000002.jpg"
                       desc.putPath(idnull, new_image) 
                       ps.app.executeAction(replace_contents, desc) 
                       options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
                       options.Format = 13   # PNG Format
                       options.PNG8 = False  # Sets it to PNG-24 bit                    
                       pngfile = "IT SHOULD BE UR PATH WHERE THIS TWIT.PY FILE EXIST"+str(a)+str(a)+str(a)+".png"
                       doc.Export(ExportIn=pngfile, ExportAs=2, Options=options)
                     a=a+1
                     

  

                     



with open('tweets.csv', 'w', encoding='UTF8', newline='') as f:
      writer = csv.writer(f)
      writer.writerows(mydict)






