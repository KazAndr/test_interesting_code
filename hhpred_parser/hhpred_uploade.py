import time
import glob
import pyautogui
import pyperclip
import pandas as pd

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def submit(message):
    pyperclip.copy(message)

    while driver.find_element_by_xpath(xpath_textbox).get_property("value") != message:
        driver.find_element_by_xpath(xpath_textbox).clear()
        driver.find_element_by_xpath(xpath_textbox).send_keys(Keys.CONTROL, "v")
    
    driver.find_element_by_xpath(xpath_submit).click()

    try:
        driver.implicitly_wait(3)
        driver.find_element_by_xpath(start_job_aw).click()
    except NoSuchElementException:
        driver.implicitly_wait(30)
        
    driver.find_element_by_xpath(xpath_input).click()
    time.sleep(2)
 

default_files = sorted(glob.glob('*.xls'))

if len(default_files) == 0:
    default_files.append('Enter a filename here!')
filename = pyautogui.prompt(
    text='Enter the name of a file for analisys:',
    title='File for analisys',
    default=f'{default_files[0]}'
)
table = pd.read_excel(filename, sheet_name='Sheet1')

# Рабочий вариант загрузки данных на сайт.
driver = webdriver.Chrome()
driver.maximize_window() 
driver.implicitly_wait(30) # глобальное время ожидания для всех элементов
# Захдим на сайт
driver.get("https://toolkit.tuebingen.mpg.de/tools/hhpred")

# Прописываем изначальные пути (полные)
xpath_cookie = '/html/body/div/div[5]/div[2]/button'
xpath_textbox = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[1]/div/div/div/div[1]/div/fieldset[1]/div/textarea'
xpath_submit = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[1]/fieldset/div/button'
xpath_input = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[1]/ul/li[1]/a'
start_job_aw = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[3]/div/div/button[1]'
full_xpath_num_job = (
    '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[1]/fieldset/div/div/input'
)
# Жамкаем кнопку по поводу cookie-сов
time.sleep(1)
driver.find_element_by_xpath(xpath_cookie).click()
user_answer = pyautogui.confirm('Run the clicker for uploads?')
if user_answer == 'OK':
    submit('MMMMMMMMMMMMM')
    for item in table.aa_sequence:
        submit(item)
num_last_seq, _ = driver.find_element_by_xpath(full_xpath_num_job).get_attribute('value').split('_')       

mode = pyautogui.confirm(
    text=(f'The program finished successfully!\n'
          f'The number of the job is {num_last_seq}.\n'
          f'A total of {table.aa_sequence.size} sequences were upload.\n\n'
          f'Run check uploads?'
         ),
    title='Uploading completed',
    buttons=['Yes', 'No']
)

if mode == 'Yes':
    main_link = 'https://toolkit.tuebingen.mpg.de/jobs/'
    uploads_list = get_uploaded_list(num_last_seq, table.aa_sequence.size)
    
    try:
        msgs = check_upload(uploads_list, table.aa_sequence)
    except IndexError:
        msgs = 'Lenght of the first array is not equal the lenght of the second array'

else: 
    msgs = 'Uploading completed'

    
title = 'Processing completed'
# Сообщение при отсутствии ошибок
if len(msgs) == 0: 
    text = "Errors didn't find!\nGood work!"
# Сообщение при разном размере массивов или в случае отказа от проверки
elif 'Lenght' in msgs or 'Uploading' in msgs: 
    text = msgs    
# Сообщение об ошибках
else: 
    text = (f'The next sequences were uploaded incorrectly:\n{", ".join(msgs)}')
    

pyautogui.alert(
    text=text,
    title=title)
