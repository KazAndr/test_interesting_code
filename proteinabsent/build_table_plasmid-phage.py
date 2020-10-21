from itertools import zip_longest

def get_unique_protein_id(element, treshold):
    result = {}
    empty_result = {'-': None}
    for item in element:
        try:
            e_value_1 = float(item[3])
        except ValueError:
            return empty_result
        
        if e_value_1 <= treshold:
            local_key = item[2]
            if local_key == '-':
                local_key = f'loc_tag={item[1]}'
            
            if local_key not in result:
                result[local_key] = e_value_1
            else:
                if e_value_1 <= result[local_key]:
                    result[local_key] = e_value_1
                    
    if len(result) == 0:
        return empty_result
    
    return result


treshold = float(input('Enter E-value 1 limit: '))

with open('seq_database.fasta', 'r') as file:
    content = file.readlines()
    
with open('Term_hmmsearch.out', 'r') as file:
    term_hmmsearch = file.readlines()
    
with open('TMP_hmmsearch.out', 'r') as file:
    tmp_hmmsearch = file.readlines()
    
with open('MCP_hmmsearch.out', 'r') as file:
    mcp_hmmsearch = file.readlines()
    
with open('ParA_hmmsearch.out', 'r') as file:
    para_hmmsearch = file.readlines()
    
with open('ParM_hmmsearch.out', 'r') as file:
    parm_hmmsearch = file.readlines()
    
with open('XerC_hmmsearch.out', 'r') as file:
    xerc_hmmsearch = file.readlines()
    
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
        
term_hmmsearch_pars = {}
tmp_hmmsearch_pars = {}
mcp_hmmsearch_pars = {}
para_hmmsearch_pars = {}
parm_hmmsearch_pars = {}
xerc_hmmsearch_pars = {}

N_E1 = 4
N_E2 = 7

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
                        
# Заполенние несуществующих ключей, для избежания KeyError в последующих элементах
empty_fill = [('-', '-', '-', '-', '-')]
for prot_name in prot_names:
    for name, dict_pars in loop_content:
        try:
            len(dict_pars[prot_name])
        except KeyError:
            dict_pars[prot_name] = empty_fill
            
with open('table_plasmids-phage.out', 'w') as file:
    file.write(f'Plasmids\tTerm\tTMP\tMCP\tParA\tParM\tXerC\n')
    for prot_name in prot_names:
                
        unique_trm = get_unique_protein_id(term_hmmsearch_pars[prot_name], treshold)
        unique_tmp = get_unique_protein_id(tmp_hmmsearch_pars[prot_name], treshold)
        unique_m = get_unique_protein_id(mcp_hmmsearch_pars[prot_name], treshold)
        unique_pa = get_unique_protein_id(para_hmmsearch_pars[prot_name], treshold)
        unique_pm = get_unique_protein_id(parm_hmmsearch_pars[prot_name], treshold)
        unique_x = get_unique_protein_id(xerc_hmmsearch_pars[prot_name], treshold)
        
        if not (unique_trm == unique_tmp == unique_m == unique_pa == unique_pm == unique_x):
            file.write(f'{prot_name}\t')
            file.write(','.join(unique_trm))
            file.write('\t')
            file.write(','.join(unique_tmp))
            file.write('\t')
            file.write(','.join(unique_m))
            file.write('\t')
            file.write(','.join(unique_pa))
            file.write('\t')
            file.write(','.join(unique_pm))
            file.write('\t')
            file.write(','.join(unique_x))
            file.write('\n')
        else:
            continue

