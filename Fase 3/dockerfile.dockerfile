# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos necesarios al directorio de trabajo en la imagen
COPY train.py .
COPY predict.py .
COPY model.pkl .

COPY myrestapi.py /app

WORKDIR /app

CMD flask --app myrestapi run --host=0.0.0.0 