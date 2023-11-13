"""
Numa eleição existem alguns candidatos.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
Desenvolvido por Fabiano de Lima Navarro
"""

# Importando as bibliotecas

from urnaf import *
from datetime import date
import textwrap
current_date = date.today()
formatted_date = current_date.strftime('%d/%m/%Y')
print()
print(f'****Votação**** Data:',formatted_date)
print("---------------------------------")


while True:
    opcao = menu()
    
    if opcao =="1":
        eleitores()
    
    elif opcao =="2":
        Votar()

    elif opcao =="3":
        resultados()
            
    elif opcao == "0":
        sair()
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
