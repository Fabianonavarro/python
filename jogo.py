import random

def mostrar_mensagem(mensagem, erro=False):
    """Exibe uma mensagem, com prefixo de erro se indicado."""
    print(f"{'ERRO: ' if erro else ''}{mensagem}")

def configurar_jogo():
    """Configura o jogo com base na dificuldade escolhida pelo usuário."""
    opcoes = {'1': (10, 2, 2), '2': (100, 3, 10), '3': (1000, 5, 50)}
    while True:
        mostrar_mensagem("Escolha a dificuldade:\n1. Fácil\n2. Intermediário\n3. Difícil")
        escolha = input("Digite o número da dificuldade (1, 2, 3): ")
        if escolha in opcoes:
            return opcoes[escolha]
        mostrar_mensagem("Escolha inválida. Tente novamente.", erro=True)

def obter_palpite(limite):
    """Obtém e valida o palpite do usuário."""
    while True:
        try:
            palpite = int(input(f"Em que número eu pensei? (0 a {limite}): "))
            if 0 <= palpite <= limite:
                return palpite
            mostrar_mensagem(f"Por favor, insira um número entre 0 e {limite}.", erro=True)
        except ValueError:
            mostrar_mensagem("Entrada inválida. Insira um número válido.", erro=True)

def fornecer_dica(numero_sorteado, palpite, faixa_proximidade):
    """Fornece uma dica sobre o palpite do usuário, incluindo proximidade."""
    if palpite == numero_sorteado:
        return "Você acertou o número!"
    
    dica = "O número é maior." if palpite < numero_sorteado else "O número é menor."
    
    if abs(palpite - numero_sorteado) <= faixa_proximidade:
        dica += " Você está próximo do número."
    else:
        dica += " Você está longe do número."
    
    return dica

def jogar():
    """Controla o fluxo principal do jogo."""
    while True:
        limite, tentativas, faixa_proximidade = configurar_jogo()
        numero_sorteado = random.randint(0, limite)
        mostrar_mensagem(f"Vou pensar em um número entre 0 e {limite}. TENTE ADIVINHAR")

        while tentativas > 0:
            palpite = obter_palpite(limite)
            if palpite == numero_sorteado:
                mostrar_mensagem(f"PARABÉNS! Você acertou!!\nSeu palpite: {palpite} | Número Sorteado: {numero_sorteado}")
                break
            tentativas -= 1
            if tentativas > 0:
                dica = fornecer_dica(numero_sorteado, palpite, faixa_proximidade)
                mostrar_mensagem(f"ERROU!! {dica} Você tem {tentativas} tentativa(s) restante(s).")
            else:
                mostrar_mensagem(f"FIM DO JOGO! O número era {numero_sorteado}. Seu palpite final: {palpite}")
        
        if input("Quer jogar novamente? [S/N] ").strip().upper() != 'S':
            mostrar_mensagem("FIM DO JOGO")
            break

if __name__ == "__main__":
    jogar()
