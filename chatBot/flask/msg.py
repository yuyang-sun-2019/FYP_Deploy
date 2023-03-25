import os
import sys
os.path.dirname(sys.executable)
#import pyautogui
import pywhatkit
import datetime
# syntax: phone number with country code, message, hour and minutes
now = datetime.datetime.now()
print(now.hour, now.minute+1)
pywhatkit.sendwhatmsg('+65xxxxxxxx', 'I need your repair services',now.hour,now.minute+1,15)
#http://wa.me/86687676
#pywhatkit.sendwhatmsg_instantly(phone_no="<phone-number>",message="Howdy! This message will be sent instantly!",)
