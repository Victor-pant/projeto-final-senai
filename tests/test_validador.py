import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Projeto Final', 'pasta_backend'))

from core.validador.validador import validar_cpf, validar_nome, validar_idade

def test_cpf_valido():
    assert validar_cpf("529.982.247-25") == True

def test_cpf_invalido():
    assert validar_cpf("000.000.000-00") == False

def test_cpf_todos_iguais():
    assert validar_cpf("11111111111") == False

def test_nome_valido():
    assert validar_nome("Maria") == True

def test_nome_muito_curto():
    assert validar_nome("A") == False

def test_nome_vazio():
    assert validar_nome("") == False

def test_idade_valida():
    assert validar_idade(20) == True

def test_idade_zero():
    assert validar_idade(0) == True

def test_idade_negativa():
    assert validar_idade(-1) == False

def test_idade_limite():
    assert validar_idade(124) == True

def test_idade_acima_limite():
    assert validar_idade(125) == False
