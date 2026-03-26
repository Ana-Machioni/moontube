from database.conexao import conectar

def cadastrar_usuario(usuario:str, senha:str):
    conexao, cursor = conectar()

    cursor.execute("INSERT INTO login (usuario, senha)  VALUES (%s, %s);", [usuario, senha])

    conexao.commit()

    conexao.close()

def verificar_usuario(usuario:str, senha:str) ->list:
    """
    Funçao que verifica se o usuario esta cadastrado
    Se estiver cadastrado retorno os dados do usuario
    Se nao estiver cadastrado retorno None
    """

    conexao, cursor = conectar()

    cursor.execute("SELECT usuario, senha FROM login WHERE usuario = %s AND senha = %s ", [usuario, senha])

    usuario= cursor.fetchone()

    conexao.commit()
    
    conexao.close()
    return usuario


