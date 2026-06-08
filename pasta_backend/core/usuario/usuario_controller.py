from flask import Blueprint, jsonify, request
from core.usuario.usuario_service import UsuarioService
from core.usuario.usuario import Usuario

usuario_bp = Blueprint("usuario", __name__)
usuario_service = UsuarioService()

@usuario_bp.route("/usuario", methods=["GET"])
def listar():
    return jsonify({"usuarios": usuario_service.listar_usuarios()})

@usuario_bp.route("/usuario/<int:id>", methods=["GET"])
def buscar(id):
    usuario = usuario_service.obter_usuario_por_id(id)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@usuario_bp.route("/usuario", methods=["POST"])
def criar():
    dados = request.json
    obj = Usuario(None, dados["usuario"], dados["senha"], dados.get("ativo", True))
    return jsonify(usuario_service.salvar(obj)), 201

@usuario_bp.route("/usuario", methods=["PUT"])
def atualizar():
    dados = request.json
    obj = Usuario(dados["id"], dados["usuario"], dados["senha"], dados["ativo"])
    atualizado = usuario_service.atualizar(obj)
    if atualizado:
        return jsonify(atualizado)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@usuario_bp.route("/usuario/<int:id>", methods=["DELETE"])
def deletar(id):
    removido = usuario_service.remover(id)
    if removido:
        return jsonify(removido)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@usuario_bp.route("/autenticar", methods=['POST'])
def autenticar():
    dados = request.json
    usuario = dados.get("usuario")
    senha = dados.get("senha")
    # CORREÇÃO: endpoint não tinha return — nunca retornava resposta
    situacao = usuario_service.autenticar(usuario, senha)
    if situacao:
        return jsonify({"autenticado": True, "usuario": situacao.get("usuario"), "id": situacao.get("id")})
    return jsonify({"autenticado": False, "erro": "Usuário ou senha inválidos"}), 401
