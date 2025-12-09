import pandas as pd
from tkinter import Tk, filedialog
import tkinter as tk
import random
import numpy as np
from tkinter import ttk
import math

datos = None


def calcula_mas():
    calculo_mas = tk.Tk()
    calculo_mas.title("Cálculo por MAS")
    calculo_mas.geometry("1000x900")
    datos_mas = datos
    col_var = entrada_var.get()
    tamanio_muestra = int(entrada_tamanio.get())
    longitud_columna = len(datos_mas[col_var])
    mas.destroy()
    unidades_muestra = random.sample(range(1, longitud_columna + 1), tamanio_muestra)
    valores = np.array([datos_mas.iloc[i - 1][col_var] for i in unidades_muestra])
    suma = np.sum(valores)
    cuadrados = valores**2
    suma_cuadrados = np.sum(cuadrados)
    estimador_total = longitud_columna * (suma / tamanio_muestra)
    estimador_promedio = suma / tamanio_muestra
    s_cua_chic = (1 / (tamanio_muestra - 1)) * (
        suma_cuadrados - ((1 / tamanio_muestra) * (suma**2))
    )
    est_var_total = (
        (longitud_columna**2)
        * (1 - (tamanio_muestra / longitud_columna))
        * (s_cua_chic / tamanio_muestra)
    )
    est_var_prom = (1 - (tamanio_muestra / longitud_columna)) * (
        s_cua_chic / tamanio_muestra
    )
    err_est_total = math.sqrt(est_var_total)
    err_est_prom = math.sqrt(est_var_prom)
    inter_conf_total = (1.96) * (err_est_total)
    inter_conf_prom = (1.96) * (err_est_prom)

    ##---------Muestra-------------#
    df_muestra = datos_mas[datos_mas["Id"].isin(unidades_muestra)]
    marco_df_muestra = ttk.LabelFrame(calculo_mas, text="Datos Muestra", padding=10)
    marco_df_muestra.pack(fill="both", expand=True, padx=10, pady=10)
    tabla_muestra = ttk.Treeview(
        marco_df_muestra, columns=list(df_muestra.columns), show="headings", height=5
    )
    tabla_muestra.pack(fill="both", expand=True)
    for col in df_muestra.columns:
        tabla_muestra.heading(col, text=col)
        tabla_muestra.column(col, width=120)
    for _, fila in df_muestra.iterrows():
        tabla_muestra.insert("", "end", values=list(fila))
    scroll_y = ttk.Scrollbar(
        marco_df_muestra, orient="vertical", command=tabla_muestra.yview
    )
    tabla_muestra.configure(yscrollcommand=scroll_y.set)
    scroll_y.pack(side="right", fill="y")
    ##-----------------
    ##-------Resultados
    marco_res = ttk.LabelFrame(calculo_mas, text="Resultados", padding=10)
    marco_res.pack(fill="x", padx=10, pady=10)
    ttk.Label(marco_res, text=f"Estimador Total: {estimador_total}").pack(
        anchor="w", pady=3
    )
    ttk.Label(marco_res, text=f"Estimador Promedio: {estimador_promedio}").pack(
        anchor="w", pady=3
    )
    ttk.Label(
        marco_res,
        text=f"Estimador de Varianza del estimador del total: {est_var_total}",
    ).pack(anchor="w", pady=3)
    ttk.Label(
        marco_res,
        text=f"Estimador de Varianza del estimador del promedio: {est_var_prom}",
    ).pack(anchor="w", pady=3)
    ttk.Label(marco_res, text=f"Estimador Error est Total: {err_est_total}").pack(
        anchor="w", pady=3
    )
    ttk.Label(marco_res, text=f"Estimador Error est promedio: {err_est_prom}").pack(
        anchor="w", pady=3
    )
    ##------------------
    calculo_mas.mainloop()


##Ventana MAS
def est_MAS():
    global entrada_var, entrada_tamanio, mas
    segunda.destroy()
    mas = tk.Tk()
    mas.title("Estimación por MAS")
    mas.geometry("1000x900")
    label_titulo = tk.Label(mas, text="Estimación por Muestreo Aleatorio Simple")
    label_titulo.place(x=20, y=20)
    label_variable_est = tk.Label(mas, text="Nombre de Columna de Variable a estimar")
    label_variable_est.place(x=20, y=40)
    entrada_var = tk.Entry()
    entrada_var.place(x=320, y=40)
    label_tamanio_muestra = tk.Label(mas, text="Tamaño muestra")
    label_tamanio_muestra.place(x=20, y=60)
    entrada_tamanio = tk.Entry()
    entrada_tamanio.place(x=320, y=60)
    boton_calcular = tk.Button(mas, text="Calcular", command=calcula_mas)
    boton_calcular.place(x=20, y=80)
    mas.mainloop()


