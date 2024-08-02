import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QLabel, QFormLayout
)
from PyQt5.QtGui import QFont, QDoubleValidator
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class FuelCostCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora de Custo de Combustível')
        self.setGeometry(100, 100, 600, 700)
        self.initUI()

    def initUI(self):
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layouts
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        button_layout = QHBoxLayout()

        # Input Fields
        self.fuel_value_input = QLineEdit(self)
        self.fuel_value_input.setPlaceholderText("Digite o Valor do Combustível (ex: 5,90)")
        self.fuel_value_input.setValidator(QDoubleValidator(0, 9999.99, 2))
        self.fuel_value_input.editingFinished.connect(self.format_fuel_value)

        self.km_per_liter_input = QLineEdit(self)
        self.km_per_liter_input.setPlaceholderText("Digite Quantos KM seu carro faz por litro")
        self.km_per_liter_input.setValidator(QDoubleValidator(0, 9999.99, 2))

        self.distance_input = QLineEdit(self)
        self.distance_input.setPlaceholderText("Qual a distância percorrida")
        self.distance_input.setValidator(QDoubleValidator(0, 9999.99, 2))

        self.fuel_type_input = QLineEdit(self)
        self.fuel_type_input.setPlaceholderText(
            "Quao o Combustivel : 1.Etanol 2.Gasolina 3.Gasolina Aditivada 4.Outros"   )

        # Form Layout
        form_layout.addRow(QLabel("Valor do Combustível:"), self.fuel_value_input)
        form_layout.addRow(QLabel("KM por Litro:"), self.km_per_liter_input)
        form_layout.addRow(QLabel("Distância Percorrida:"), self.distance_input)
        form_layout.addRow(QLabel("Tipo de Combustível:"), self.fuel_type_input)

        # Buttons
        self.calculate_button = QPushButton('Calcular', self)
        self.calculate_button.clicked.connect(self.calculate_cost)
        button_layout.addWidget(self.calculate_button)

        self.new_query_button = QPushButton('Nova Consulta', self)
        self.new_query_button.clicked.connect(self.clear_fields)
        button_layout.addWidget(self.new_query_button)

        self.exit_button = QPushButton('Sair', self)
        self.exit_button.clicked.connect(self.close)
        self.exit_button.setStyleSheet('background-color: red; color: white;')
        button_layout.addWidget(self.exit_button)

        # Result Label
        self.result_label = QLabel('', self)
        self.result_label.setFont(QFont('Arial', 12))
        self.result_label.setAlignment(Qt.AlignCenter)

        # Matplotlib Figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Add Widgets to Main Layout
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.canvas)

        # Set Layout
        central_widget.setLayout(main_layout)

    def format_fuel_value(self):
        text = self.fuel_value_input.text()
        if not text:
            return
        
        clean_text = text.replace('R$ ', '').replace('.', '').replace(',', '.')
        
        try:
            float_value = float(clean_text)
            formatted_text = f'R$ {float_value:,.2f}'.replace('.', ',')
            self.fuel_value_input.setText(formatted_text)
        except ValueError:
            self.fuel_value_input.setText(text)

    def calculate_cost(self):
        try:
            valor_combustivel_text = self.fuel_value_input.text().replace('R$ ', '').replace('.', '').replace(',', '.')
            valor_combustivel = float(valor_combustivel_text)
            km_por_litros = float(self.km_per_liter_input.text())
            distancia_em_km = float(self.distance_input.text())
            tipo_combustivel = self.fuel_type_input.text().strip()

            fuel_types = { '1': 'Etanol',
                '2': 'Gasolina',
                '3': 'Gasolina Aditivada',
                '4': 'Outros'
            }

            if tipo_combustivel in fuel_types:
                fuel_type = fuel_types[tipo_combustivel]
            else:
                self.result_label.setText(
                    'Opção inválida! Digite um dos números abaixo:\n'
                    '1 para Etanol\n'
                    '2 para Gasolina\n'
                    '3 para Gasolina Aditivada\n'
                    '4 para Outros'
                )
                return

            litros_consumidos = int(distancia_em_km // km_por_litros)  # Use integer division
            valor_gasto = litros_consumidos * valor_combustivel

            self.result_label.setText(
                f'Valor gasto com {fuel_type}: R$ {valor_gasto:.2f}\n'
                f'Gastou: {litros_consumidos} litros com {fuel_type}'
            )

            self.plot_graph(litros_consumidos, valor_gasto, fuel_type)
        except ValueError:
            self.result_label.setText('Por favor, insira valores válidos.')

    def plot_graph(self, litros_consumidos, valor_gasto, fuel_type):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(['Litros Consumidos', 'Valor Gasto'], [litros_consumidos, valor_gasto], color=['blue', 'green'])
        ax.set_ylabel('Valor')
        ax.set_title(f'Gasto com {fuel_type}')
        ax.set_ylim(0, max(litros_consumidos, valor_gasto) * 1.1)
        self.canvas.draw()

    def clear_fields(self):
        self.fuel_value_input.clear()
        self.km_per_liter_input.clear()
        self.distance_input.clear()
        self.fuel_type_input.clear()
        self.result_label.clear()
        self.figure.clear()
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = FuelCostCalculator()
    mainWin.show()
    sys.exit(app.exec_())
