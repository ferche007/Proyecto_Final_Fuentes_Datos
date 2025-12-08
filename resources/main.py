import pandas as pd
from tkinter import Tk, filedialog


Tk().withdraw()


archivo = filedialog.askopenfilename(
    title="Selecciona un archivo CSV o XLSX",
    filetypes=[("Archivos CSV", "*.csv"), ("Archivos Excel", "*.xlsx")],
)

if not archivo:
    print("No seleccionaste archivo")
    exit()


if archivo.endswith(".csv"):
    df = pd.read_csv(archivo)
else:
    df = pd.read_excel(archivo)

print("Archivo cargado correctamente")
print(df.head())