##Ventana ER
def est_ER():
    global entrada_var, entrada_tamanio, entrada_var_aux, er
    segunda.destroy()
    er = tk.Tk()
    er.title("Estimación por Estimador de Razón")
    er.geometry("1000x900")
    label_titulo = tk.Label(er, text="Estimación por Estimador de Razón")
    label_titulo.place(x=20, y=20)
    label_variable_est = tk.Label(er, text="Nombre de Columna de Variable a estimar")
    label_variable_est.place(x=20, y=40)
    entrada_var = tk.Entry()
    entrada_var.place(x=320, y=40)
    label_variable_aux = tk.Label(er, text="Nombre de Columna Variable auxiliar")
    label_variable_aux.place(x=20, y=60)
    entrada_var_aux = tk.Entry()
    entrada_var_aux.place(x=320, y=60)
    label_tamanio_muestra = tk.Label(er, text="Tamaño muestra")
    label_tamanio_muestra.place(x=20, y=80)
    entrada_tamanio = tk.Entry()
    entrada_tamanio.place(x=320, y=80)
    er.mainloop()


##Ventana EST
def est_EST():
    global entrada_var, entrada_tamanio, entrada_est, est
    segunda.destroy()
    est = tk.Tk()
    est.title("Estimación por Estratificación")
    est.geometry("1000x900")
    label_titulo = tk.Label(est, text="Estimación por Estratificación")
    label_titulo.place(x=20, y=20)
    label_variable_est = tk.Label(est, text="Nombre de Columna de Variable a estimar")
    label_variable_est.place(x=20, y=40)
    entrada_var = tk.Entry()
    entrada_var.place(x=320, y=40)
    label_variable_est = tk.Label(est, text="Nombre de Columna con Estratos")
    label_variable_est.place(x=20, y=60)
    entrada_est = tk.Entry()
    entrada_est.place(x=320, y=60)
    label_tamanio_muestra = tk.Label(est, text="Tamaño muestra")
    label_tamanio_muestra.place(x=20, y=80)
    entrada_tamanio = tk.Entry()
    entrada_tamanio.place(x=320, y=80)
    est.mainloop()


##Ventana Secundaria
def abrir_segunda_ven():
    global segunda
    segunda = tk.Tk()
    segunda.title("Tipo de Estimación a usar")
    segunda.geometry("1000x900")
    label_archivo = tk.Label(segunda, text=f"Archivo cargado: {archivo.split('/')[-1]}")
    label_archivo.place(x=20, y=20)
    label_estrteg = tk.Label(
        segunda,
        text="Selecciona a través de que método quieres realizar la estimación estadística",
    )
    label_estrteg.place(x=20, y=40)
    boton_MAS = tk.Button(segunda, text="Estimación por MAS", command=est_MAS)
    boton_MAS.place(x=20, y=60)
    boton_ER = tk.Button(segunda, text="Estimación por Estimador Razón", command=est_ER)
    boton_ER.place(x=180, y=60)
    boton_EST = tk.Button(
        segunda, text="Estimación por Estratificación", command=est_EST
    )
    boton_EST.place(x=420, y=60)
    segunda.mainloop()


def selecciona_base():
    global datos, archivo
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo CSV o XLSX",
        filetypes=[("Archivos CSV", "*.csv"), ("Archivos Excel", "*.xlsx")],
    )
    if not archivo:
        return
    if archivo.endswith(".csv"):
        datos = pd.read_csv(archivo)
    else:
        datos = pd.read_excel(archivo)
    root.destroy()
    abrir_segunda_ven()


##Ventana Principal
root = tk.Tk()
root.title("Calculadora estadística")
root.geometry("1000x900")
etiqueta_sele = tk.Label(root, text="Selecciona Base de Datos a analizar")
etiqueta_sele.place(x=20, y=20)
boton_selec = tk.Button(root, text="Seleccionar", command=selecciona_base)
boton_selec.place(x=100, y=100)
root.mainloop()
