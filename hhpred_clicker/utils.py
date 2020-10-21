import time
import pyautogui
import pyperclip

from config import *

def submit(message):
    time.sleep(0.5)
    pyautogui.doubleClick(TEXTBOX)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyperclip.copy(message) 
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.5)
    pyautogui.press('\t')
    pyautogui.press('end')
    time.sleep(0.3)
    pyautogui.click(SUBMIT)
    time.sleep(3)
    pyautogui.press('home')
    time.sleep(0.7)
    pyautogui.click(INPUT)
    
    return None

def downloads():
    time.sleep(0.5)
    pyautogui.click(ELEMENT)
    time.sleep(2)
    pyautogui.click(DOWNLOAD)
    time.sleep(5)
    pyautogui.click(CLOSE)
    time.sleep(0.5)
    
    
def final_downloads():
    time.sleep(0.5)
    pyautogui.click(FINAL_ELEMENT)
    time.sleep(2)
    pyautogui.click(DOWNLOAD)
    time.sleep(5)
    pyautogui.click(FINAL_CLOSE)
    time.sleep(0.5)