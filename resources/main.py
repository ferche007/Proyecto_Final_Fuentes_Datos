import pandas as pd
from tkinter import Tk, filedialog
import tkinter as tk
import random
import numpy as np
from tkinter import ttk
import math

datos = None


##Calculo MAS
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


##Calculo ER
def calcula_er():
    calculo_er = tk.Tk()
    calculo_er.title("Cálculo por Estimador Razón")
    calculo_er.geometry("1000x900")
    datos_er = datos
    col_var = entrada_var.get()
    col_var_aux = entrada_var_aux.get()
    tamanio_muestra = int(entrada_tamanio.get())
    longitud_columna = len(datos_er[col_var])
    er.destroy()
    unidades_muestra = random.sample(range(1, longitud_columna + 1), tamanio_muestra)
    valores_prim = np.array([datos_er.iloc[i - 1][col_var] for i in unidades_muestra])
    valores_aux = np.array(
        [datos_er.iloc[j - 1][col_var_aux] for j in unidades_muestra]
    )
    valor_cruz = valores_prim * valores_aux
    sum_valor_cruz = np.sum(valor_cruz)
    sum_primarios = np.sum(valores_prim)
    sum_aux = np.sum(valores_aux)
    cuadrados = valores_prim**2
    cuadrados_aux = valores_aux**2
    sum_cua_prim = np.sum(cuadrados)
    sum_cua_aux = np.sum(cuadrados_aux)
    aux_total = datos_er[col_var_aux].sum()
    aux_prom = aux_total / longitud_columna
    r_gorr = sum_primarios / sum_aux
    est_total = (aux_total) * (sum_primarios / sum_aux)
    est_promedio = (aux_prom) * (sum_primarios / sum_aux)
    sr_chic = (1 / (tamanio_muestra - 1)) * (
        sum_cua_prim - (2 * r_gorr * (sum_valor_cruz)) + ((r_gorr**2) * sum_cua_aux)
    )
    var_total = (
        (longitud_columna**2)
        * (1 - (tamanio_muestra / longitud_columna))
        * (sr_chic / tamanio_muestra)
    )
    var_prom = (1 - (tamanio_muestra / longitud_columna)) * (sr_chic / tamanio_muestra)
    err_est_total = math.sqrt(var_total)
    err_est_prom = math.sqrt(var_prom)
    ##---------Muestra-------------#
    df_muestra = datos_er[datos_er["Id"].isin(unidades_muestra)]
    marco_df_muestra = ttk.LabelFrame(calculo_er, text="Datos Muestra", padding=10)
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
    marco_res = ttk.LabelFrame(calculo_er, text="Resultados", padding=10)
    marco_res.pack(fill="x", padx=10, pady=10)
    ttk.Label(marco_res, text=f"Estimador Total: {est_total}").pack(anchor="w", pady=3)
    ttk.Label(marco_res, text=f"Estimador Promedio: {est_promedio}").pack(
        anchor="w", pady=3
    )
    ttk.Label(
        marco_res,
        text=f"Estimador de Varianza del estimador del total: {var_total}",
    ).pack(anchor="w", pady=3)
    ttk.Label(
        marco_res,
        text=f"Estimador de Varianza del estimador del promedio: {var_prom}",
    ).pack(anchor="w", pady=3)
    ttk.Label(marco_res, text=f"Estimador Error est Total: {err_est_total}").pack(
        anchor="w", pady=3
    )
    ttk.Label(marco_res, text=f"Estimador Error est promedio: {err_est_prom}").pack(
        anchor="w", pady=3
    )
    ##------------------
    calculo_er.mainloop()


