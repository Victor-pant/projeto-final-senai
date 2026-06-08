import sqlite3
import os

# Caminho absoluto baseado na localização deste arquivo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "escola.db")

# Também aceita variável de ambiente para flexibilidade no Render
DB_NAME = os.environ.get("DB_PATH", DB_PATH)

CREATE_TABLE_ALUNOS_SQL = """
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cpf TEXT NOT NULL
);
"""

CREATE_TABLE_USUARIOS_SQL = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL,
    ativo INTEGER NOT NULL
);
"""

CREATE_TABLE_PROFESSORES_SQL = """
CREATE TABLE IF NOT EXISTS professores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    formacao TEXT NOT NULL
);
"""

CREATE_TABLE_MATERIAS_SQL = """
CREATE TABLE IF NOT EXISTS materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sigla_curricular TEXT NOT NULL,
    descricao TEXT NOT NULL
);
"""

INSERT_INICIAIS_USUARIO = """
INSERT INTO usuarios (usuario, senha, ativo) VALUES ('senai', 'senai123', 1);
"""

def init_db():
    print(f">> Inicializando banco em: {DB_NAME}")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(CREATE_TABLE_ALUNOS_SQL)
    cursor.execute(CREATE_TABLE_USUARIOS_SQL)
    cursor.execute(CREATE_TABLE_PROFESSORES_SQL)
    cursor.execute(CREATE_TABLE_MATERIAS_SQL)

    cursor.execute("SELECT COUNT(*) FROM usuarios;")
    if cursor.fetchone()[0] == 0:
        cursor.execute(INSERT_INICIAIS_USUARIO)
        print(">> Usuário padrão criado: senai / senai123")
    else:
        print(">> Tabela USUARIOS já contém dados.")

    conn.commit()
    conn.close()
    print(">> Banco inicializado com sucesso!")

if __name__ == "__main__":
    init_db()
