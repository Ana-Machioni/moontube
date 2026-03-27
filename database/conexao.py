import mysql.connector

def conectar():
    tipo_conexao = "Nuvem" 
    if tipo_conexao == "local":
        #Conectando no bd
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="Musica"
        )

    else:
        conexao = mysql.connector.connect(
            host="servidor-anadz-servidor-anadz.a.aivencloud.com",
            port=28799,
            user="avnadmin",
            password="AVNS_2l6qHVA-QZ89CJ-75rp",
            database="Musica"
        )


            #Criando o cursor
        cursor = conexao.cursor(dictionary=True)
            

        return conexao, cursor 






































