import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from datetime import datetime
import os

import Helpers


OUTPUT_FILE_PATH="salida/"


def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    # input("Enter para continuar ->")
    
    Helpers.printLine(30,3)
    
    
    unique_meal_plans=[]
    meals_included_count=0
    
    filePaths=(filedialog.askopenfilenames(title=f"Selecciona los archivos"))

    for path in filePaths:
        file = Path(path)
        
        if (file.suffix.lower()==".xml"):
            tree = ET.parse(file)
            root = tree.getroot()

            for elem in root.iter():
                if "MealsIncluded" in elem.tag:
                    meals_included_count += 1
                    # Extraer el valor de MealPlanCodes
                    meal_plan_code = elem.attrib.get("MealPlanCodes")
                    # Agregar solo valores únicos
                    if meal_plan_code and meal_plan_code not in unique_meal_plans:
                        unique_meal_plans.append(meal_plan_code)


    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"results_{timestamp}.txt"
    
    os.makedirs(OUTPUT_FILE_PATH, exist_ok=True)
    file_path=OUTPUT_FILE_PATH+"salida_"+filename
    with open(file_path, "w") as file_out:
        file_out.write("Files Scanned: "+", ".join(filePaths)+"\n")
        file_out.write(f"Meals Included Count: {meals_included_count}\n")
        file_out.write("Unique Meal Plans:\n" + "\n".join(unique_meal_plans) + "\n")
        
    print(f"Se han guardado los resultados de la busqueda en {file_path}")



if __name__=="__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()