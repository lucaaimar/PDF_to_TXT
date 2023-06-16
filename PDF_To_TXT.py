import os
import subprocess

# Percorso dell'eseguibile pdftotext
pdftotext_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdftotext")

# Directory dei file PDF
directory = "./PDF"

# Percorso e nome del file di output
output_file = "./affido.txt"

# Lista dei file PDF nella directory
file_list = [file for file in os.listdir(directory) if file.endswith(".pdf")]

# Esegui pdftotext per mantenere la disposizione del testo nello spazio
for file_name in file_list:
    file_path = os.path.join(directory, file_name)
    output_path = os.path.join(directory, file_name.replace(".pdf", ".txt"))
    command = [pdftotext_path, '-layout', file_path, output_path]
    subprocess.run(command)

# Unisci i file di output in un unico file
with open(output_file, "w", encoding="utf-8") as output:
    for file_name in file_list:
        file_path = os.path.join(directory, file_name.replace(".pdf", ".txt"))
        with open(file_path, "r", encoding="latin-1") as file:
            output.write(file.read() + "\n\n")
        os.remove(file_path)  # Rimuovi i file temporanei di output

print("Trasformazione completata. Il testo è stato scritto in", output_file)
