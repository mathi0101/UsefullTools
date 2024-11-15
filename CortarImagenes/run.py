from PIL import Image
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from datetime import datetime
import os


OUTPUT_FILE_PATH="salida/"


def main():
    os.makedirs(OUTPUT_FILE_PATH, exist_ok=True)
    root = tk.Tk()
    root.withdraw()  
    # Cargar la imagen
    image_path = filedialog.askopenfilename(title=f"Selecciona la imagen")
    image = Image.open(image_path)

    # Obtener las dimensiones de la imagen
    image_width, image_height = image.size

    # Configurar el número de filas y columnas
    num_rows = 5
    num_cols = 12

    # Calcular el tamaño de cada carta
    card_width = image_width // num_cols
    card_height = image_height // num_rows

    # Crear cada carta como un archivo PNG por separado
    output_paths = []
    palos = ['o','c','e','b','x']
    for row in range(num_rows):
        for col in range(num_cols):
            left = col * card_width
            top = row * card_height
            right = left + card_width
            bottom = top + card_height

            card = image.crop((left, top, right, bottom))
            output_path = f'{OUTPUT_FILE_PATH}/carta_{col+1}_{palos[row]}.png'
            card.save(output_path)
            output_paths.append(output_path)

    

if __name__=="__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()