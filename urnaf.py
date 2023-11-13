import textwrap
import datetime
from time import sleep
import pygame as pyg

candidatos = {'1': 'Verde Branco', '2': 'Cinza Branco', '3': 'Verde Lagoa', '0': 'Anula'}
eleitor = {
    '1': 'Teste',
    '2': 'Branco',
    '3': 'Scooby',
    '4': 'Doguito',
    '5': 'lamica',
    '6': 'Dell',
    '7': 'Teste1',
    '8': 'LG',
    '9': 'lar',
    '10': 'Lagoa'
}

votos = {} # dicionário com total de votos começa vazio
votoseleitores = {}   # dicionário com total de votos começa vazio

def menu():
      
    menu = """\n
  ================ MENU ================
  [1]\tEleitores
  [2]\tVotar
  [3]\tResultado
  [0]\tSair
  => """
    return input(textwrap.dedent(menu))
    

    
def eleitores():
    eleitores = input('Digite o numero do eleitor: ')
    if eleitores in eleitor: # se é um dos números de eleitor válido
        
        contatos = dict(eleitor)
        print('Eleitor:', contatos[eleitores])
        confirma = input('Confirma 1 (ou 2 para retorna):')
            
        if confirma == "1":
            
            contatos = dict(eleitor)
            print('Eleitor:', contatos[eleitores], ", Confirmado com Sucesso")
            votoseleitores[eleitores] = votoseleitores.get(eleitores, 0) + 1

        elif confirma == "2":
            print('''Eleitor inválido:
             "Retonando escolha novamente''')

    else:
        print('''Eleitor inválido:
       "Retonando escolha novamente''')
def Votar():
    voto = input('Digite o número do candidato : ')
    if voto in candidatos: # se é um dos números de candidato válido
        contatos = dict(candidatos)
        print('Candidato:', contatos[voto])
        confirma = input('Confirma 1 (ou 2 para retorna):')
        if confirma == "1":
            contatos = dict(candidatos)
            print('Candidato:', contatos[voto],', Voto realizado com sucesso')
            votos[voto] = votos.get(voto, 0) + 1
            pyg.mixer.init()
            pyg.mixer.music.load('urna.mp3')
            pyg.mixer.music.play()
            pyg.mixer.music.set_volume(10)
            sleep(2)
            
            
        elif confirma == "2":
            print('''Candidato inválido:
             "Retonando escolha novamente''')
        #     votoseleitores[eleitores] = votoseleitores.get(eleitores, 0) - 1
                
    else:
        print('''Número inválido:
        "Retonando escolha novamente''')
        #votoseleitores[eleitores] = votoseleitores.get(eleitores, 0) - 1

def resultados():
    print('Resultado:')
    for numero, qtd_votos in votos.items():   #votos[voto] = votos.get(voto, 0) + 1
        print(f'{candidatos[numero]} teve {qtd_votos} votos')
        print("--------------------------")

    for numero, qtd_eleitores in votoseleitores.items():   # votoseleitores[eleitores] = votoseleitores.get(eleitores, 0) + 1
        print(f'Eleitor: {eleitor[numero]} Voltou {qtd_eleitores} x')

def sair():
  print("saindo")
  sleep(2)
  quit()
