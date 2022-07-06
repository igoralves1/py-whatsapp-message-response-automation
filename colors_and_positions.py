from numpy import true_divide
import pyautogui as pt
from time import sleep

while True:
    posXY = pt.position()
    print(posXY)
    print(posXY[0])
    print(posXY[1])
    # print(posXY,pt.pixel(posXY[0],posXY[1]))
    sleep(1)
    if posXY[0] == 0:
        break
