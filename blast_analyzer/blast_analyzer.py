import os
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


def different_indervalt(last_inrerval, curent_interval):
    inter11, inter12 = [int(i) for i in last_inrerval.split('-')]
    inter21, inter22 = [int(i) for i in curent_interval.split('-')]
    
    dif_1 = abs(inter11 - inter21)
    dif_2 = abs(inter12 - inter22)
    
    if dif_1 >=25 or dif_2>=25:
        return True
    else:
        return False
    

def parsing_dscTable(table_element):
    html_table = table_element.get_attribute('outerHTML')
    table = pd.read_html(html_table)[0]
    table = table[table['E value'] < 0.01]
    
    msg = []
    if len(table) == 0:
        msg.append('-')
    else:
        table_cut = table[:20][
            (~table.Description.str.contains('hypothetical protein', regex=False))
        ]

        if len(table_cut) == 0:
            msg.append('hp')
        else:
            for idx, row in table.iterrows():
                if (
                    (('hypothetical protein' not in row['Description'])
                     and ("conserved hypothetical protein" not in row['Description'])
                     and ("unnamed protein product" not in row['Description'])
                     and ("conserved protein of unknown function" not in row['Description'])
                    ) 
                    and len(msg) < 3):

                    msg.append(f"{row['Description']};{'{:.1e}'.format(row['E value'])}")
    
    
    if len(msg) == 0:
        try:
            a = (len(table)/len(table[table.Description.str.contains('hypothetical protein')]))/100
            ratio_hp = (1 - a)
        except ZeroDivisionError:
            ratio_hp = 0
            
        if ratio_hp >= 0.2:
            msg.append('hp')
        else:
            msg.append('-')
    
    return msg


def parsing_cddInfo(table_element):
    html_table = table_element.get_attribute('outerHTML')
    table_results = pd.read_html(html_table)[0]
    # Удаление всего лишнего из таблицы
    table_results = table_results.iloc[1:, 1:].dropna()[::2]
    # Оставляем только данные где E-value < 0.001
    table_results['E_value_float'] = table_results[5].astype(float)
    table_results = table_results[table_results['E_value_float'] < 0.001]
    
    msg = []
    if len(table_results) == 0:
        msg.append('-')
    else:
        last_interval = '0-0' # Данный интервал взят наобум, но работать скорее всего будет
        for idx, row in table_results.iterrows():
            if len(msg) < 3 and different_indervalt(last_interval, row[4]):
                msg.append(f'{row[1]}({row[4]});{row[5]}')
                last_interval = row[4]
    
    return msg

def send_submit(sequence):
    box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "QUERY")))
    button = driver.wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "blastbutton")))

    pyperclip.copy(sequence) 
    box.send_keys(Keys.CONTROL, "a")
    box.send_keys(Keys.DELETE)
    box.send_keys(Keys.CONTROL, "v")
    
    button.click()

    # Пауза реализована следующим образом:
    # Прокнамма с паузами в 5 секунд пытается найти элемент "Edit Search" в течении 500 секунд
    # как только элемент найден, пограмма идет дальше.
    # Если элемент не найден даже по прошествии 500 секунд, программа сообщает пользователю
    # что все плохо.
    element_exist = False
    for i in range(100): # 500 секунд ожмдания
        try:
            edit_search = driver.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="searchOptions"]')))
            element_exist = True
            break
        except TimeoutException:
            continue
    if element_exist:
        try:
            table_result = driver.wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="dscTable"]')))

            msg_main = parsing_dscTable(table_result)


            graphic_summary = driver.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="btnGrph"]')))
            graphic_summary.click()

            lable_cddInfo = driver.wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="cddDesc"]')))

            NO_SWITCH = "No putative conserved domains have been detected"

            if NO_SWITCH not in lable_cddInfo.get_attribute('outerHTML'):
                # Поиск кнопки и переход на дополнительную страницу
                cddInfo = driver.wait.until(EC.element_to_be_clickable(
                            (By.XPATH, '//*[@id="cddInfo"]/a/img')))
                cddInfo.click()

                # открытые табы
                #driver.window_handles

                # перемещание по табам
                driver.switch_to.window(driver.window_handles[1])
                # Поиск элемента таблицы на дополнительной странице (не забыть активировать таб)
                table_cddInfo = driver.wait.until(EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="std"]')))

                msg_cddInfo = parsing_cddInfo(table_cddInfo)

                # Закрытие активного таба и перемещение к основному. 
                # !!! Не активировать при одном активном табе!!!
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            else:
                msg_cddInfo = ['-']
        except TimeoutException:
            msg_main = ['-']
            msg_cddInfo = ['-']

    else:
        pyautogui.alert(title=f'Timed out error!',
                       text=(f'The search for the item returned no results.\n'
                        f'The program is completing its work.')
                       )
        
    return msg_main, msg_cddInfo


default_files = sorted(glob.glob('*.xls'))

if len(default_files) == 0:
    default_files.append('Enter a filename here!')
filename = pyautogui.prompt(
    text='Enter the name of a file for analisys:',
    title='File for analisys'
)
table = pd.read_excel(filename, sheet_name='Sheet1')

driver = webdriver.Chrome()
driver.maximize_window() 
driver.wait = WebDriverWait(driver, 5)
driver.get(f"https://blast.ncbi.nlm.nih.gov/"
           f"Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome")

# basic adjasment
organism = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "EQ_MENU")))
psi_blast = driver.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="psiBlast"]')))
delta_blast = driver.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="deltaBlast"]')))

mode = pyautogui.confirm(
    'Enter mode of processing.',
    buttons=['Virus+PSI-BLAST', 'DELTA-BLAST']
)

if mode == 'Virus+PSI-BLAST':
    organism.send_keys(f'Viruses (taxid:10239)')
    psi_blast.click()
else:
    delta_blast.click()

start_pos = pyautogui.prompt(
    text='What element will we start processing from? (default: 1)', 
    title='', 
    default='1'
    )

if os.path.isfile('results_blast_analyzer.csv'):
    del_file = pyautogui.confirm(
        title='File already exist!',
        text='File with results is in the current folder. Delete it before processing?', 
        buttons=['YES', 'NO'])
    if del_file == 'YES':
        os.remove('results_blast_analyzer.csv')
    
if start_pos == '':
    start_pos = 1
elif start_pos is None:
    driver.quit() # завершение работы драйвера
else:
    start_pos = int(start_pos)
    
with open('results_blast_analyzer.csv', 'a') as file:
    for idx, elem in enumerate(table.aa_sequence[start_pos-1:]):
        pyautogui.alert(text=f'{start_pos + idx}', title='Sequence number', timeout=700)
        msg_1, msg_2, = send_submit(elem)
        file.write(f'{start_pos + idx}\t')
        file.write('$'.join(msg_1))
        file.write('\t')
        file.write('$'.join(msg_2))
        file.write('\n')
        # переходим на основное меню
        edit_search = driver.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="searchOptions"]')))
        edit_search.click()
        
driver.quit() # завершение работы драйвера
pyautogui.alert(
    text=(f'The program finished successfully!\n'
          f'A total of {start_pos + idx} sequences were processed.\n'
         f'Good luck with further analysis.'),
    title='Processing completed')
