from banco import conectar

def buscar_por_login(login):
    conexao = conectar()
    usuario =conexao.execute(
        """"
        SELECT * FROM usuarios WHERE login = ?
        """
        (login,)
    ).fetchone()
    return usuario
