# Calculadora Estadística
> **Leonardo Villareal, Fernando Mejía, Francisco Pérez**

Herramienta para realizar cálculos estadísticos esenciales dentro de un contenedor Docker, incluyendo interfaz gráfica. Ideal para estudiantes, investigadores y usuarios que busquen ejecutar herramientas estadísticas sin conflictos de dependencias locales. Una aplicación de escritorio desarrollada ealizar cálculos estadísticos avanzados mediante diferentes métodos de muestreo y estimación. La aplicación permite analizar datos desde archivos CSV o Excel y realizar estimaciones estadísticas con múltiples metodologías.

## - Características

- **Interfaz gráfica intuitiva** construida con Tkinter
- **Múltiples métodos de estimación estadística**:
  - Muestreo Aleatorio Simple (MAS)
  - Estimador de Razón (ER)
  - Estimación por Estratificación
- **Herramientas de análisis**:
  - Comparación de varianzas entre MAS y ER
  - Calculadora de tamaño de muestra óptimo
  - Visualización de distribuciones de estimadores
- **Soporte para múltiples formatos**: CSV y Excel (.xlsx)
- **Visualización de datos**: Gráficos y tablas interactivas
- **Despliegue con Docker**: Configuración lista para contenedores

## - Requisitos

### Software Base
- Python 3.11 o superior
- Sistema operativo: Linux, macOS, o Windows
- Docker (opcional, para despliegue en contenedor)

### Para macOS (con Docker)
- XQuartz instalado y configurado
- Configuración de X11 forwarding para la interfaz gráfica

## - Instalación

### Instalación Local

1. **Clonar el repositorio**:
   git clone <url-del-repositorio>
   cd Proyecto_Final_Fuentes_Datos
   2. **Instalar dependencias**:h
   cd resources
   pip install -r requirements.txt
   3. **Ejecutar la aplicación**:
   python main.py
   ### Instalación con Docker

#### Para macOS:

1. **Instalar XQuartz**:
   - Descargar e instalar desde [XQuartz.org](https://www.xquartz.org/)

2. **Configurar XQuartz**:
   - Abrir XQuartz → Ajustes → Seguridad
   - Marcar: "Allow connections from network clients"
   - Reiniciar XQuartz

3. **Configurar variables de entorno**:
   
   export DISPLAY=:0
   xhost + 127.0.0.1
   4. **Construir la imagen Docker**:
   docker build -t calculadora-estadistica -f resources/Dockerfile .
   5. **Ejecutar el contenedor**:
   docker run -e DISPLAY=host.docker.internal:0 -it calculadora-estadistica
   #### Para Linux:

1. **Construir la imagen**:
   docker build -t calculadora-estadistica -f resources/Dockerfile .
   2. **Ejecutar el contenedor** (con X11 forwarding):
 
   docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix calculadora-estadistica
   ## - Uso

### Flujo de Trabajo

1. **Iniciar la aplicación**: Ejecutar `main.py` o el contenedor Docker

2. **Cargar datos**: 
   - Hacer clic en "Seleccionar" en la ventana principal
   - Elegir un archivo CSV o Excel (.xlsx)
   - La aplicación automáticamente agregará una columna "Id" si no existe

3. **Seleccionar método de estimación**:
   - Elegir entre los métodos disponibles según tus necesidades

4. **Configurar parámetros**:
   - Ingresar el nombre de la columna a estimar
   - Especificar el tamaño de la muestra
   - Para ER: proporcionar columna auxiliar
   - Para Estratificación: especificar columna de estratos y valores

5. **Visualizar resultados**:
   - Revisar estimadores, varianzas y errores estándar
   - Examinar la muestra seleccionada en formato tabla
   - Analizar gráficos comparativos (si aplica)

## 📊 Métodos de Estimación

### 1. Muestreo Aleatorio Simple (MAS)

**Descripción**: Selección aleatoria de unidades de la población sin reemplazo.

**Parámetros requeridos**:
- Nombre de columna de variable a estimar
- Tamaño de muestra

**Resultados proporcionados**:
- Estimador del total
- Estimador del promedio
- Varianza del estimador del total
- Varianza del estimador del promedio
- Error estándar del total
- Error estándar del promedio
- Tabla con los datos de la muestra seleccionada

### 2. Estimador de Razón (ER)

**Descripción**: Utiliza una variable auxiliar correlacionada para mejorar la precisión de la estimación.

**Parámetros requeridos**:
- Nombre de columna de variable a estimar
- Nombre de columna de variable auxiliar
- Tamaño de muestra

**Resultados proporcionados**:
- Estimador del total (usando razón)
- Estimador del promedio (usando razón)
- Varianzas y errores estándar correspondientes
- Tabla con los datos de la muestra seleccionada

### 3. Estimación por Estratificación

**Descripción**: Divide la población en estratos homogéneos y selecciona muestras de cada estrato.

**Parámetros requeridos**:
- Nombre de columna de variable a estimar
- Nombre de columna con estratos
- Tamaño de muestra total
- Valores de los estratos (formato: "valor1,valor2,valor3")

**Resultados proporcionados**:
- Estimador del total estratificado
- Estimador del promedio estratificado
- Varianzas y errores estándar correspondientes

### 4. Comparativa de Varianzas MAS vs ER

**Descripción**: Compara visualmente las varianzas de ambos métodos para diferentes tamaños de muestra.

**Parámetros requeridos**:
- Nombre de columna de variable a estimar
- Nombre de columna auxiliar (para ER)

**Resultado**: Gráfico de líneas mostrando la evolución de las varianzas según el tamaño de muestra.

### 5. Calculadora de Tamaño de Muestra Óptimo

**Descripción**: Calcula el número óptimo de unidades para una muestra dado un nivel de confianza y error máximo.

**Parámetros requeridos**:
- Nivel de confianza Z (tabla de referencia incluida)
- Varianza estimada de los datos
- Error absoluto máximo permitido
- Número de unidades en la población
- Tipo de estimación: "TOTAL" o "PROMEDIO"

**Tabla de referencia Z incluida**:
- 90% confianza: Z = 1.282
- 95% confianza: Z = 1.645
- 97.5% confianza: Z = 1.960
- 99% confianza: Z = 2.326
- 99.5% confianza: Z = 2.576

### 6. Distribución del Estimador

**Descripción**: Genera y visualiza la distribución completa del estimador para todas las posibles muestras de un tamaño dado.

**Parámetros requeridos**:
- Nombre de columna de variable a estimar
- Tamaño de muestra

**Resultado**: Gráfico de barras mostrando la frecuencia de cada valor del estimador.
