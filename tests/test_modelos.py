import sys
sys.path.insert(0, '/home/claude/projeto_final/pasta_backend')

from core.aluno.aluno import Aluno
from core.professor.professor import Professor
from core.materias.materias import Materia
from core.usuario.usuario import Usuario

def test_aluno_to_json():
    a = Aluno(1, "João", 20, "529.982.247-25")
    j = a.to_JSON()
    assert j["id"] == 1
    assert j["nome"] == "João"
    assert j["cpf"] == "529.982.247-25"

def test_professor_to_json():
    p = Professor(2, "Carlos", 35, "Matemática")
    j = p.to_JSON()
    assert j["formacao"] == "Matemática"

def test_materia_construtor_ordem():
    # Materia(nome, sigla_curricular, descricao, id=None)
    m = Materia("Matemática", "MAT", "Álgebra e cálculo")
    assert m.nome == "Matemática"
    assert m.id is None

def test_usuario_to_json_nao_expoe_senha():
    u = Usuario(1, "admin", "senha123", True)
    j = u.to_JSON()
    assert "senha" not in j
    assert j["usuario"] == "admin"
