#!/usr/bin/env python
# coding: utf-8

# In[161]:


from itertools import zip_longest


# ## Чтение файлов

# In[50]:


with open('seq_database.fasta', 'r') as file:
    content = file.readlines()


# In[51]:


with open('Term_hmmsearch.out', 'r') as file:
    term_hmmsearch = file.readlines()


# In[52]:


with open('TMP_hmmsearch.out', 'r') as file:
    tmp_hmmsearch = file.readlines()


# In[53]:


with open('MCP_hmmsearch.out', 'r') as file:
    mcp_hmmsearch = file.readlines()


# In[54]:


with open('ParA_hmmsearch.out', 'r') as file:
    para_hmmsearch = file.readlines()


# In[55]:


with open('ParM_hmmsearch.out', 'r') as file:
    parm_hmmsearch = file.readlines()


# In[56]:


with open('XerC_hmmsearch.out', 'r') as file:
    xerc_hmmsearch = file.readlines()


# ## Поиск вхождений плазмид в группы

# In[57]:


prot_names = []
for item in content:
    try:
        prot_name = item.split('_prot_')[0].split('|')[1]
        if prot_name not in prot_names:
            prot_names.append(prot_name)
        else:
            continue
    except IndexError:
        continue


# In[58]:


term_hmmsearch_dict = dict.fromkeys(prot_names, 0)
tmp_hmmsearch_dict = dict.fromkeys(prot_names, 0)
mcp_hmmsearch_dict = dict.fromkeys(prot_names, 0)
para_hmmsearch_dict = dict.fromkeys(prot_names, 0)
parm_hmmsearch_dict = dict.fromkeys(prot_names, 0)
xerc_hmmsearch_dict = dict.fromkeys(prot_names, 0)


# In[59]:


loop_content = (
    (term_hmmsearch, term_hmmsearch_dict),
    (tmp_hmmsearch, tmp_hmmsearch_dict),
    (mcp_hmmsearch, mcp_hmmsearch_dict),
    (para_hmmsearch, para_hmmsearch_dict),
    (parm_hmmsearch, parm_hmmsearch_dict),
    (xerc_hmmsearch, xerc_hmmsearch_dict)
    
)

for prot_name in prot_names:
    for lines, dict_prot in loop_content:
        for line in lines:
            try:
                prot_name_line = line.split('_prot_')[0].split('|')[1]
            except IndexError:
                continue
            if prot_name == prot_name_line:
                dict_prot[prot_name] +=1


# In[61]:


