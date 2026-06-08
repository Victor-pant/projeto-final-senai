from flask import Blueprint, request, jsonify
from core.materias.materias_service import MateriasService
from core.materias.materias import Materia

materias_bp = Blueprint("materias", __name__)
service = MateriasService()

@materias_bp.route("/materias", methods=["GET"])
def listar():
    materias = service.listar()
    return jsonify({"materias": materias})

@materias_bp.route("/materias/<int:id>", methods=["GET"])
def buscar(id):
    materia = service.buscar_por_id(id)
    if materia:
        return jsonify(materia)
    return jsonify({"erro": "Matéria não encontrada"}), 404

@materias_bp.route("/materias", methods=["POST"])
def criar():
    try:
        data = request.json
        materia = Materia(data["nome"], data["sigla_curricular"], data["descricao"], None)
        resultado = service.criar(materia)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@materias_bp.route("/materias/<int:id>", methods=["PUT"])
def atualizar(id):
    # CORREÇÃO: rota agora recebe id via URL para ser consistente
    try:
        data = request.json
        materia = Materia(data["nome"], data["sigla_curricular"], data["descricao"], id)
        resultado = service.atualizar(materia)
        if resultado:
            return jsonify(resultado)
        return jsonify({"erro": "Matéria não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@materias_bp.route("/materias/<int:id>", methods=["DELETE"])
def deletar(id):
    removido = service.deletar(id)
    if removido:
        return jsonify({"msg": "Matéria removida com sucesso"})
    return jsonify({"erro": "Matéria não encontrada"}), 404
