import time
import pyautogui

def screenshot():
    name=int(round(time.time()*1000))
    name='python\screenshots data/{}.png'.format(name)
    time.sleep(5)
    img= pyautogui.screenshot(name)
    img.show()


screenshot()