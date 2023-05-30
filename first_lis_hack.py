import numpy as np
import cv2

def pil2cv(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:
        pass
    elif new_image.shape[2] == 3:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image

from PIL import ImageGrab

img = ImageGrab.grab()

# スクリーンショットをMAT型に変換
screen_image = pil2cv(img)
## 透過

new_img = screen_image[1000:1900 , 3200:4600]

# ファイルに保存
cv2.imwrite('new_img.jpg', new_img)

import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda")

raw_image = Image.open('new_img.jpg').convert('RGB')
#raw_image = Image.open('src.png').convert('RGB')

# conditional image captioning
text = "a photography of"
inputs = processor(raw_image, text, return_tensors="pt").to("cuda")

out = model.generate(**inputs, max_new_tokens=100)
print(processor.decode(out[0], skip_special_tokens=True))

# unconditional image captioning
inputs = processor(raw_image, return_tensors="pt").to("cuda")

out = model.generate(**inputs , max_new_tokens=100)
caption = processor.decode(out[0], skip_special_tokens=True)
print(caption)


#----

no_1_img = screen_image[2550:2650 , 2650:3300]
cv2.imwrite('1.jpg', no_1_img)

no_2_img = screen_image[2650:2700 , 2650:3300]
cv2.imwrite('2.jpg', no_2_img)

no_3_img = screen_image[2700:2800 , 2650:3300]
cv2.imwrite('3.jpg', no_3_img)

no_4_img = screen_image[2800:2900 , 2650:3300]
cv2.imwrite('4.jpg', no_4_img)

import pyocr
# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

txt_1 = engine.image_to_string(Image.open('1.jpg'), lang="eng")
txt_2 = engine.image_to_string(Image.open('2.jpg'), lang="eng")
txt_3 = engine.image_to_string(Image.open('3.jpg'), lang="eng")
txt_4 = engine.image_to_string(Image.open('4.jpg'), lang="eng")

chat_gpt_txt = "Choose the word or phrase that best describes the image caption.\n"
chat_gpt_txt += '[caption]: ' + caption + '\n'
chat_gpt_txt += '[choices]: \n'
chat_gpt_txt += '1. ' + txt_1 + '\n'
chat_gpt_txt += '2. ' + txt_2 + '\n'
chat_gpt_txt += '3. ' + txt_3 + '\n'
chat_gpt_txt += '4. ' + txt_4 + '\n'


import openai
openai.api_key = "OPENAI-KEY"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are chatgpt"},
        {"role": "user", "content": "Choose the word or phrase that best describes the image caption.\n[caption]: a close up of a car with a hood on a white background\n[choices]: \n1. boarding\n2. watering\n3. addressing\n4. vehicle"},
        {"role": "assistant", "content": "4. vehicle"},
        {"role": "user", "content": chat_gpt_txt},
    ]
)

#返信のみを出力
print(" ----ChatGPT---- ")
gpt_res = response["choices"][0]["message"]["content"]
print(gpt_res)

import pyautogui
import time

def click_chice(no):
  if no == 1:
    pyautogui.moveTo(2743, 2591, duration=1)
  elif no == 2:
    pyautogui.moveTo(2743, 2668, duration=1)
  elif no == 3:
    pyautogui.moveTo(2743, 2741, duration=1)
  elif no == 4:
    pyautogui.moveTo(2743, 2812, duration=1)
  
  time.sleep(0.1)
  pyautogui.click()

if '1' in gpt_res:
   click_chice(1)
elif '2' in gpt_res:
   click_chice(2)
elif '3' in gpt_res:
   click_chice(3)
elif '4' in gpt_res:
   click_chice(4)

pyautogui.moveTo(1781, 2491, duration=1)
time.sleep(0.1)
pyautogui.click()