import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Importa o módulo ttk para a barra de progresso / Imports the ttk module for the progress bar
from threading import Thread, Event

class FileDivider:
    def __init__(self, root):
        # Configurações da interface gráfica / GUI setup
        self.root = root
        self.root.title("Divisor de Arquivos Excel")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Configuração dos componentes da interface gráfica / GUI components setup
        self.input_folder_label = tk.Label(root, text="Pasta de Entrada:")
        self.input_folder_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.input_folder_entry = tk.Entry(root, width=50)
        self.input_folder_entry.grid(row=0, column=1, padx=5, pady=5)
        self.input_folder_button = tk.Button(root, text="Navegar", command=self.select_input_folder)
        self.input_folder_button.grid(row=0, column=2, padx=5, pady=5)

        self.output_folder_label = tk.Label(root, text="Pasta de Saída:")
        self.output_folder_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.output_folder_entry = tk.Entry(root, width=50)
        self.output_folder_entry.grid(row=1, column=1, padx=5, pady=5)
        self.output_folder_button = tk.Button(root, text="Navegar", command=self.select_output_folder)
        self.output_folder_button.grid(row=1, column=2, padx=5, pady=5)

        self.max_file_size_label = tk.Label(root, text="Tamanho máximo por Arquivo (MB):")
        self.max_file_size_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.max_file_size_entry = tk.Entry(root, width=20)
        self.max_file_size_entry.grid(row=2, column=1, padx=5, pady=5)

        self.start_button = tk.Button(root, text="Iniciar Processamento", command=self.start_processing)
        self.start_button.grid(row=3, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(root, text="Parar Processamento", command=self.stop_processing)
        self.stop_button.grid(row=3, column=1, padx=5, pady=5)

        self.status_label = tk.Label(root, text="")
        self.status_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
        self.progress_bar.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W+tk.E)

        self.pasta_entrada = ""
        self.pasta_saida = ""
        self.stop_event = None
        self.processing_thread = None

    def select_input_folder(self):
        # Abre o diálogo para selecionar a pasta de entrada / Opens the dialog to select the input folder
        self.pasta_entrada = filedialog.askdirectory()
        self.input_folder_entry.delete(0, tk.END)
        self.input_folder_entry.insert(0, self.pasta_entrada)

    def select_output_folder(self):
        # Abre o diálogo para selecionar a pasta de saída / Opens the dialog to select the output folder
        self.pasta_saida = filedialog.askdirectory()
        self.output_folder_entry.delete(0, tk.END)
        self.output_folder_entry.insert(0, self.pasta_saida)

    def divide_arquivo_excel(self, arquivo_entrada, tamanho_pedaco_mb):
        # Divide o arquivo Excel em partes menores / Splits the Excel file into smaller parts
        tamanho_arquivo_bytes = os.path.getsize(arquivo_entrada)
        tamanho_pedaco_bytes = tamanho_pedaco_mb * 1024 * 1024
        num_pedacos = tamanho_arquivo_bytes // tamanho_pedaco_bytes + 1
        df = pd.read_excel(arquivo_entrada)
        linhas_por_pedaco = len(df) // num_pedacos
        
        for i in range(num_pedacos):
            if self.stop_event.is_set():
                break
            pedaco_inicial = i * linhas_por_pedaco
            pedaco_final = min((i + 1) * linhas_por_pedaco, len(df))
            pedaco = df.iloc[pedaco_inicial:pedaco_final]
            arquivo_saida = os.path.join(self.pasta_saida, f"{os.path.splitext(os.path.basename(arquivo_entrada))[0]}_pedaco_{i + 1}.xlsx")
            pedaco.to_excel(arquivo_saida, index=False)
            
            # Atualiza a barra de progresso / Updates the progress bar
            progresso_atual = (i + 1) * 100 / num_pedacos
            self.progress_bar['value'] = progresso_atual
            self.root.update_idletasks()

    def start_processing(self):
        # Inicia o processamento dos arquivos / Starts the file processing
        self.pasta_entrada = self.input_folder_entry.get()
        self.pasta_saida = self.output_folder_entry.get()
        tamanho_pedaco_str = self.max_file_size_entry.get()

        # Verifica se os campos de entrada estão vazios / Checks if input fields are empty
        if not self.pasta_entrada or not self.pasta_saida or not tamanho_pedaco_str:
            self.status_label.config(text="Por favor, preencha todos os campos.")
            return

        # Verifica se o tamanho do pedaço é um número válido / Checks if the piece size is a valid number
        try:
            tamanho_pedaco_mb = int(tamanho_pedaco_str)
        except ValueError:
            self.status_label.config(text="Por favor, insira um valor numérico para o tamanho máximo por arquivo.")
            return

        # Se tudo estiver ok, continua com o processamento / If everything is okay, continues with the processing
        self.stop_event = Event()
        self.status_label.config(text="Processamento em andamento...")

        def process_files():
            # Processa cada arquivo na pasta de entrada / Processes each file in the input folder
            for arquivo_entrada in os.listdir(self.pasta_entrada):
                if self.stop_event.is_set():
                    break
                if arquivo_entrada.endswith(".xlsx"):
                    arquivo_entrada = os.path.join(self.pasta_entrada, arquivo_entrada)
                    self.divide_arquivo_excel(arquivo_entrada, tamanho_pedaco_mb)
            self.status_label.config(text="Processamento concluído.")  # Updates status after processing

        self.processing_thread = Thread(target=process_files)
        self.processing_thread.start()

    def stop_processing(self):
        # Interrompe o processamento / Stops the processing
        if self.processing_thread and self.processing_thread.is_alive():
            self.stop_event.set()
            self.status_label.config(text="Processamento interrompido.")

    def on_closing(self):
        # Função de encerramento do programa / Program closing function
        self.stop_processing()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDivider(root)
    root.mainloop()
