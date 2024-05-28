DivExcel com Interface Gráfica

Descrição / Description
O DivExcel é um programa em Python que divide arquivos Excel grandes em partes menores, baseado em um tamanho máximo especificado pelo usuário na interface gráfica. O programa lê arquivos .xlsx de uma pasta de entrada, divide cada arquivo e salva as partes divididas em uma pasta de saída.
DivExcel is a Python program that splits large Excel files into smaller parts based on a user-specified maximum size through the graphical interface. The program reads .xlsx files from an input folder, divides each file, and saves the divided parts into an output folder.

Requisitos / Requirements
Python 3.x
Pandas
Tkinter

Você pode instalar os requisitos necessários com o seguinte comando:
You can install the required dependencies with the following command:

pip install pandas

Execute o programa principal:
Run the main program:

python DivExcel.py

Instruções / Instructions

Selecione a Pasta de Entrada: Clique no botão "Navegar" próximo ao campo "Pasta de Entrada" e selecione a pasta que contém os arquivos .xlsx que você deseja dividir.
Select Input Folder: Click the "Browse" button next to the "Input Folder" field and select the folder containing the .xlsx files you want to split.

Selecione a Pasta de Saída: Clique no botão "Navegar" próximo ao campo "Pasta de Saída" e selecione a pasta onde os arquivos divididos serão salvos.
Select Output Folder: Click the "Browse" button next to the "Output Folder" field and select the folder where the split files will be saved.

Defina o Tamanho Máximo por Arquivo (MB): Insira o tamanho máximo desejado para cada arquivo dividido em megabytes.
Set Maximum File Size (MB): Enter the desired maximum size for each split file in megabytes.

Inicie o Processamento: Clique no botão "Iniciar Processamento" para começar a dividir os arquivos.
Start Processing: Click the "Start Processing" button to begin splitting the files.

Pare o Processamento: Clique no botão "Parar Processamento" para interromper o processo de divisão de arquivos a qualquer momento.
Stop Processing: Click the "Stop Processing" button to interrupt the file splitting process at any time.

Acompanhe o Progresso: A barra de progresso e a etiqueta de status mostrarão o andamento do processo de divisão dos arquivos.
Monitor Progress: The progress bar and status label will show the progress of the file splitting process.

Nota / Note

Este programa foi desenvolvido para simplificar o processo de divisão de grandes arquivos Excel, proporcionando uma interface amigável e intuitiva. O tamanho dos arquivos divididos é definido pelo usuário diretamente na interface gráfica.
This program was developed to simplify the process of splitting large Excel files, providing a user-friendly and intuitive interface. The size of the split files is defined by the user directly through the graphical interface.