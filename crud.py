from db import conectar

def criar_produto(nome, preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (%s, %s)",
        (nome, preco)
    )

    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    conn.close()
    return produtos

def atualizar_produto(id, nome, preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE produtos SET nome=%s, preco=%s WHERE id=%s",
        (nome, preco, id)
    )

    conn.commit()
    conn.close()

def deletar_produto(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM produtos WHERE id=%s", (id,))
    
    conn.commit()
    conn.close()