'''
Busca cep 

'''
import requests 
import json
import time

from datetime import date
 
print("_____________________________________________________________________________")

current_date = date.today()
formatted_date = current_date.strftime('%d/%m/%Y')
print("Data:", formatted_date)


print()
def main():
        print("--------------------------------")
        print("   ### Consulta CEP ##           ")
        print("--------------------------------")
        print()

        cep_input = input("Digite o CEP que deseja consultar: ")

        if len(cep_input) != 8:
                print('Quantidade de dígitos inválida!')
                main()
                
        busca = requests.get ('https://viacep.com.br/ws/ws/{}/json/'.format(cep_input))
        busca_cep = busca.json()

        if "erro" not in busca_cep:
                print()
                print("==> CEP ENCONTRADO <==")
                print()
                print("CEP: {}".format(busca_cep["cep"]))

                print("Endereco: {}".format(busca_cep["logradouro"]))
                print('Bairro: {}'.format(busca_cep['bairro']))
                print('Cidade: {}'.format(busca_cep['localidade']))
                print('Estado: {}'.format(busca_cep['uf']))
                print("__________________________________________________")

        else:
            print("Este CEP {}: e  inválido. Favor Verificar".format(cep_input))

        print("__________________________________________________")
        
        option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
        if option == 1:
            print("Você escolheu a opção ==> 1 <==")
            print("Aguarde")
            time.sleep(5)
            print()
            print()
            main()
        else:
            print("Você escolheu a opção ==> 2 <==")
            print("Aguarde")   
            time.sleep(5)
            print('Saindo...')
            exit()
                        
if __name__ == '__main__':
	main()
