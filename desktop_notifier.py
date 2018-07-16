#coding=utf-8
from googletrans import Translator
import time
import notify2
import urllib2
import json
from bs4 import BeautifulSoup
import datetime
import codecs

# path to notification window icon
ICON_PATH = "/home/user/Downloads/Inshorts-Desktop-Notifier/Inshorts.jpg"

#os.system('python app.py')

categories = ['','national','business','sports','world','politics','technology','startup','entertainment','miscellaneous','hatke','science','automobile']
    
index = 0
    
while(1):

   page1 = urllib2.urlopen('http://127.0.0.1:5000/news?category=' + categories[index])
    
   temp = json.loads(page1.read())

   newsitems = temp['data']

   # initialise the d-bus connection
   notify2.init("News Notifier")

   # create Notification object
   n = notify2.Notification(None, icon = ICON_PATH)

   # set urgency level
   n.set_urgency(notify2.URGENCY_NORMAL)

   # set timeout for a notification
   n.set_timeout(10000)
   
   translator = Translator()
   
   file1 = codecs.open('File1.txt',encoding='utf-8',mode='a')

   for newsitem in newsitems:

      title = translator.translate(newsitem['title'], dest='ta')

      content = translator.translate(newsitem['content'], dest='ta')
      
      # update notification data for Notification object
      #n.update(title.text, content.text) 
      
      file1.write(title.text)
      
      file1.write('\n')
      
      file1.write(newsitem['title'])
      
      file1.write('\n')
      
      file1.write(content.text)
      
      file1.write('\n')
      
      file1.write(newsitem['content'])
      
      file1.write('\n')
      file1.write('\n')
      
      n.update(newsitem['title'], newsitem['content'])
      
      # show notification on screen
      n.show()

      # short delay between notifications
      time.sleep(15)
  
   index = index + 1    
   
   if index == 13:
      index = 0
      
   file1.close()   
