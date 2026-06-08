from core.professor.professor_repository import ProfessorRepository


class ProfessorService:

    def __init__(self):
        self.repository = ProfessorRepository()

    def listar_professores(self):
        return self.repository.listar()
    
    def obter_professor_por_id(self, professor_id):
        professor = self.repository.obter_por_id(professor_id)
        if not professor:
            return None
        else:
            return professor
        
    def adicionar_professor(self, professor):
        if not professor.nome or not professor.formacao or not professor.idade:
            raise ValueError("Nome, Formação e idade são obrigatórios")
        return self.repository.salvar(professor)
    
    def atualizar_professor(self, professor):
        if not professor.id:
            raise ValueError("ID do professor é obrigatório para atualização")
        return self.repository.atualizar(professor)
    
    def remover_professor(self, professor_id):
        sucesso = self.repository.remover(professor_id)
        if not sucesso:
            return None
        return {"id": professor_id, "removido": True}

    def salvar(self, professor):
        return self.repository.salvar(professor)