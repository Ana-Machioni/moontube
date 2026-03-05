from database.conexao import conectar

def cadastrar_usuario(usuario:str, senha:str):
    conexao, cursor = conectar()

    cursor.execute("INSERT INTO login (usuario, senha)  VALUES (%s, %s);", [usuario, senha])

    conexao.commit()

    conexao.close()