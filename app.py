from flask import Flask, request
app = Flask(__name__)

@app.get("/")
def hola_mundo():
    return render_template("saludo.html", )

    
@app.get("/adios")
def adios():
    return f"""
    <h1>¡Hola {request.args.get("nombre", "mundo")}!</h1>"
    <p>
    Esta es nuesta <strong> primera </strong> página
    </p>
    """

print("Iniciando servidor")