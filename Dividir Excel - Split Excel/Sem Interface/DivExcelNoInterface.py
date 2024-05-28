import os
import json
import pandas as pd
import logging
from threading import Event, Thread
from datetime import datetime, timedelta

class FileDividerExecutor:
    def __init__(self):
        # Define the path to the 'Config' folder and 'config.json' file
        # Define o caminho para a pasta 'Config' e o arquivo 'config.json'
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config', 'config.json')
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

        # Define input and output folder paths and max file size in MB
        # Define os caminhos das pastas de entrada e saída e o tamanho máximo do arquivo em MB
        self.pasta_entrada = config['input_folder']
        self.pasta_saida = config['output_folder']
        self.tamanho_pedaco_mb = config['max_file_size_mb']
        self.stop_event = Event()

        # Set up logging configuration
        # Configura a configuração de logging
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Log')
        os.makedirs(log_dir, exist_ok=True)
        self.log_path = os.path.join(log_dir, 'file_divider.log')

        logging.basicConfig(filename=self.log_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def divide_arquivo_excel(self, arquivo_entrada, tamanho_pedaco_mb):
        try:
            # Calculate file size in bytes and number of parts
            # Calcula o tamanho do arquivo em bytes e o número de partes
            tamanho_arquivo_bytes = os.path.getsize(arquivo_entrada)
            tamanho_pedaco_bytes = tamanho_pedaco_mb * 1024 * 1024
            num_pedacos = tamanho_arquivo_bytes // tamanho_pedaco_bytes + 1
            
            # Read Excel file into a DataFrame
            # Lê o arquivo Excel em um DataFrame
            df = pd.read_excel(arquivo_entrada)
            linhas_por_pedaco = len(df) // num_pedacos

            for i in range(num_pedacos):
                if self.stop_event.is_set():
                    break
                
                # Determine the start and end of each part
                # Determina o início e o fim de cada parte
                pedaco_inicial = i * linhas_por_pedaco
                pedaco_final = min((i + 1) * linhas_por_pedaco, len(df))
                pedaco = df.iloc[pedaco_inicial:pedaco_final]
                
                # Save each part as a new Excel file
                # Salva cada parte como um novo arquivo Excel
                arquivo_saida = os.path.join(self.pasta_saida, f"{os.path.splitext(os.path.basename(arquivo_entrada))[0]}_pedaco_{i + 1}.xlsx")
                pedaco.to_excel(arquivo_saida, index=False)
        except Exception as e:
            logging.error(f"Erro ao dividir o arquivo {arquivo_entrada}: {str(e)}")

    def start_processing(self):
        try:
            for arquivo_entrada in os.listdir(self.pasta_entrada):
                if self.stop_event.is_set():
                    break
                
                # Check if the file is an Excel file
                # Verifica se o arquivo é um arquivo Excel
                if arquivo_entrada.endswith(".xlsx"):
                    arquivo_entrada = os.path.join(self.pasta_entrada, arquivo_entrada)
                    logging.info(f'Dividindo arquivo {arquivo_entrada}')
                    self.divide_arquivo_excel(arquivo_entrada, self.tamanho_pedaco_mb)
                    
                    # Remove the file after splitting
                    # Remove o arquivo após a divisão
                    os.remove(arquivo_entrada)
            logging.info("Processamento concluído.")
        except Exception as e:
            logging.error(f"Erro durante o processamento: {str(e)}")
        finally:
            self.delete_old_logs()

    def delete_old_logs(self):
        try:
            # Delete logs older than 30 days
            # Exclui logs com mais de 30 dias
            thirty_days_ago = datetime.now() - timedelta(days=30)
            for filename in os.listdir(os.path.dirname(self.log_path)):
                file_path = os.path.join(os.path.dirname(self.log_path), filename)
                if os.path.isfile(file_path):
                    creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                    if creation_time < thirty_days_ago:
                        os.remove(file_path)
        except Exception as e:
            logging.error(f"Erro ao excluir logs antigos: {str(e)}")

    def stop_processing(self):
        # Signal to stop the processing
        # Sinaliza para parar o processamento
        self.stop_event.set()

if __name__ == "__main__":
    # Create an instance of FileDividerExecutor
    # Cria uma instância do FileDividerExecutor
    executor = FileDividerExecutor()
    
    # Start the processing in a separate thread
    # Inicia o processamento em uma thread separada
    processing_thread = Thread(target=executor.start_processing)
    processing_thread.start()
    processing_thread.join()
