import pyautogui as pag
import time
from PIL import ImageGrab
from PIL import Image
import cv2
import numpy as np
import pyocr

engines = pyocr.get_available_tools()
engine = engines[0]

def find_mouse_pointer_for_debug():
    while True:
        print(pag.position())
        time.sleep(0.1)

def mouse_click(x,y):
    pag.moveTo(x,y)
    time.sleep(0.1)
    pag.click()

def click_a():
    mouse_click(177,976)

def click_b():
    mouse_click(388,1014)

def click_c():
    mouse_click(236,1053)

def click_d():
    mouse_click(233,1087)

# cap (234,510) (695 , 614)

def pil2cv(image):
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image

## MAIN
#find_mouse_pointer_for_debug()


img = ImageGrab.grab()

# スクリーンショットをMAT型に変換
screen_shot = pil2cv(img)
cv2.imwrite('new_img.jpg', screen_shot)
q_img = screen_shot[1030:1300,300:1500]
cv2.imwrite('q_img.jpg', q_img)


# OCRエンジンを取得
txt_1 = engine.image_to_string(Image.open('q_img.jpg'), lang="eng")
print(txt_1)


