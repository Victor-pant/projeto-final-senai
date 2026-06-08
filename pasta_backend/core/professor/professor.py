class Professor:
    def __init__(self, id=0, nome="", idade=0, formacao=""):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__formacao = formacao

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
    def formacao(self):
        return self.__formacao

    @formacao.setter
    def formacao(self, formacao): 
        self.__formacao = formacao

    def to_JSON(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "formacao": self.formacao
        }

        