from core.aluno.aluno_repository import AlunoRepository
from core.validador.validador import *


class AlunoService:

    def __init__(self):
        self.repository = AlunoRepository()

    def listar_alunos(self):
        return self.repository.listar()
    
    def obter_aluno_por_id(self, aluno_id):
        aluno = self.repository.obter_por_id(aluno_id)
        if not aluno:
            return None
        else:
            return aluno
        
    def adicionar_aluno(self, aluno):
        if not aluno.nome or not aluno.cpf or not aluno.idade:
            raise ValueError("Nome, CPF, e idade são obrigatórios")
        if not validar_cpf(aluno.cpf):
            raise ValueError("CPF Inválido")
        if not validar_idade(aluno.idade):
            raise ValueError("Idade Inválido")
        if not validar_nome(aluno.nome):
            raise ValueError("Nome Inválido")
        
        return self.repository.adicionar(aluno)
    
    def atualizar_aluno(self, aluno):
        if not aluno.id:
            raise ValueError("ID do aluno é obrigatório para atualziação")
        return self.repository.atualizar(aluno)
    
    def remover_aluno(self,aluno_id):
        sucesso = self.repository.remover(aluno_id)
        if not sucesso:
            return None
        return {"id": aluno_id, "removido": True}

    def salvar(self, aluno):

        if not aluno.nome or not aluno.cpf or not aluno.idade:
            raise ValueError("Nome, CPF e idade são obrigatórios")

        if not validar_cpf(aluno.cpf):
            raise ValueError("CPF inválido")

        if not validar_idade(aluno.idade):
            raise ValueError("Idade inválida")

        if not validar_nome(aluno.nome):
            raise ValueError("Nome inválido")

        return self.repository.adicionar(aluno)
    

