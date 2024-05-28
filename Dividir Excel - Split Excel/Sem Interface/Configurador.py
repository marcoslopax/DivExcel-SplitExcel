import os
import json
import tkinter as tk
from tkinter import filedialog

class FileDividerConfigurator:
    def __init__(self, root):
        self.root = root
        self.root.title("Configurador de Divisor de Arquivos Excel")  # Title for the application window / Título para a janela da aplicação

        # Labels and entry widgets for input folder selection / Etiquetas e widgets de entrada para seleção de pasta de entrada
        self.input_folder_label = tk.Label(root, text="Pasta de Entrada:")
        self.input_folder_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.input_folder_entry = tk.Entry(root, width=50)
        self.input_folder_entry.grid(row=0, column=1, padx=5, pady=5)
        self.input_folder_button = tk.Button(root, text="Navegar", command=self.select_input_folder)
        self.input_folder_button.grid(row=0, column=2, padx=5, pady=5)

        # Labels and entry widgets for output folder selection / Etiquetas e widgets de entrada para seleção de pasta de saída
        self.output_folder_label = tk.Label(root, text="Pasta de Saída:")
        self.output_folder_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.output_folder_entry = tk.Entry(root, width=50)
        self.output_folder_entry.grid(row=1, column=1, padx=5, pady=5)
        self.output_folder_button = tk.Button(root, text="Navegar", command=self.select_output_folder)
        self.output_folder_button.grid(row=1, column=2, padx=5, pady=5)

        # Label and entry widget for maximum file size / Etiqueta e widget de entrada para tamanho máximo de arquivo
        self.max_file_size_label = tk.Label(root, text="Tamanho máximo por Arquivo (MB):")
        self.max_file_size_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.max_file_size_entry = tk.Entry(root, width=20)
        self.max_file_size_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button to save configuration / Botão para salvar configuração
        self.save_button = tk.Button(root, text="Salvar Configuração", command=self.save_configuration)
        self.save_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # Label to display status or error messages / Etiqueta para exibir status ou mensagens de erro
        self.status_label = tk.Label(root, text="")
        self.status_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def select_input_folder(self):
        folder = filedialog.askdirectory()
        self.input_folder_entry.delete(0, tk.END)
        self.input_folder_entry.insert(0, folder)

    def select_output_folder(self):
        folder = filedialog.askdirectory()
        self.output_folder_entry.delete(0, tk.END)
        self.output_folder_entry.insert(0, folder)

    def save_configuration(self):
        config = {
            'input_folder': self.input_folder_entry.get(),
            'output_folder': self.output_folder_entry.get(),
            'max_file_size_mb': self.max_file_size_entry.get()
        }

        # Check if input fields are empty / Verifica se os campos de entrada estão vazios
        if not config['input_folder'] or not config['output_folder'] or not config['max_file_size_mb']:
            self.status_label.config(text="Por favor, preencha todos os campos.")  # Please fill in all fields
            return

        # Check if the file size is a valid number / Verifica se o tamanho do arquivo é um número válido
        try:
            config['max_file_size_mb'] = int(config['max_file_size_mb'])
        except ValueError:
            self.status_label.config(text="Por favor, insira um valor numérico para o tamanho máximo por arquivo.")  # Please enter a numerical value for maximum file size
            return

        # Define the path to the 'Config' folder and the 'config.json' file / Define o caminho para a pasta 'Config' e o arquivo 'config.json'
        config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config')
        os.makedirs(config_dir, exist_ok=True)
        config_path = os.path.join(config_dir, 'config.json')

        with open(config_path, 'w') as config_file:
            json.dump(config, config_file)

        self.status_label.config(text=f"Configuração salva com sucesso em {config_path}.")  # Configuration saved successfully at

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDividerConfigurator(root)
    root.mainloop()
