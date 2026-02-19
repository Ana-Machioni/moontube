from flask import Flask, render_template
import mysql.connector
from model.musica import recuperar_musicas 
from model.genero import recuperar_generos


app = Flask (__name__)

@app.route("/home", methods=["GET"])
@app.route("/")
def pagina_principal():
    # recuperando as musicas 
    musicas = recuperar_musicas()
    # recuperando os generos 
    generos = recuperar_generos()
    # mostrando a pagina 
    return render_template("principal.html", musicas = musicas, generos = generos)

@app.route("/admin")
def pag_admin():
    # recuperando as muicas 
    musicas = recuperar_musicas()
    generos = recuperar_generos()
    # mostrando a pagina 
    return render_template ("administracao.html", musicas = musicas, generos = generos )

if __name__ == "__main__":
    app.run(debug=True)