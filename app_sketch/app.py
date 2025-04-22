from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Tu función Python (ejemplo)
def mi_funcion_python(parametro):
    return f"Recibí: {parametro} y lo procesé."

# Ruta principal (formulario HTML)
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para llamar a la función desde el frontend
@app.route("/ejecutar", methods=["POST"])
def ejecutar_funcion():
    datos = request.form.get("dato")  # Obtiene datos del formulario
    resultado = mi_funcion_python(datos)  # Llama a tu función
    return jsonify({"resultado": resultado})  # Devuelve el resultado como JSON

if __name__ == "__main__":
    app.run(debug=True)