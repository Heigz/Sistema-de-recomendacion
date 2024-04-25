from flask import Flask, render_template
from controllers.controllerPreferencias import preferencias_blueprint

app = Flask(__name__)

app.register_blueprint(preferencias_blueprint)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/recomendarPorOpciones")
def recomendar_por_opciones():
    return render_template("preferenciasFormulario.html")

@app.route("/recomendarPorAuto")
def recomendar_por_auto():
    return render_template("preferenciasPorAutoFormulario.html")



if __name__ == "__main__":
    app.run(debug=True)
