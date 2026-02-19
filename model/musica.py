# sempre que precisar de uma lista de todas as musicas, musicas = 
from database.conexao import conectar


def recuperar_musicas():
    # passo 1 e 2 ja feito
    conexao, cursor = conectar()

    #Executando a consultando
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    #rec os dados
    musicas =  cursor.fetchall()

    #fechando a conexao
    conexao.close()

    return musicas 