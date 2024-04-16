from flask import Flask, render_template
from controllers.controllerPreferencias import preferencias_blueprint

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("preferenciasFormulario.html")


app.register_blueprint(preferencias_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
