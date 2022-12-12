import pyautogui
import time

for i in range(5):
  tt = time.localtime(t)
  now=str(tt.tm_year)+"/"+str(tt.tm_mon)+"/"+str(tt.tm_mday)+"_"+str(tt.tm_hour)+":"+str(tt.tm_min)+":"+str(tt.tm_sec)
  myScreenshot = pyautogui.screenshot()
  myScreenshot.save(home/E94116130/introduction_to_computers_labs/secret.now.png')
  sleep(2)