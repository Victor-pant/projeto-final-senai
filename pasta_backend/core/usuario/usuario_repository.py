import sqlite3

DB_NAME = "escola.db"

class UsuarioRepository:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def listar(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, usuario, senha, ativo FROM usuarios;")
        rows = cursor.fetchall()
        conn.close()

        return [
            {"id": r[0], "usuario": r[1], "senha": r[2], "ativo": r[3]}
            for r in rows
        ]

    def obter_por_id(self, user_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, usuario, senha, ativo FROM usuarios WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return {"id": row[0], "usuario": row[1], "senha": row[2], "ativo": row[3]}
        return None

    def salvar(self, usuario):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (usuario, senha, ativo) VALUES (?, ?, ?)",
            (usuario.usuario, usuario.senha, usuario.ativo)
        )

        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()

        return {
            "id": novo_id,
            "usuario": usuario.usuario,
            "ativo": usuario.ativo
        }

    def atualizar(self, usuario):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM usuarios WHERE id = ?", (usuario.id,))
        if not cursor.fetchone():
            conn.close()
            return None

        cursor.execute(
            "UPDATE usuarios SET usuario=?, senha=?, ativo=? WHERE id=?",
            (usuario.usuario, usuario.senha, usuario.ativo, usuario.id)
        )

        conn.commit()
        conn.close()

        return {
            "id": usuario.id,
            "usuario": usuario.usuario,
            "ativo": usuario.ativo
        }

    def remover(self, user_id):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        conn.commit()

        removido = cursor.rowcount
        conn.close()

        return removido > 0
    
    def buscar_por_usuario(self, usuario):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, usuario, senha, ativo FROM usuarios WHERE usuario = ?",
            (usuario,)
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                "id": row[0],
                "usuario": row[1],
                "senha": row[2],
                "ativo": row[3]
            }

        return None
    

    def autenticar(self, usuario, senha):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, usuario, senha, ativo FROM usuarios WHERE usuario = ? AND senha = ?",
            (usuario,senha)
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                "id": row[0],
                "usuario": row[1],
                "senha": row[2],
                "ativo": row[3]
            }

        return None