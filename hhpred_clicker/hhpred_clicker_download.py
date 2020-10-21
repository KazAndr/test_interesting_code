import time
import pyautogui

from config import *
from utils import downloads, final_downloads()


element_number = pyautogui.prompt('How many element are for downloads?')
element_number = int(element_number)
user_answer = pyautogui.confirm('Run the clicker for downloads?')
for i in range(element_number-1):
    downloads()
final_downloads()