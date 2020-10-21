import os
import time
import glob
import pyautogui
import pyperclip
import pandas as pd

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def del_dupls(table, content):
    table_with = table[table.Name.str.lower().str.contains(content, regex=False, na=False)]
    try: # если таблица пустая, значит таких элементов нет и удалять нечего
        first_insert = table_with.iloc[0]
    except IndexError:
        return table
    
    table_without = table[~table.Name.str.lower().str.contains(content, regex=False, na=False)]
    
    table_without.loc[table_without.size+1 ] = first_insert
    table_without = table_without.reset_index(drop=True)
    
    return table_without.sort_values(by=['e_value'])

    
def get_html_table_from_site(link):
    driver.get(link)
    # Включаем отображение всех элементов
    el = driver.find_element_by_class_name(size_out)
    for option in el.find_elements_by_tag_name('option'):
        if option.text == 'All':
            option.click()
            
    table_element = driver.find_element_by_class_name(class_table)
    html_view_table = table_element.get_attribute('outerHTML')
    return html_view_table
    
def parse_table(html_table):
    table = pd.read_html(html_table)[0]
    # Переименование колонок для удобства
    table = table.rename(columns={
        "Nr (Click to sort Ascending)": "nr",
        "Hit (Click to sort Ascending)": "hit",
        "Name (Click to sort Ascending)": "Name",
        "Probability (Click to sort Ascending)": "probability",
        "E-value (Click to sort Ascending)": "e_value",
        "SS (Click to sort Ascending)": "ss",
        "Cols (Click to sort Ascending)": "cols",
        "Target Length (Click to sort Ascending)": "target_length"
    })
    
    # Удаляем из таблицы не интересующие нас результаты
    table_cut = table[
        (~table.Name.str.contains('automated matches', regex=False, na=False)) 
        & (~table.Name.str.contains('Uncharacterized protein [Function unknown]', regex=False, na=False))
        & (~table.Name.str.contains('Human', regex=False, na=False))
        & (~table.Name.str.contains('Homo sapiens', regex=False, na=False))
        & (~table.Name.str.contains('Mouse', regex=False, na=False))
    ]
    
    sorted_table = table_cut.sort_values(by=['e_value'])
    
    # Удаляем все включения кроме первого по 'domain of unknown function'
    sorted_table = del_dupls(sorted_table, 'domain of unknown function')
    # Удаляем все включения кроме первого по 'hypothetical protein'
    sorted_table = del_dupls(sorted_table, 'hypothetical protein')
    
    # Нас интересуют только первые три значения в отсортированной по E-value таблице
    # забираем только их
    first_three_sorted = sorted_table[:3]
    
    # Из полученных данных выделяем только те, что удвлетворяют условиям:
    # Если значения E-value <0.1 - забираем
    # Если значения E-value лежат в диапазоне от 0.1 - 8 - забираем, но только одно. 
    msg = []
    saved_value = 0
    for idx, row in first_three_sorted.iterrows():
        if row['probability'] > 60:
            if row['e_value'] < 0.1:
                msg.append(f'{row.hit}; {row.Name}({row.probability}/{"{:.2e}".format(row.e_value)})')
                saved_value += 1
            else:
                if  0.1 <= row['e_value'] <= 8 and saved_value == 0:
                    msg.append(f'{row.hit}; {row.Name}({row.probability}/{"{:.2e}".format(row.e_value)})')
                    saved_value += 1
                    
    # Возвращаем получившееся сообщение, разделенное $
    return '$'.join(msg)


def save_elem(frame, msg):
    with open('results_blast_analyzer.csv', 'a') as results:
        results.write(f'{frame}')
        results.write('\t')
        results.write(msg)
        results.write('\n')
        

# Рабочий вариант сохранения данных с сайта.
driver = webdriver.Chrome()
driver.maximize_window() 
driver.implicitly_wait(30) # глобальное время ожидания для всех элементов

# Имя класса таблицы
class_table = 'table.b-table.table-striped'
# Имя класса к выбору количества элементов в таблице
size_out = "mx-2.custom-select"

main_link = 'https://toolkit.tuebingen.mpg.de/jobs/'

job = pyautogui.prompt(
    text='Enter the job number for download:',
    title='Job number',
    default='000000'
)

if os.path.isfile('results_blast_analyzer.csv'):
    del_file = pyautogui.confirm(
        title='File already exist!',
        text='File with results is in the current folder. Delete it before processing?', 
        buttons=['YES', 'NO'])
    if del_file == 'YES':
        os.remove('results_blast_analyzer.csv')
    
mode = pyautogui.confirm(
    'Enter mode of processing.',
    buttons=['one frame', 'N frames', 'range of frames']
)

if mode == 'one frame':
    n_element = pyautogui.prompt(
        text='Enter the number of element for download:',
        title='Enrer the number of element',
        default='50'
    )
    n_element = int(n_element)
    html_table = get_html_table_from_site(f'{main_link}{job}_{n_element}')
    msg = parse_table(html_table)
    save_elem(n_element, msg)
    
elif mode == 'N frames':
    n_elements = pyautogui.prompt(
        text='Enter the number of elements for download:',
        title='Enrer the number of elements',
        default='50'
    )
    n_elements = int(n_elements)
    
    for i in range(1, n_elements + 1):
        html_table = get_html_table_from_site(f'{main_link}{job}_{i}')
        msg = parse_table(html_table)
        save_elem(i, msg)
        
else:
    n_range = pyautogui.prompt(
        text='Enter values separated by a space (e.g. 5 50)',
        title='Enter the range of frames',
        default='5 50'
    )
    start, stop = n_range.split()
    start = int(start)
    stop = int(stop)
    
    for i in range(start, stop + 1):
        html_table = get_html_table_from_site(f'{main_link}{job}_{i}')
        msg = parse_table(html_table)
        save_elem(i, msg)
    


pyautogui.alert(
    text=(f'The program finished successfully!\n'
          f'The results were saved in "results_blast_analyzer.csv".'),
    title='Processing completed')
driver.quit() # завершение работы драйвера