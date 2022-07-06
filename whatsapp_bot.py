import pyautogui as pt
import paperclip as pc
# from pynput.mouse import Controller, Button
from time import sleep

# mouse = Controller()

class WhatsApp:
    def __init__(self, speed=5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    def nav_green_dot(self):
        try:
            # position = pt.locateOnScreen('clip_pic.png', confidence = .7)
            # position = pt.locateOnScreen('clip_pic.png')
            # print(position)
            print(pt.locateOnScreen('tt2.png'))
            
            # pt.moveTo(position[0:2], duration = self.speed)
            # pt.moveRel(-100, 0, duration = self.speed)
        except Exception as e:
            print ('Exception (nav_green_dot): ', e)

wa_bot = WhatsApp(speed = .5, click_speed = .4)
sleep(5)
wa_bot.nav_green_dot()                