with open('resultsmatch.out', 'w') as file:
    file.write(
        f'Plasmids\tTerm\tTMP\tMCP\tParA\tParM\tXerC\t'
        f'TeTmM\tTeTmMPa\tTeTmMPm\tTeTmMPaPm\tTeTmMX\t'
        f'TeTmMPaX\tTeTmMPmX\tTeTmMPaPmX\tTeTmPa\tTeMPa\n'
    )
    
    for prot_name in prot_names:
        file.write(f'{prot_name}\t')
        file.write(f'{term_hmmsearch_dict[prot_name]}\t')
        file.write(f'{tmp_hmmsearch_dict[prot_name]}\t')
        file.write(f'{mcp_hmmsearch_dict[prot_name]}\t')
        file.write(f'{para_hmmsearch_dict[prot_name]}\t')
        file.write(f'{parm_hmmsearch_dict[prot_name]}\t')
        file.write(f'{xerc_hmmsearch_dict[prot_name]}\t')
        
        # TeTmM
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')
        
        #TeTmMPa
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
            and para_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')
            
        #TeTmMPm
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
            and parm_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')
        
        #TeTmMPaPm
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
            and para_hmmsearch_dict[prot_name] != 0
            and parm_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')
        
        #TeTmMX
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
            and xerc_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')
            
        #TeTmMPaX
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
            and para_hmmsearch_dict[prot_name] != 0
            and xerc_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')
            
        #TeTmMPmX
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
            and parm_hmmsearch_dict[prot_name] != 0
            and xerc_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')

        #TeTmMPaPmX
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
            and para_hmmsearch_dict[prot_name] != 0
            and parm_hmmsearch_dict[prot_name] != 0
            and xerc_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')
            
        #TeTmPa
        if (term_hmmsearch_dict[prot_name] != 0
            and tmp_hmmsearch_dict[prot_name] != 0
            and para_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\t')
        else:
            file.write(f' \t')
        #TeMPa
        if (term_hmmsearch_dict[prot_name] != 0
            and mcp_hmmsearch_dict[prot_name] != 0
            and para_hmmsearch_dict[prot_name] != 0
           ):
            file.write(f'+\n')
        else:
            file.write(f' \n')


# ## Парсинг данных из файлов (locus_tag, protein_id, E-value_1,E-value_1)

# In[239]:


term_hmmsearch_pars = {}
tmp_hmmsearch_pars = {}
mcp_hmmsearch_pars = {}
para_hmmsearch_pars = {}
parm_hmmsearch_pars = {}
xerc_hmmsearch_pars = {}


# In[240]:


N_E1 = 4
N_E2 = 7


# In[241]:


loop_content = (
    (term_hmmsearch, term_hmmsearch_pars),
    (tmp_hmmsearch, tmp_hmmsearch_pars),
    (mcp_hmmsearch, mcp_hmmsearch_pars),
    (para_hmmsearch, para_hmmsearch_pars),
    (parm_hmmsearch, parm_hmmsearch_pars),
    (xerc_hmmsearch, xerc_hmmsearch_pars)
    
)

for prot_name in prot_names:
    for lines, dict_prot in loop_content:
        for line in lines:
            try:
                prot_name_line = line.split('_prot_')[0].split('|')[1]
            except IndexError:
                continue
            
            if prot_name == prot_name_line:
                splt_line = line.split()
                
                try:
                    protein_id = line.split('protein_id=')[1].split(']')[0]
                except IndexError:
                    protein_id = '-'
                try:
                    locus_tag = line.split('locus_tag=')[1].split(']')[0]
                except IndexError:
                    locus_tag = '-'
                    
                if prot_name in dict_prot:
                    dict_prot[prot_name].append(
                        (
                            prot_name_line,
                            locus_tag,
                            protein_id,
                            splt_line[N_E1],
                            splt_line[N_E2]
                        )
                
                    )
                else:
                     dict_prot[prot_name] = [(
                        (
                            prot_name_line,
                            locus_tag,
                            protein_id,
                            splt_line[N_E1],
                            splt_line[N_E2])
                     )]


# In[242]:


loop_content = (
    ('term_hmmsearch_locus_tag_Evalue.out', term_hmmsearch_pars),
    ('tmp_hmmsearch_locus_tag_Evalue.out', tmp_hmmsearch_pars),
    ('mcp_hmmsearch_locus_tag_Evalue.out', mcp_hmmsearch_pars),
    ('para_hmmsearch_locus_tag_Evalue.out', para_hmmsearch_pars),
    ('parm_hmmsearch_locus_tag_Evalue.out', parm_hmmsearch_pars),
    ('xerc_hmmsearch_locus_tag_Evalue.out', xerc_hmmsearch_pars)
    
)

for filename, dict_prot in loop_content:
        with open(filename, 'w') as file:
            file.write(f'Plasmids\tlocus_tag\tprotein_id\tE-value_1\tE-value_2\n')
            for prot_name in prot_names:
                try:
                    for item in dict_prot[prot_name]:
                        file.write(f'{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\t{item[4]}\n')
                except KeyError:
                    pass


# ## Формирование единого файла с результатами выборки с отсечкой по E-value_1

# In[243]:


empty_fill = [('-', '-', '-', '-', '-')]


# In[244]:


# Заполенние несуществующих ключей, для избежания KeyError в последующих элементах
for prot_name in prot_names:
    for name, dict_pars in loop_content:
        try:
            len(dict_pars[prot_name])
        except KeyError:
            dict_pars[prot_name] = empty_fill


# In[305]:


treshold = float(input('Enter E-value 1 limit: '))
with open('joinedfile_limitedEvalue.out', 'w') as file:
    file.write(f'Plasmids\t') # Самая первая колонка
    file.write(f'locus_tag(Term)\tprotein_id(Term)\tE-value_1(Term)\tE-value_2(Term)\t')  # Term
    file.write(f'locus_tag(TMP)\tprotein_id(TMP)\tE-value_1(TMP)\tE-value_2(TMP)\t')  # TMP
    file.write(f'locus_tag(MCP)\tprotein_id(MCP)\tE-value_1(MCP)\tE-value_2(MCP)\t')  # MCP
    file.write(f'locus_tag(ParA)\tprotein_id(ParA)\tE-value_1(ParA)\tE-value_2(ParA)\t')  # ParA
    file.write(f'locus_tag(ParM)\tprotein_id(ParM)\tE-value_1(ParM)\tE-value_2(ParM)\t')  # ParM
    file.write(f'locus_tag(XerC)\tprotein_id(XerC)\tE-value_1(XerC)\tE-value_2(XerC)\n')  # XerC
    for prot_name in prot_names:
        for i_trm, i_tmp, i_m, i_pa, i_pm, i_x in zip_longest(
            term_hmmsearch_pars[prot_name],
            tmp_hmmsearch_pars[prot_name],
            mcp_hmmsearch_pars[prot_name],
            para_hmmsearch_pars[prot_name],
            parm_hmmsearch_pars[prot_name],
            xerc_hmmsearch_pars[prot_name],
            fillvalue='-----'
        ):
            file.write(f'{prot_name}\t')
            
            dict_conds = {
                'c_trm': False,
                'c_tmp' : False,
                'c_m' : False,
                'c_pa' : False,
                'c_pm' : False, 
                'c_x' : False
            }
            for key, item in [
                ('c_trm', i_trm), ('c_tmp', i_tmp), ('c_m', i_m), 
                ('c_pa', i_pa), ('c_pm', i_pm), ('c_x', i_x)]:
                try:
                    dict_conds[key] = float(item[3]) <= treshold
                except ValueError:
                    continue
            
            if dict_conds['c_trm']: #(c_trm and c_tmp and c_m and c_pa and c_pm and c_x):
                file.write(f'{i_trm[1]}\t{i_trm[2]}\t{i_trm[3]}\t{i_trm[4]}\t') # Term value
            else:
                file.write(f'-\t-\t-\t-\t')
            if dict_conds['c_tmp']:
                file.write(f'{i_tmp[1]}\t{i_tmp[2]}\t{i_tmp[3]}\t{i_tmp[4]}\t') # TMP value
            else:
                file.write(f'-\t-\t-\t-\t')
            if dict_conds['c_m']:
                file.write(f'{i_m[1]}\t{i_m[2]}\t{i_m[3]}\t{i_m[4]}\t') # MCP value
            else:
                file.write(f'-\t-\t-\t-\t')
            if dict_conds['c_pa']:
                file.write(f'{i_pa[1]}\t{i_pa[2]}\t{i_pa[3]}\t{i_pa[4]}\t') # ParA value
            else:
                file.write(f'-\t-\t-\t-\t')
            if dict_conds['c_pm']:
                file.write(f'{i_pm[1]}\t{i_pm[2]}\t{i_pm[3]}\t{i_pm[4]}\t') # ParM value
            else:
                file.write(f'-\t-\t-\t-\t')
            if dict_conds['c_x']:
                file.write(f'{i_x[1]}\t{i_x[2]}\t{i_x[3]}\t{i_x[4]}\n') # XerC value
            else:
                file.write(f'-\t-\t-\t-\n')
# Сохранение файла вхождений
with open('resultsmatch_limited_E-value_1.out', 'w') as file:
    file.write(
        f'Plasmids\tTerm\tTMP\tMCP\tParA\tParM\tXerC\n'
    )
    for prot_name in prot_names:
        file.write(f'{prot_name}\t')
        for filename, dict_prot in loop_content:
            total_cond = False
            for item in dict_prot[prot_name]:
                try:
                    local_cond = float(item[3]) <= treshold
                except ValueError:
                    continue
                if local_cond:
                    total_cond = True
                else:
                    pass
            if total_cond:
                file.write('+\t')
            else:
                file.write('-\t')
        file.write('\n')


# In[ ]:




