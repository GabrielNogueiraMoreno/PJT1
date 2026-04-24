from db import conectar

def registrar(username, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (username, senha) VALUES (%s, %s)",
        (username, senha)
    )

    conn.commit()
    conn.close()

def login(username, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE username=%s AND senha=%s",
        (username, senha)
    )

    user = cursor.fetchone()
    conn.close()

    return user