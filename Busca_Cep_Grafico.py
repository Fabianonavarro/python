import tkinter as tk
from tkinter import messagebox
import requests
from datetime import date

class CepApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta CEP")
        
        # Definindo a dimensão da janela
        self.root.geometry("500x300")
        
        self.create_widgets()
        self.update_date()
    
    def create_widgets(self):
        # Configura o label da data
        self.date_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.date_label.pack(pady=10)
        
        # Configura o label e a entrada de CEP
        self.cep_label = tk.Label(self.root, text="Digite o CEP:", font=("Arial", 12))
        self.cep_label.pack()
        
        self.cep_entry = tk.Entry(self.root, font=("Arial", 12))
        self.cep_entry.pack(pady=5)
        
        # Configura os botões de consulta, nova consulta e sair entre os dados e a área de resultados
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        # Botão Consultar
        self.search_button = tk.Button(button_frame, text="Consultar", font=("Arial", 12), command=self.consultar_cep)
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        # Botão Nova Consulta
        self.new_search_button = tk.Button(button_frame, text="Nova Consulta", font=("Arial", 12), command=self.clear)
        self.new_search_button.pack(side=tk.LEFT, padx=5)
        
        # Botão Sair
        self.exit_button = tk.Button(button_frame, text="Sair", font=("Arial", 12), command=self.quit_app, bg="red", fg="white")
        self.exit_button.pack(side=tk.LEFT, padx=5)
        
        # Configura a área de texto para exibir resultados com cor de fundo azul claro
        self.result_text = tk.Text(self.root, height=8, width=60, font=("Arial", 12), wrap=tk.WORD, bg="#e0f7fa")
        self.result_text.pack(pady=10)
    
    def update_date(self):
        current_date = date.today()
        formatted_date = current_date.strftime('%d/%m/%Y')
        self.date_label.config(text=f"Data: {formatted_date}")
    
    def consultar_cep(self):
        cep_input = self.cep_entry.get().strip()
        
        if len(cep_input) != 8 or not cep_input.isdigit():
            messagebox.showerror("Erro", "Quantidade de dígitos inválida ou o CEP contém caracteres não numéricos!")
            return
        
        try:
            response = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
            busca_cep = response.json()
            
            if "erro" not in busca_cep:
                result = (f"CEP: {busca_cep['cep']}\n"
                          f"Endereco: {busca_cep['logradouro']}\n"
                          f"Bairro: {busca_cep['bairro']}\n"
                          f"Cidade: {busca_cep['localidade']}\n"
                          f"Estado: {busca_cep['uf']}")
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, result)
            else:
                messagebox.showerror("Erro", f"Este CEP {cep_input} é inválido. Favor verificar.")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar o CEP: {e}")
    
    def clear(self):
        self.cep_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
    
    def quit_app(self):
        if messagebox.askyesno("Sair", "Você realmente deseja sair?"):
            self.root.destroy()  # Corrige a funcionalidade para fechar a janela

if __name__ == "__main__":
    root = tk.Tk()
    app = CepApp(root)
    root.mainloop()
