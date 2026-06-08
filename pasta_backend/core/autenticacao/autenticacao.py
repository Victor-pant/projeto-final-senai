import base64
from functools import wraps
from flask import request, jsonify
from core.usuario.usuario_service import UsuarioService


def autenticacao(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Basic "):
            return jsonify({"erro": "Credenciais ausentes"}), 401
        
        token = auth.split(" ")[1]
        try:
            decoded = base64.b64decode(token).decode("utf-8")
            usuario, senha = decoded.split(":")
        except Exception:
            return jsonify({"erro":"Credenciais invalidas"}), 401
        
        service = UsuarioService()
        user = service.obter_usuario_por_usuario_senha(usuario, senha)
        if (
            not user
            or user["senha"] != senha
            or user["usuario"] != usuario
            or not user["ativo"]
        ):
            return jsonify({"erro": "Usuário ou Senha Inváidos"}), 401
        return f(*args, **kwargs)
    return decorated