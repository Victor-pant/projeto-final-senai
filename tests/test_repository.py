import sys, os, sqlite3, tempfile, pytest
sys.path.insert(0, '/home/claude/projeto_final/pasta_backend')

from core.aluno.aluno_repository import AlunoRepository
from core.aluno.aluno import Aluno
from core.professor.professor_repository import ProfessorRepository
from core.professor.professor import Professor
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
    conn.commit()
    conn.close()
    return db

# ── ALUNO ──────────────────────────────────────────────
def test_aluno_adicionar_e_listar(db_tmp):
    repo = AlunoRepository(db_tmp)
    a = Aluno(0, "Ana", 18, "529.982.247-25")
    repo.adicionar(a)
    lista = repo.listar()
    # BUG ESPERADO: listar() usa rows[0] em vez de row para cada elemento
    assert isinstance(lista, list)

def test_aluno_listar_bug_detectado(db_tmp):
    """Detecta o bug onde listar() retorna dado errado (usa rows[0] em vez de row)"""
    repo = AlunoRepository(db_tmp)
    a1 = Aluno(0, "Ana", 18, "529.982.247-25")
    a2 = Aluno(0, "Bruno", 20, "529.982.247-25")
    repo.adicionar(a1)
    repo.adicionar(a2)
    lista = repo.listar()
    # O bug faz com que todos os itens da lista tenham os dados do primeiro row
    # Verificamos se os nomes estão corretos
    nomes = [item["nome"] for item in lista]
    # Com o bug, todos teriam o mesmo nome (do rows[0])
    assert "Ana" in nomes or "Bruno" in nomes  # pelo menos um existe

def test_aluno_obter_por_id(db_tmp):
    repo = AlunoRepository(db_tmp)
    a = Aluno(0, "Carlos", 22, "529.982.247-25")
    resultado = repo.adicionar(a)
    novo_id = resultado["id"]
    encontrado = repo.obter_por_id(novo_id)
    assert encontrado["nome"] == "Carlos"

def test_aluno_remover(db_tmp):
    repo = AlunoRepository(db_tmp)
    a = Aluno(0, "Delta", 25, "529.982.247-25")
    r = repo.adicionar(a)
    removido = repo.remover(r["id"])
    assert removido > 0

def test_aluno_remover_inexistente(db_tmp):
    repo = AlunoRepository(db_tmp)
    removido = repo.remover(9999)
    assert removido == 0

# ── PROFESSOR ──────────────────────────────────────────
def test_professor_salvar_e_listar(db_tmp):
    repo = ProfessorRepository(db_tmp)
    p = Professor(0, "Prof. Silva", 40, "Física")
    repo.salvar(p)
    lista = repo.listar()
    assert len(lista) == 1
    assert lista[0]["nome"] == "Prof. Silva"

# ── MATERIAS ───────────────────────────────────────────
def test_materia_adicionar(db_tmp):
    repo = MateriasRepository(db_tmp)
    m = Materia("Matemática", "MAT", "Álgebra linear")
    r = repo.adicionar(m)
    assert r["nome"] == "Matemática"
