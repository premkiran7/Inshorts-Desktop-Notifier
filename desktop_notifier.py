import time
import notify2
import urllib2
import json
from bs4 import BeautifulSoup

#ICON_PATH = "/home/premkiran/Inshorts-Desktop-Notifier/Inshorts.png"

categories = ['','national','business','sports','world','politics','technology','startup','entertainment','miscellaneous','hatke','science','automobile']
    
index = 0
    
while(1):

   page1 = urllib2.urlopen('http://127.0.0.1:5000/news?category=' + categories[index])
    
   temp = json.loads(page1.read())

   newsitems = temp['data']

   # initialise the d-bus connection
   notify2.init("News Notifier")

   # create Notification object
   n = notify2.Notification(None)#, icon = ICON_PATH)

   # set urgency level
   n.set_urgency(notify2.URGENCY_NORMAL)

   # set timeout for a notification
   n.set_timeout(10000)

   for newsitem in newsitems:

      # update notification data for Notification object
      n.update(newsitem['title'], newsitem['content'])

      # show notification on screen
      n.show()

      # short delay between notifications
      time.sleep(15)
  
   index = index + 1    
   
   if index == 13:
      index = 0
