# tools/entrega.py

import numpy as np
import joblib

class Entrega:
    def __init__(self, values):
        # transforma os valores em float
        self.values = [float(v) for v in values]
        # carrega o modelo já treinado
        self.model = joblib.load('./modelo/modelo.pkl')

    def prepare(self):
        # transforma a entrada em array 2D (para o modelo)
        return np.array(self.values).reshape(1, -1)

    def predict(self, prepared_data):
        return self.model.predict(prepared_data)[0]
