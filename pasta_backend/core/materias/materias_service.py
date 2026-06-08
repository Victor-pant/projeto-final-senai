from core.materias.materiais_repository import MateriasRepository

class MateriasService:

    def __init__(self):
        self.repo = MateriasRepository()

    def validar(self, materia):
        if not materia.sigla_curricular:
            raise ValueError("Sigla curricular é obrigatória")
        if not materia.descricao:
            raise ValueError("Descrição é obrigatória")

    def criar(self, materia):
        self.validar(materia)
        return self.repo.adicionar(materia)

    def listar(self):
        return self.repo.listar()

    def buscar_por_id(self, id):
        materia = self.repo.obter_por_id(id)
        if not materia:
            return None  # CORREÇÃO: não lançar exceção, deixar o controller tratar
        return materia

    def atualizar(self, materia):
        # CORREÇÃO: assinatura era atualizar(self, materia, id) mas controller passa só materia
        self.validar(materia)
        return self.repo.atualizar(materia)

    def deletar(self, id):
        # CORREÇÃO: não retornava o resultado
        return self.repo.remover(id)
