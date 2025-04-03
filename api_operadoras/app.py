from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
CORS(app)

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, 'operadoras.csv')

df = pd.read_csv(csv_path, sep=';', encoding='utf-8')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.dropna(subset=['nome_fantasia', 'razao_social'])

# Rota de busca
@app.route('/operadoras', methods=['GET'])
def buscar_operadoras():
    termo = request.args.get('q', '').lower()

    if not termo:
        return jsonify({'erro': 'Parâmetro de busca (q) é obrigatório!'}), 400

    resultados = df[
        df['nome_fantasia'].str.lower().str.contains(termo, na=False) |
        df['razao_social'].str.lower().str.contains(termo, na=False)
    ]

    resultados = resultados.head(10).replace({np.nan: None}).to_dict(orient='records')

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)