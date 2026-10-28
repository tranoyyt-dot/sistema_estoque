from  repositories.usuario_repository import buscar_por_login    

def autenticar(login, senha):
    usuario = buscar_por_login(login)
    if usuario is None:
        return None 
    if usuario["senha"] != senha:
        return None
    return  usuario