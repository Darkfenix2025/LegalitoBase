#import sys
#from pathlib import Path

#sys.path.append(str(Path(__file__).resolve().parent))

from flask import Flask, render_template, request
from programas.procesar_hechos import groq_query  # <--- Corrección de import


app = Flask(__name__)  # <--- Corrección: no necesitas especificar el path del archivo
                        # __name__ es una variable built-in que devuelve el nombre del módulo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def procesar():
    texto = request.form['texto']
    resultado = groq_query(texto)  # <--- Corrección: llamada a la función sin prefijo
    return render_template('resultado.html', resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)