import random
from random import randint

print("Vou pensar em um número entre 0 a 10. TENTE ADIVINHAR")
continua = "S"

while continua == "S":
  computador = randint(0,10)
  num = int(input("Em que número eu pensei? "))

  if num == computador:
   print("PARABÉNS! Você acertou!!")
   print ("SEU:", num, "Numero Sorteado:", computador)
   break
  else:
     print("ERROU!! Mais chance na proxima vez!")
     print ("SEU:", num, "Numero Sorteado:", computador)
     continua = input("Quer tentar de novo? [S/N] ").upper()
print ("FIM DO JOGO")
