import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class JogoAdivinhacao(QWidget):
    def __init__(self):
        super().__init__()

        self.limite = 10
        self.tentativas = 2
        self.faixa_proximidade = 2
        self.numero_sorteado = None

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Configuração da dificuldade
        self.dificuldade_combo = QComboBox()
        self.dificuldade_combo.addItems(["Fácil", "Intermediário", "Difícil"])
        self.dificuldade_combo.currentIndexChanged.connect(self.configurar_jogo)
        
        layout.addWidget(QLabel("Escolha a dificuldade:"), alignment=Qt.AlignCenter)
        layout.addWidget(self.dificuldade_combo)

        # Campo de entrada para palpite
        self.palpite_input = QLineEdit()
        self.palpite_input.setPlaceholderText(f"Digite seu número de 0 a {self.limite}")
        
        layout.addWidget(self.palpite_input)

        # Botão para enviar o palpite (renomeado para "Jogar")
        self.jogar_button = QPushButton("Jogar")
        self.jogar_button.clicked.connect(self.verificar_palpite)
        self.jogar_button.setStyleSheet("font-size: 16px; padding: 10px;")  # Estilo do botão
        
        layout.addWidget(self.jogar_button)
        layout.addSpacing(30)  # Espaço extra após o botão "Jogar"

        # Botão para reiniciar o jogo
        self.reiniciar_button = QPushButton("Reiniciar Jogo")
        self.reiniciar_button.clicked.connect(self.iniciar_jogo)
        self.reiniciar_button.setStyleSheet("font-size: 16px; padding: 10px;")  # Estilo do botão
        
        layout.addWidget(self.reiniciar_button)

        # Botão para sair do jogo
        self.sair_button = QPushButton("Sair")
        self.sair_button.clicked.connect(self.close)
        self.sair_button.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 16px; padding: 10px;")
        
        layout.addWidget(self.sair_button)

        # Label para exibir mensagens
        self.mensagem_label = QLabel()
        self.mensagem_label.setAlignment(Qt.AlignCenter)
        self.mensagem_label.setWordWrap(True)
        self.mensagem_label.setStyleSheet("font-size: 14px;")
        
        layout.addWidget(self.mensagem_label)

        # Label para exibir o resultado final
        self.resultado_label = QLabel()
        self.resultado_label.setAlignment(Qt.AlignCenter)
        self.resultado_label.setWordWrap(True)
        self.resultado_label.setStyleSheet("font-size: 18px; padding: 10px;")

        layout.addWidget(self.resultado_label)

        self.setLayout(layout)
        self.setWindowTitle('Desafio da Adivinhação')
        self.iniciar_jogo()

    def configurar_jogo(self):
        """Configura o jogo com base na dificuldade escolhida pelo usuário."""
        dificuldades = {
            "Fácil": (10, 2, 2),
            "Intermediário": (100, 3, 10),
            "Difícil": (1000, 5, 50)
        }
        dificuldade = self.dificuldade_combo.currentText()
        self.limite, self.tentativas, self.faixa_proximidade = dificuldades[dificuldade]
        self.palpite_input.setPlaceholderText(f"Digite seu número de 0 a {self.limite}")
        self.iniciar_jogo()

    def iniciar_jogo(self):
        """Inicia um novo jogo."""
        self.numero_sorteado = random.randint(0, self.limite)
        self.tentativas_restantes = self.tentativas
        self.palpite_input.clear()
        self.palpite_input.setStyleSheet("")  # Remove any previous styling
        self.palpite_input.setEnabled(True)  # Reenable the input field
        self.jogar_button.setEnabled(True)  # Reenable the button
        self.mensagem_label.setText(f"Vou pensar em um número entre 0 e {self.limite}. TENTE ADIVINHAR")
        self.mensagem_label.setStyleSheet("")  # Remove any previous styling
        self.resultado_label.setText("")  # Limpa o texto do resultado final

    def fornecer_dica(self, palpite):
        """Fornece uma dica sobre o palpite do usuário, incluindo proximidade."""
        if palpite == self.numero_sorteado:
            return "Você acertou o número!"
        
        dica = "O número é maior." if palpite < self.numero_sorteado else "O número é menor."
        
        if abs(palpite - self.numero_sorteado) <= self.faixa_proximidade:
            dica += " Você está próximo do número."
        else:
            dica += " Você está longe do número."
        
        return dica

    def verificar_palpite(self):
        """Verifica o palpite do usuário e fornece feedback."""
        try:
            palpite = int(self.palpite_input.text())
            if 0 <= palpite <= self.limite:
                if palpite == self.numero_sorteado:
                    self.mensagem_label.setText(f"<b>PARABÉNS! Você acertou!!</b>")
                    self.mensagem_label.setStyleSheet("color: green; font-size: 16px;")
                    self.resultado_label.setText(
                        f"<b>Acertou!</b><br><br>"
                        f"Número Digitado: <span style='font-size: 30px; color: blue;'>{palpite}</span><br>"
                        f"Número Sorteado: <span style='font-size: 30px; color: red;'>{self.numero_sorteado}</span>")
                    self.resultado_label.setStyleSheet("border: 2px solid green; padding: 10px; margin-top: 20px;")
                    self.finalizar_jogo()
                else:
                    self.tentativas_restantes -= 1
                    if self.tentativas_restantes > 0:
                        dica = self.fornecer_dica(palpite)
                        self.mensagem_label.setText(f"<b>ERROU!!</b> {dica} Você tem {self.tentativas_restantes} tentativa(s) restante(s).")
                        self.mensagem_label.setStyleSheet("color: red; font-size: 16px;")
                    else:
                  #      self.mensagem_label.setText(f"<b>FIM DO JOGO!</b> O número era {self.numero_sorteado}.")
                        self.mensagem_label.setText(f"<b>FIM DO JOGO!</b> ")
                        self.mensagem_label.setStyleSheet("color: red; font-size: 16px;")
                        self.resultado_label.setText(
                            f"<b>Errou!</b><br><br>"
                            f"Número Digitado: <span style='font-size: 30px; color: blue;'>{palpite}</span><br>"
                            f"Número Sorteado: <span style='font-size: 30px; color: red;'>{self.numero_sorteado}</span>")
                        self.resultado_label.setStyleSheet("border: 2px solid red; padding: 10px; margin-top: 20px;")
                        self.finalizar_jogo()
            else:
                QMessageBox.warning(self, "Entrada Inválida", f"Por favor, insira um número entre 0 e {self.limite}.")
            self.palpite_input.clear()  # Limpa o campo de palpite após cada tentativa
        except ValueError:
            QMessageBox.warning(self, "Entrada Inválida", "Entrada inválida. Insira um número válido.")

    def finalizar_jogo(self):
        """Desabilita o campo de palpite e o botão de envio quando o jogo termina."""
        self.palpite_input.setStyleSheet("background-color: #FFDDDD;")  # Altera a cor de fundo para vermelho claro
        self.palpite_input.setEnabled(False)  # Desativa o campo de entrada
        self.jogar_button.setEnabled(False)  # Desativa o botão de envio

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jogo = JogoAdivinhacao()
    jogo.show()
    sys.exit(app.exec_())
