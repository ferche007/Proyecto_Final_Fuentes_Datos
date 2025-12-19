# Imagen base
FROM python:3.11-slim

# Instalar dependencias de Tkinter y X virtual/VNC
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    libx11-dev \
    libxext-dev \
    libxrender-dev \
    libxtst6 \
    libxi6 \
    xvfb \
    x11vnc \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY requirements.txt .
COPY NBA.csv .
COPY student_habits.xlsx .
COPY main.py .
COPY demograficos_2025.csv .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto VNC
EXPOSE 5900

# Comando para lanzar Xvfb, x11vnc y Tkinter
CMD bash -c "Xvfb :1 -screen 0 1024x768x24 & sleep 2; x11vnc -display :1 -nopw -forever & DISPLAY=:1 python main.py"
