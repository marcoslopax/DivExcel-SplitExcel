DivExcel

Descrição / Description

O DivExcel é um programa em Python que divide arquivos Excel grandes em partes menores, baseado em um tamanho máximo especificado. O programa lê arquivos .xlsx de uma pasta de entrada, divide cada arquivo e salva as partes divididas em uma pasta de saída. O programa possui duas versões: uma versão com interface gráfica e outra baseada em configuração por arquivo JSON e logs automáticos.
DivExcel is a Python program that splits large Excel files into smaller parts based on a specified maximum size. The program reads .xlsx files from an input folder, divides each file, and saves the divided parts into an output folder. The program has two versions: one with a graphical interface and another based on JSON configuration file and automatic logging.

Configuração / Configuration

Versão com Arquivo de Configuração / Configuration File Version

Crie um arquivo config.json na pasta Config com o seguinte conteúdo:
Create a config.json file in the Config folder with the following content:

{
    "input_folder": "input/path",
    "output_folder": "output/path",
    "max_file_size_mb": 15
}

Versão com Interface Gráfica / Graphical Interface Version

Use a interface gráfica para selecionar as pastas de entrada e saída e definir o tamanho máximo dos arquivos divididos.
Use the graphical interface to select the input and output folders and set the maximum size of the split files.

Requisitos / Requirements

Python 3.x
Pandas
Tkinter (para a versão com interface gráfica)

Você pode instalar os requisitos necessários com o seguinte comando:
You can install the required dependencies with the following command:

pip install pandas

Uso / Usage

Versão com Arquivo de Configuração / Configuration File Version

Execute o programa principal:
Run the main program:

python divexcel.py

Versão com Interface Gráfica / Graphical Interface Version

Execute a interface gráfica:
Run the graphical interface:

python config_interface.py

Logs (somente para a versão com arquivo de configuração) / Logs (for configuration file version only)

Os logs do processo de divisão de arquivos serão armazenados na pasta Log. Logs antigos (com mais de 30 dias) serão excluídos automaticamente.
The logs of the file splitting process will be stored in the Log folder. Old logs (older than 30 days) will be automatically deleted.

Instruções / Instructions

Versão com Arquivo de Configuração / Configuration File Version

Configuração: Certifique-se de que o arquivo config.json está corretamente preenchido com os caminhos das pastas de entrada e saída, bem como o tamanho máximo desejado para cada arquivo dividido.
Configuration: Ensure that the config.json file is correctly filled with the input and output folder paths, as well as the desired maximum size for each split file.

Execute o Programa: Inicie o programa para dividir os arquivos Excel na pasta de entrada.
Run the Program: Start the program to split the Excel files in the input folder.

Versão com Interface Gráfica / Graphical Interface Version

Selecione a Pasta de Entrada: Clique no botão "Navegar" próximo ao campo "Pasta de Entrada" e selecione a pasta que contém os arquivos .xlsx que você deseja dividir.
Select Input Folder: Click the "Browse" button next to the "Input Folder" field and select the folder containing the .xlsx files you want to split.

Selecione a Pasta de Saída: Clique no botão "Navegar" próximo ao campo "Pasta de Saída" e selecione a pasta onde os arquivos divididos serão salvos.
Select Output Folder: Click the "Browse" button next to the "Output Folder" field and select the folder where the split files will be saved.

Defina o Tamanho Máximo por Arquivo (MB): Insira o tamanho máximo desejado para cada arquivo dividido em megabytes.
Set Maximum File Size (MB): Enter the desired maximum size for each split file in megabytes.

Salvar Configuração: Clique no botão "Salvar Configuração" para salvar as configurações no arquivo config.json.
Save Configuration: Click the "Save Configuration" button to save the settings in the config.json file.

Nota / Note

Este programa foi desenvolvido para simplificar o processo de divisão de grandes arquivos Excel, proporcionando duas opções de uso: uma com interface amigável e intuitiva, e outra com configuração automatizada e logging. O tamanho dos arquivos divididos é definido nas configurações fornecidas.
This program was developed to simplify the process of splitting large Excel files, providing two usage options: one with a user-friendly and intuitive interface, and another with automated configuration and logging. The size of the split files is defined in the provided settings.