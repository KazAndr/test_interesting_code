import re
import os
import glob

import pandas as pd


# Функция для определения количества обрануженных элементов
def get_num_prot(lines):
    res = []
    for i in lines:
        a = re.findall('No \w+\n',i)
        if a:
            res.extend(a)
            
    return int(res[-1].split()[1])


# Функция для вставки дополнительного пробела перед '('
# Добавлена по причине наличия болших значений Template
# Не позволяющих разделить Template и HMM
def insert_space(line):
    list_elem = list(line)
    for idx, item in enumerate(list_elem[:]):
        if item =='(':
            list_elem.insert(idx, ' ')
    return ''.join(list_elem)

# Функция для удаления всех елементов содержащих content
# кроме самого первого. Возвращает отсортированную по e_value таблицу.
#
def del_dupls(table, content):
    table_with = table[table.Name.str.lower().str.contains(content, regex=False)]
    try: # если таблица пустая, значит таких элементов нет и удалять нечего
        first_insert = table_with.iloc[0]
    except IndexError:
        return table
    
    table_without = table[~table.Name.str.lower().str.contains(content, regex=False)]
    
    table_without.loc[table_without.size+1 ] = first_insert
    table_without = table_without.reset_index(drop=True)
    
    return table_without.sort_values(by=['E_value_float'])

files = sorted(glob.glob('./data/*.hhr'), key=lambda a : int(os.path.basename(a)[15:-4]))

# Имена колонок постоянные
results = open('results_hhpred_analyzer.csv', 'w')

NAME_CLMN= [
    'No', 'Hit', 'Name', 'Prob', 'E_value', 'P_value',
    'Score', 'SS', 'Cols', 'Query_HMM', 'Template', 'HMM'
]

for file in files:
    
    # Выделяем номер рамки
    _, _, frame = file.split('_')
    frame, _ = frame.split('.')
    
    # Считываем файлы
    with open(file) as f:
        lines = f.readlines()
    
    # Добавляем '('
    
    lines = [insert_space(line) for line in lines]
    
    # Определяем количество элементов в таблице
    num = get_num_prot(lines)
    # разделяем файл на информационные блоки согласно полученному выше значению
    info = lines[:8]
    hits = lines[8:num+9] # 9-ка, потому что счет идет от начала файла
    algn = lines[num+9:]
    
    # Создаем pandas-таблицу для удобной работы с информацией
    table = pd.DataFrame(columns=NAME_CLMN)
    
    # Цикл по hits для заполнения таблицы
    for idx, hit in enumerate(hits[1:]): # пропускаем название колонок
        No, Hit, *trsh, Prob, E_v, P_v, Sco, SS, Cols, Q_HMM, Template, HMM = hit.split()
        nm_idx = algn.index(f'No {No}\n')
        _, *name = algn[nm_idx + 1].split()
        name = ' '.join(name)

        table.loc[idx] = [
            No,
            Hit,
            name,
            Prob,
            E_v,
            P_v,
            Sco,
            SS,
            Cols,
            Q_HMM,
            Template,
            HMM
        ]
    
    # Удаляем из таблицы не интересующие нас результаты
    table_cut = table[
        (~table.Name.str.contains('automated matches', regex=False)) 
        & (~table.Name.str.contains('Uncharacterized protein [Function unknown]', regex=False))
        & (~table.Name.str.contains('Human', regex=False))
        & (~table.Name.str.contains('Homo sapiens', regex=False))
        & (~table.Name.str.contains('Mouse', regex=False))
    ]
    

    
    # Создаем новые колонки с числовыми значениями, для сортировки и  сравнения значений
    table_cut['E_value_float'] = table_cut['E_value'].astype(float)
    table_cut['Prob_float'] = table_cut['Prob'].astype(float)
    
    
    sorted_table = table_cut.sort_values(by=['E_value_float'])
    
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
        if row['Prob_float'] > 60:
            if row['E_value_float'] < 0.1:
                msg.append(f'{row.Hit}; {row.Name}({row.Prob}/{row.E_value})')
                saved_value += 1
            else:
                if  0.1 <= row['E_value_float'] <= 8 and saved_value == 0:
                    msg.append(f'{row.Hit}; {row.Name}({row.Prob}/{row.E_value})')
                    saved_value += 1
                    
    #записываем полученную информацию в файл
    results.write(frame)
    results.write('\t')
    results.write('$'.join(msg))
    results.write('\n')

# Обязтельно закрываем файл после окончания работы программы
results.close()