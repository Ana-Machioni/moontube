# sempre que precisar de uma lista de todas as musicas, musicas = 
from database.conexao import conectar


def recuperar_musicas():
    # passo 1 e 2 ja feito
    conexao, cursor = conectar()

    #Executando a consultando
    cursor.execute("SELECT codigo, cantor, nome,  duracao,  url_imagem, nome_genero, ativo FROM musica;")

    #rec os dados
    musicas =  cursor.fetchall()

    #fechando a conexao
    conexao.close()

    return musicas 

def adicionar_musica(cantor:str, nome_musica:str, duracao:str, imagem:str, genero:str) -> bool: 
    """
    
    a função tem objetivo de adicionar musica no banco de dados 

    """

    try:
        # conectando ao banco
        conexao, cursor = conectar()
        # executar insert
        cursor.execute("""
                            INSERT INTO Musica
                                (CANTOR, NOME, DURACAO, URL_IMAGEM, NOME_GENERO)
                            VALUES 
                                (%s, %s, %s, %s, %s)
                    """,
                    [cantor, nome_musica, duracao, imagem, genero]
                    )
        # values = valores 

        # commit = confitmando o insert 
        conexao.commit()

        # fechando a conexao 
        conexao.close()

        return True 
    
    except Exception as erro : 
        print (erro)
        return False 
    
def excluir_musica(codigo: int):
    """
        a funçao tem objetivo de deletar musicas no banco de dados 
    """

    try:
        # conectando ao banco
        conexao, cursor = conectar()
        # executar insert 
        cursor.execute(""" 
                            DELETE FROM Musica
                            WHERE codigo = %s;
                        """, [codigo])

        # commit 
        conexao.commit()

        # fechando conexao
        conexao.close()

        return True
    
    except Exception as erro:
        print(erro)
        return False
    
# def ativar_musica(codigo:int, status:bool):


        
    