class Materia:
    def __init__(self, nome, sigla_curricular, descricao, id=None):
        self.__id = id
        self.__nome = nome
        self.__sigla_curricular = sigla_curricular
        self.__descricao = descricao

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sigla_curricular(self):
        return self.__sigla_curricular

    @sigla_curricular.setter
    def sigla_curricular(self, sigla_curricular):
        self.__sigla_curricular = sigla_curricular

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "sigla_curricular": self.__sigla_curricular,
            "descricao": self.__descricao
        }