def calcula_est():
    calculo_est = tk.Tk()
    calculo_est.title("Cálculo por Estimador Razón")
    calculo_est.geometry("1000x900")
    datos_est = datos
    col_var = entrada_var.get()
    longitud_columna = len(datos_est[col_var])
    tamanio_muestra = int(entrada_tamanio.get())
    col_estratos = entrada_est.get()
    estratos = estratos = [
        x.strip() for x in entrada_estratos_cu.get().strip("()").split(",")
    ]
    est.destroy()
    num_cada_est = []
    df_estratos = []
    for i in estratos:
        numero = (datos_est[col_estratos].astype(str) == i).sum()
        num_cada_est.append(numero)
        df_estratos.append(datos_est[datos_est[col_estratos].astype(str) == i])
    n_prop_est = []
    for j in num_cada_est:
        n_prop = tamanio_muestra * (j / longitud_columna)
        n_prop_est.append(n_prop)
    muestras_estratos = []
    ids_por_estrato = []

    for idx, df_est_i in enumerate(df_estratos):
        n = int(n_prop_est[idx])
        if n > 0:
            muestra_i = df_est_i.sample(n=n, random_state=1)
        else:
            muestra_i = df_est_i.head(0)

        muestras_estratos.append(muestra_i)

        ids_estrato_i = muestra_i["Id"].tolist()
        ids_por_estrato.append(ids_estrato_i)
    valores_estrato = []
    for i in ids_por_estrato:
        valores_estrato.append(np.array([datos_est.iloc[x - 1][col_var] for x in i]))
    suma = []
    for i in valores_estrato:
        suma.append(np.sum(i))
    cuadrados = []
    for i in valores_estrato:
        cuadrados.append(i**2)
    suma_cuadrados = []
    for i in cuadrados:
        suma_cuadrados.append(np.sum(i))
    est_total = []
    for i, j, z in zip(suma, num_cada_est, n_prop_est):
        est_total.append((i / z) * j)
    est_promedio = []
    for i, j, z in zip(suma, n_prop_est, num_cada_est):
        est_promedio.append((i / j) * (z / longitud_columna))
    est_total_bueno = np.sum(est_total)
    est_promedio_bueno = np.sum(est_promedio)
    var_tot = []
    for Nh, nh, valores in zip(num_cada_est, n_prop_est, valores_estrato):

        nh = int(nh)

        if nh > 1:
            Sh2 = np.var(valores, ddof=1)
            f = nh / Nh
            var_h = (Nh**2) * (1 - f) * (Sh2 / nh)
        else:
            var_h = 0

        var_tot.append(var_h)

    var_total_estimador = np.sum(var_tot)

    var_prom = []
    for Nh, nh, valores in zip(num_cada_est, n_prop_est, valores_estrato):

        nh = int(nh)

        if nh > 1:
            Sh2 = np.var(valores, ddof=1)
            f = nh / Nh
            Wh = Nh / longitud_columna
            var_h = (Wh**2) * (1 - f) * (Sh2 / nh)
        else:
            var_h = 0

        var_prom.append(var_h)
    var_promedio_estimador = np.sum(var_prom)
    err_est_prom = math.sqrt(var_promedio_estimador)
    err_est_total = math.sqrt(var_total_estimador)

    ##-------Resultados
    marco_res = ttk.LabelFrame(calculo_est, text="Resultados", padding=10)
    marco_res.pack(fill="x", padx=10, pady=10)
    ttk.Label(marco_res, text=f"Estimador Total: {est_total_bueno}").pack(
        anchor="w", pady=3
    )
    ttk.Label(marco_res, text=f"Estimador Promedio: {est_promedio_bueno}").pack(
        anchor="w", pady=3
    )
    ttk.Label(
        marco_res,
        text=f"Estimador de Varianza del estimador del total: {var_total_estimador}",
    ).pack(anchor="w", pady=3)
    ttk.Label(
        marco_res,
        text=f"Estimador de Varianza del estimador del promedio: {var_promedio_estimador}",
    ).pack(anchor="w", pady=3)
    ttk.Label(marco_res, text=f"Estimador Error est Total: {err_est_total}").pack(
        anchor="w", pady=3
    )
    ttk.Label(marco_res, text=f"Estimador Error est promedio: {err_est_prom}").pack(
        anchor="w", pady=3
    )
    ##------------------
    calculo_est.mainloop()


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
    boton_calcular = tk.Button(er, text="Calcular", command=calcula_er)
    boton_calcular.place(x=20, y=100)
    er.mainloop()


##Ventana EST
def est_EST():
    global entrada_var, entrada_tamanio, entrada_est, est, entrada_estratos_cu
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
    label_estratos_cu = tk.Label(
        est,
        text="¿Qué estratos hay? EJ. Si estratos estan en tabla como H hombre y M mujer (H,M)",
    )
    label_estratos_cu.place(x=20, y=100)
    entrada_estratos_cu = tk.Entry()
    entrada_estratos_cu.place(x=560, y=100)
    boton_calcular = tk.Button(est, text="Calcular", command=calcula_est)
    boton_calcular.place(x=20, y=140)
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
