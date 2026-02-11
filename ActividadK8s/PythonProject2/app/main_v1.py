from flask import Flask

app = Flask(__name__)
archivo = "data/notas.txt"

@app.route('/')
def home():
    return "La API funciona correctamente"

@app.route('/add/<nota>')
def agregoNota(nota):
    with open(archivo, "a") as f:
        f.write(nota + "\n")
    return nota

@app.route('/list')
def lista():
    with open(archivo, "r") as f:
        notas = f.read()
    return notas

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
