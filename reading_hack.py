import pyautogui as pag
import time

def find_mouse_pointer_for_debug():
    while True:
        print(pag.position())
        time.sleep(0.5)

def mouse_click(x,y):
    pag.moveTo(x,y)
    time.sleep(0.05)
    pag.click()


## start lesson 742,280
def base_lesson():
    mouse_click(742,280)
    time.sleep(0.5)
    for _ in range(10):
        mouse_click(842,1026)
    mouse_click(764,1077)

    for _ in range(10):
        mouse_click(254,979)
        mouse_click(361,1015)
        mouse_click(326,1051)
        mouse_click(307,1084)
    mouse_click(764,1077) #next

def test_train():
    mouse_click(749,443)
    mouse_click(764,1077) #next
    for _ in range(10):
        mouse_click(385,1095)

        mouse_click(764,1077)
        mouse_click(553,792)

    mouse_click(337,724)

    for _ in range(10):
        mouse_click(385,1095)

        mouse_click(764,1077)
        mouse_click(553,792)

## MAIN
#find_mouse_pointer_for_debug()
mouse_click(528,808)
base_lesson()
test_train()

