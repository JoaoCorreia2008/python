import json
import gravar_dados

from gravar_dados import nome_do_ficheiro
from pessoas import pessoas

pessoas = []
with open(nome_do_ficheiro,'r',encoding='utf8') as f:
    pessoas = json.load(f)

print(*pessoas,sep='\n')