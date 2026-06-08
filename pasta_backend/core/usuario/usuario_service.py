from core.usuario.usuario_repository import UsuarioRepository

class UsuarioService:

    def __init__(self):
        self.repository = UsuarioRepository()

    def listar_usuarios(self):
        return self.repository.listar()

    def obter_usuario_por_id(self, user_id):
        return self.repository.obter_por_id(user_id)

    def salvar(self, usuario):
        if not usuario.usuario or not usuario.senha:
            raise ValueError("Usuário e senha são obrigatórios")
        
        return self.repository.salvar(usuario)

    def atualizar(self, usuario):
        if not usuario.id:
            raise ValueError("ID é obrigatório")

        return self.repository.atualizar(usuario)

    def remover(self, user_id):
        sucesso = self.repository.remover(user_id)
        if not sucesso:
            return None
        
        return {"id": user_id, "removido": True}
    
    def obter_usuario_por_usuario_senha(self, usuario, senha):
        user = self.repository.buscar_por_usuario(usuario)

        if not user:
            return None

        if user["senha"] != senha:
            return None

        return user
    
    def autenticar(self, usuario, senha):
        situacao = self.repository.autenticar(usuario, senha)
        if situacao != None:
            return situacao
        else:
            return False