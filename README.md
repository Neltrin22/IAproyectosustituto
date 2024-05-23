# IAproyectosustituto
Nelson Alcides Puerta García CC: 71335787
Ingeniería de Sistemas

Repositorio del proyecto sustituto para la materia de Inteligencia Artificial UdeA

Procedimiento para ejecutar el proyecto:

Fase 1:
Ingrese a la carpeta Fase 1
descargue y/o abra el archivo "01 - Generacion del modelo v1.ipynb" en un entorno de colab
ejecute celda por celda de codigo desde arriba hacia abajo

First, build your container

docker build -t api .

Then, run the container

docker run -it -p 5001:5000 api

Finally, on a separate shell run the client to make requests

python client.py
