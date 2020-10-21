import os
import time
import glob
import pyautogui
import pyperclip
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys 

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def get_uploaded_list(job_number, nums_seq):
    result = []
    for i in range(1, nums_seq+1):
        driver.get(f'{main_link}{job_number}_{i}')
        try:
            driver.find_element_by_xpath(xpath_input).click()
            time.sleep(2)
            result.append(driver.find_element_by_xpath(xpath_textbox).get_attribute('value'))
        except NoSuchElementException:
            result.append('Error404')
            
    return result


def check_upload(array_1, array_2):
    if len(array_1) == len(array_2):
        result = []
        for idx, items in enumerate(zip(array_1, array_2)):
            if items[0] != items[1]:
                result.append(str(idx+1))
            else:
                continue
    else:
        raise IndexError(
            'Lenght of the first array is not equal the lenght of the second array')
    return result


default_files = sorted(glob.glob('*.xls'))

if len(default_files) == 0:
    default_files.append('Enter a filename here!')
filename = pyautogui.prompt(
    text='Enter the name of a file for analisys:',
    title='File for analisys',
    default=f'{default_files[0]}'
)
table = pd.read_excel(filename, sheet_name='Sheet1')


driver = webdriver.Chrome()
driver.maximize_window() 
driver.implicitly_wait(30) # глобальное время ожидания для всех элементов
# Захдим на сайт
#driver.get("https://toolkit.tuebingen.mpg.de/tools/hhpred")

# Прописываем изначальные пути (полные)
main_link = 'https://toolkit.tuebingen.mpg.de/jobs/'
xpath_cookie = '/html/body/div/div[5]/div[2]/button'
xpath_textbox = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[1]/div/div/div/div[1]/div/fieldset[1]/div/textarea'
xpath_submit = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[1]/fieldset/div/button'
xpath_input = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[1]/ul/li[1]/a'
start_job_aw = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[3]/div/div/button[1]'
full_xpath_num_job = (
    '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[1]/fieldset/div/div/input'
)
# Жамкаем кнопку по поводу cookie-сов
#time.sleep(1)
#driver.find_element_by_xpath(xpath_cookie).click()

input_values = pyautogui.prompt(
    text='Enter the number of job and number of sequences separated by a space (e.g. 123456 50)',
    title='Enter the data',
    default='123456 50'
)
job_number, iterations = input_values.split()
uploads_list = get_uploaded_list(job_number, int(iterations))
try:
    msgs = check_upload(uploads_list, table.aa_sequence)
except IndexError:
    msgs = 'Lenght of the first array is not equal the lenght of the second array'

title = 'Processing completed'
# Сообщение при отсутствии ошибок
if len(msgs) == 0: 
    text = "Errors didn't find!\nGood work!"
# Сообщение при разном размере массивов или в случае отказа от проверки
elif 'Lenght' in msgs or 'Uploading' in msgs: 
    text = msgs    
# Сообщение об ошибках
else: 
    text = (f'The next sequences were uploaded incorrect:\n{", ".join(msgs)}')
    

pyautogui.alert(
    text=text,
    title=title)