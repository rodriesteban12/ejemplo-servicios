from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola, esto es una prueba"

if __name__ == "__main__":
    app.run('0.0.0.0' ,debug=True)
