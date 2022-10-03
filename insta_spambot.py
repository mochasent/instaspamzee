import pyautogui
import time

text = open('zie.txt', 'r')
time.sleep(1)

for word in text:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(1)
