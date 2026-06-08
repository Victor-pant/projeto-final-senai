class Aluno:
    def __init__(self, id=0, nome="", idade=0, cpf=""):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

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
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):  # corrigido
        self.__cpf = cpf

    def to_JSON(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf
        }

        