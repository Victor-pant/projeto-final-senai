from flask import Blueprint, jsonify, request
from core.professor.professor_service import ProfessorService
from core.professor.professor import Professor

professor_bp = Blueprint('professor', __name__)

# objeto do professor
professor_service = ProfessorService()

# endpoint listar professor
@professor_bp.route('/professor', methods=['GET'])
def listar_professores():
    professores = professor_service.listar_professores()
    return jsonify({"professores": professores})

# endpoint buscar professor por id
@professor_bp.route('/professor/<int:id>', methods=['GET'])
def buscar_professor_por_id(id):
    professor = professor_service.obter_professor_por_id(id)
    return jsonify({"professor": professor})

# endpoint alterar professor
@professor_bp.route('/professor', methods=['PUT'])
def atualizar_professor():
    dados = request.get_json()
    obj_professor = Professor(
        dados["id"],
        dados["nome"],
        dados["idade"],
        dados["formacao"]
    )
    atualizado = professor_service.atualizar_professor(obj_professor)
    if atualizado:
        return jsonify(atualizado)
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404

# endpoint deletar professor
@professor_bp.route('/professor/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    removido = professor_service.remover_professor(id)
    if removido:
        return jsonify({"msg": f"Professor id: {id} foi removido!"})
    else:
        return jsonify({"erro": "Professor não encontrado!"}), 404

# endpoint cadastrar professor
@professor_bp.route('/professor', methods=['POST'])
def cadastrar_professor():
    dados = request.json
    obj = Professor(
        0,
        dados["nome"],
        dados["idade"],
        dados["formacao"]
    )
    professor_service.salvar(obj)
    
    return jsonify({"dados": obj.to_JSON()})



