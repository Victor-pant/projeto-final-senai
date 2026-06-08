from flask import Blueprint, jsonify, request
from core.aluno.aluno_service import AlunoService
from core.aluno.aluno import Aluno

aluno_bp = Blueprint('aluno', __name__)
aluno_service = AlunoService()

# endpoint listar alunos
@aluno_bp.route('/aluno', methods=['GET'])
def listar_alunos():
    alunos = aluno_service.listar_alunos()
    return jsonify({"alunos": alunos})

# endpoint buscar aluno por id
@aluno_bp.route('/aluno/<int:id>', methods=['GET'])
def buscar_aluno_por_id(id):
    aluno = aluno_service.obter_aluno_por_id(id)
    return jsonify({"aluno": aluno})

# endpoint alterar aluno
@aluno_bp.route('/aluno', methods=['PUT'])
def atualizar_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(dados["id"], dados["nome"], dados["idade"], dados["cpf"])
    atualizado = aluno_service.atualizar_aluno(obj_aluno)
    if atualizado:
        return jsonify(atualizado)
    return jsonify({"erro": "Aluno não encontrado"}), 404

# endpoint deletar aluno
@aluno_bp.route('/aluno/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    removido = aluno_service.remover_aluno(id)
    if removido:
        return jsonify({"msg": f"Aluno id: {id} foi removido!"})
    return jsonify({"erro": "Aluno não encontrado!"}), 404

# endpoint cadastrar aluno
@aluno_bp.route('/aluno', methods=['POST'])
def cadastrar_aluno():
    dados = request.json
    obj = Aluno(0, dados["nome"], dados["idade"], dados["cpf"])
    resultado = aluno_service.salvar(obj)
    return jsonify({"dados": resultado})
