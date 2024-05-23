from flask import Flask, jsonify, request
import numpy as np
import pickle
from loguru import logger
from threading import Thread

app = Flask(__name__)

estado_entrenamiento = "no entrenando"

# Cargar el modelo
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def _entrenar():
    global estado_entrenamiento
    logger.info("Entrenamiento iniciado")
    estado_entrenamiento = 'entrenando'

    # Simula un proceso de entrenamiento prolongado
    sleep(10)

    logger.info("Entrenamiento finalizado")
    estado_entrenamiento = 'no entrenando'

@app.route("/estado", methods=["GET"])
def estado():
    return jsonify({"estado": estado_entrenamiento})

@app.route("/predecir", methods=["POST"])
def predecir():
    try:
        data = request.json
        features = [
            data.get('Gender'),
            data.get('Age'),
            data.get('Height'),
            data.get('Weight'),
            data.get('family_history_with_overweight'),
            data.get('FAVC'),
            data.get('FCVC'),
            data.get('NCP'),
            data.get('CAEC'),
            data.get('SMOKE'),
            data.get('CH2O'),
            data.get('SCC'),
            data.get('FAF'),
            data.get('TUE'),
            data.get('CALC'),
            data.get('MTRANS')
        ]
        
        # Convertir las características a un array de numpy para el modelo
        features_array = np.array(features).reshape(1, -1)
        prediccion = model.predict(features_array)[0]
        
        logger.info(f"Predicción para los parámetros {data} es {prediccion}")
        return jsonify({"prediccion": prediccion})
    except Exception as e:
        logger.error(f"Error en predecir: {e}")
        return jsonify({'error': str(e)}), 400

@app.route("/entrenar", methods=["POST"])
def entrenar():
    if estado_entrenamiento == 'entrenando':
        return jsonify({"error": "ya se está entrenando"}), 400

    hilo = Thread(target=_entrenar)
    hilo.start()
    return jsonify({'resultado': 'entrenamiento iniciado con éxito'})

if __name__ == "__main__":
    app.run(debug=True)
