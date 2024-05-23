import requests
import json

# URL de la aplicación Flask
url = "http://127.0.0.1:5000/predecir"

# Datos de entrada para la predicción
datos = {
    "Gender": 1,  # Suponiendo que 1 es masculino y 0 es femenino
    "Age": 25,
    "Height": 175,
    "Weight": 70,
    "family_history_with_overweight": 1,  # Suponiendo que 1 es sí y 0 es no
    "FAVC": 1,  # Frecuencia de consumo de alimentos altos en calorías
    "FCVC": 2,  # Frecuencia de consumo de vegetales
    "NCP": 3,  # Número de comidas principales al día
    "CAEC": 2,  # Frecuencia de consumo de alimentos entre comidas
    "SMOKE": 0,  # Fumador: 1 sí, 0 no
    "CH2O": 2,  # Consumo diario de agua (en litros)
    "SCC": 1,  # Monitorización de calorías consumidas
    "FAF": 2,  # Frecuencia de actividad física
    "TUE": 1,  # Tiempo usando dispositivos electrónicos
    "CALC": 1,  # Consumo de alcohol
    "MTRANS": 0  # Medio de transporte: 0 a pie, 1 en coche, etc.
}

# Realizar la solicitud POST
response = requests.post(url, json=datos)

# Imprimir la respuesta del servidor
if response.status_code == 200:
    prediccion = response.json().get("prediccion")
    print(f"La predicción del riesgo de obesidad es: {prediccion}")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
