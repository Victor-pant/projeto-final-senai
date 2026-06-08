class Usuario:
    def __init__(self, id=None, usuario="", senha="", ativo=False):
        self.__id = id
        self.__usuario = usuario
        self.__senha = senha
        self.__ativo = ativo

    # ID
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    # USUARIO
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    # SENHA
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    # ATIVO
    @property
    def ativo(self):
        return self.__ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    # CONVERTER PARA JSON
    def to_JSON(self):
        return {
            "id": self.__id,
            "usuario": self.__usuario,
            "ativo": self.__ativo
        }