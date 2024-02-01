'''calcular o valor de uma viagem.
    
'''
# Variaveis
valorCombustivel = float(input("Digite o Valor do Combustivel:")) 
kmPorLitros = int(input("Digite Quantos KM seu carro faz por litro:"))
distanciaEmKm = int(input("Qual a distancia percorrida:"))

# Calculos
litrosConsumidos = distanciaEmKm / kmPorLitros
valorGasto = litrosConsumidos * valorCombustivel

# Escolha combustivel
tipoCombustivel = int(input('Qual combustivel usou ?\n1. Etanol\n2. Gasolina\n'))

# Resultado escolhas
if tipoCombustivel == 1:
    print("Você escolheu a opção ==> (1) Etanol <==")
    print(f' Valor gasto com Etanol R$: {valorGasto:.2f}')
    print(f' Gastou: {litrosConsumidos:.2f} litros com Etanol')
    
else:
    print("Você escolheu a opção ==> (2) Gasolina <==")
    print(f' Valor gasto com Gasolina R$: {valorGasto:.2f}')
    print(f' Gastou: {litrosConsumidos:.2f} litros com Gasolina')
    
    
