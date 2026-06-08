import sys, os, sqlite3, pytest
sys.path.insert(0, '/home/claude/projeto_final/pasta_backend')

from core.aluno.aluno_service import AlunoService
from core.aluno.aluno_repository import AlunoRepository
from core.aluno.aluno import Aluno
from core.professor.professor_service import ProfessorService
from core.professor.professor_repository import ProfessorRepository
from core.professor.professor import Professor
from core.materias.materias_service import MateriasService
from core.materias.materiais_repository import MateriasRepository
from core.materias.materias import Materia

@pytest.fixture
def db_tmp(tmp_path):
    db = str(tmp_path / "test.db")
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("CREATE TABLE alunos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, cpf TEXT)")
    c.execute("CREATE TABLE professores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, formacao TEXT)")
    c.execute("CREATE TABLE materias (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sigla_curricular TEXT, descricao TEXT)")
    conn.commit(); conn.close()
    return db

def test_aluno_service_salvar_valido(db_tmp):
    service = AlunoService()
    service.repository = AlunoRepository(db_tmp)
    a = Aluno(0, "João Silva", 20, "529.982.247-25")
    r = service.salvar(a)
    assert r["nome"] == "João Silva"

def test_aluno_service_cpf_invalido(db_tmp):
    service = AlunoService()
    service.repository = AlunoRepository(db_tmp)
    a = Aluno(0, "Nome Válido", 20, "000.000.000-00")
    with pytest.raises(ValueError, match="CPF"):
        service.salvar(a)

def test_aluno_service_nome_invalido(db_tmp):
    service = AlunoService()
    service.repository = AlunoRepository(db_tmp)
    a = Aluno(0, "A", 20, "529.982.247-25")
    with pytest.raises(ValueError, match="Nome"):
        service.salvar(a)

def test_aluno_service_campos_obrigatorios(db_tmp):
    service = AlunoService()
    service.repository = AlunoRepository(db_tmp)
    a = Aluno(0, "", 20, "529.982.247-25")
    with pytest.raises(ValueError):
        service.salvar(a)

def test_professor_service_salvar(db_tmp):
    service = ProfessorService()
    service.repository = ProfessorRepository(db_tmp)
    p = Professor(0, "Prof. Ana", 35, "Química")
    r = service.salvar(p)
    assert r["formacao"] == "Química"

def test_materias_service_criar_valido(db_tmp):
    service = MateriasService()
    service.repo = MateriasRepository(db_tmp)
    m = Materia("Física", "FIS", "Mecânica clássica")
    r = service.criar(m)
    assert r["sigla_curricular"] == "FIS"

def test_materias_service_sem_sigla(db_tmp):
    service = MateriasService()
    service.repo = MateriasRepository(db_tmp)
    m = Materia("Física", "", "Mecânica")
    with pytest.raises(ValueError, match="Sigla"):
        service.criar(m)

def test_materias_service_atualizar_corrigido(db_tmp):
    """Após a correção, atualizar() deve funcionar com apenas 1 argumento (materia)"""
    service = MateriasService()
    service.repo = MateriasRepository(db_tmp)
    m = Materia("Física", "FIS", "Mecânica")
    r = service.criar(m)
    m2 = Materia("Física Atualizada", "FIS", "Conteúdo novo", r["id"])
    resultado = service.atualizar(m2)
    assert resultado["nome"] == "Física Atualizada"
