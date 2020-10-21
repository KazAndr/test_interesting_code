import glob
import pyautogui

import pandas as pd

def split_blast(elem):
    if elem == 'hp' or elem == '-':
        return elem, elem
    else:
        elems = elem.split('$')
        names = []
        e_values = []
        for item in elems:
            to_names, to_e_values = item.split(';')
            names.append(to_names)
            e_values.append(to_e_values)

        return '\n'.join(names), '\n'.join(e_values)


def split_hhpred(elem):
    if len(elem) == 0:
        return '-', '-'
    else:
        elems = elem.split('$')
        return '\n'.join(elems)

default_files = sorted(glob.glob('*.xls'))

if len(default_files) == 0:
    default_files.append('Enter a filename here!')
filename = pyautogui.prompt(
    text='Enter the name of a file for analisys:',
    title='File for analisys',
    default=f'{default_files[0]}'
)
firts_table = pd.read_excel(filename, sheet_name='Sheet1')
blast_table = pd.read_csv('results_blast_analyzer.csv', sep='\t', names=[1, 2])
hhpred_table = pd.read_csv('results_hhpred_analyzer.csv', sep='\t', names=[1, 2])
hhpred_table = hhpred_table.fillna('') 

annotation_table = pd.DataFrame(columns=[
    'ORF№',
    'Start codon',
    'Stop codon',
    'Strand',
    'Blast results, Name',
    'Blast results, E-val',
    'Conserved domains, Name',
    'Conserved domains,E-val',
    'Hhpred results, (Prob./E-val)',
])

for idx, orf in enumerate(firts_table.orf):
    blast_names, blast_eval_n = split_blast(blast_table.iloc[idx, 0])
    blast_domainsm, blast_eval_d = split_blast(blast_table.iloc[idx, 1])
    hhpred_results = split_hhpred(hhpred_table.iloc[idx, 1])
    
    annotation_table.loc[idx] = [
        firts_table.orf[idx],
        firts_table.start[idx],
        firts_table.stop[idx],
        firts_table.strand[idx],
        blast_names,
        blast_eval_n,
        blast_domainsm,
        blast_eval_d,
        hhpred_results
    ]
    
annotation_table.to_excel('annotation_table.xlsx', sheet_name='results', index=False)
