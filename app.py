from flask import Flask, render_template
import mysql.connector
from model.musica import recuperar_musicas 
from model.genero import recuperar_generos
from model.musica import adicionar_musica
from model.musica import request 


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

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("musica_nome")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    url = request.form.get("imagem")

    if adicionar_musica():

        



if __name__ == "__main__":
    app.run(debug=True)