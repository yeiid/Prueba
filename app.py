from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal para la página
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para manejar el simulador de comandos
@app.route('/comando', methods=['POST'])
def comando():
    comando = request.form.get('comando')
    if comando == "ls":
        resultado = "Archivo1.txt  Archivo2.py  Carpeta1"
    elif comando == "pwd":
        resultado = "/home/usuario/proyecto"
    else:
        resultado = "Comando no reconocido en esta simulación."
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
