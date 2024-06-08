import pyautogui
from PIL import Image,ImageGrab
import time
from numpy import asarray
# pyautogui.keyDown('k')
# pyautogui.keyDown('r')
# pyautogui.keyDown('i')
# pyautogui.keyDown('s')
# pyautogui.keyDown('t')
# pyautogui.keyDown('a')
# pyautogui.keyDown('l')


def hit(key):
     pyautogui.keyDown(key)
     return

def isCollide(data):
    for i in range(500,520):
        for j in range(233,270):
            if data[i,j] < 100:
                hit("down")
                return 

    for i in range(200,280):
            for j in range(363,450):
               if data[i,j] < 100:
                    hit("up")
                    return 
    return 


if __name__=='__main__':
    print("Dino Game about to start in 3 seconds")
    time.sleep(3)
    hit("up")  #auto start
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)
    # if isCollide(data):
    #     pyautogui.keyDown('up')
    #print(data)
    # print(asarray(image))
    # # for zoom 100% dinosaur game,capturing cactus
    # for i in range(500,520):
    #     for j in range(290,310):
    #         data[i,j]=0

    # # for birds
    # for i in range(500,520):
    #     for j in range(233,270):
    #         data[i,j]=0


    image.show()


