import pyautogui
import time
import winsound
from PIL import ImageGrab
from functools import partial
import requests
import os

# 螢幕1
#ImageGrab.grab = partial(ImageGrab.grab, bbox =(0, 0, 1920, 1080), all_screens=True)

# 螢幕2
ImageGrab.grab = partial(ImageGrab.grab, bbox =(1920, 0, 3840, 1080), all_screens=True)

def lineNotify(str):
    pyautogui.screenshot('screenshot-tmp.png') # 自動截圖
                           
    headers = {
        "Authorization": "Bearer " + "sV6wBygW6IBNSP5ww9riZOS8n7unF6PG9Wr9M9tBVeK",
    }
     
    params = {"message": str + "警告, 請注意",  # 傳訊息，這邊設定傳success
    }

    files = {'imageFile': open(r'screenshot-tmp.png','rb')} # 傳圖片檔案

    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params, files = files)

    fileTest = "screenshot-tmp.png" # 因為照片在傳出去的時候會鎖死刪不掉，所以要刪前一個檔案
    try: # 防止找不到檔案導致程式停止
        os.remove(fileTest) # 刪除截圖的圖片檔案
    except OSError as e:
        print(e) # 印出錯誤訊息
                      
def get_capslock_state():
    import ctypes
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)

imageArr = ['player.png', 'member.png', 'friend.png', 'player2.png']

while True:
    flag = False
    tmp = ""

    for image in imageArr:
        conf = 1

        if image == "player2.png":
            conf = 0.98

        if image == "member.png":
            conf = 0.99

        location = pyautogui.locateOnScreen(image, confidence = conf)

        if location != None:
            tmp = image
            flag = True


    if flag == True and get_capslock_state() == 0:
        lineNotify(tmp)
        winsound.Beep(600,1000)
    
    print("loop done")
    time.sleep(3)

