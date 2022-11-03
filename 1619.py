import re
def smiles(str_smile):
    result = re.findall(r'[;:]{1}-*[()\[\]]+',str_smile)
    return len(result)

print(smiles(':);------[[[[[]'))