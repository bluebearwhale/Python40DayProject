import pyautogui
import pyperclip
import time
import os
import threading

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def send_message(send=None):
    if send is None:
        send="이 메세지는 자동으로 보내는 메세지입니다."
    

    picPosition=pyautogui.locateOnScreen('pic1.png')
    print(picPosition)

    if picPosition is None:
        picPosition=pyautogui.locateOnScreen('pic2.png')
        print(picPosition)
    if picPosition is None:
        picPosition=pyautogui.locateOnScreen('pic3.png')
        print(picPosition)

    clickPosition=pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)
    pyperclip.copy(send)
    pyautogui.hotkey("ctrl","v")
    time.sleep(1.0)
    pyautogui.write(["enter"])
    time.sleep(1.0)
    pyautogui.write(["escape"])
    time.sleep(1.0)
    
threading.Thread(target=send_message).start()
#send_message()

