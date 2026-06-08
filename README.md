# 🎓 EduSenai — Sistema de Gestão Escolar

Sistema web desenvolvido como Projeto Final do curso de Python no SENAI.  
Permite gerenciar **alunos**, **professores** e **matérias** de uma instituição de ensino, com autenticação de usuário.

---

## 📸 Páginas do sistema

| Tela | Descrição |
|---|---|
| Login | Autenticação com usuário e senha |
| Dashboard | Painel inicial com contadores e navegação |
| Alunos | CRUD completo com validação de CPF |
| Professores | CRUD com nome, idade e formação |
| Matérias | CRUD com sigla curricular e descrição |

---

## 🏗️ Arquitetura

O projeto é dividido em dois serviços Flask independentes:

```
projeto_final/
├── pasta_backend/          → API REST (porta 5000)
│   ├── app.py
│   ├── requirements.txt
│   ├── escola.db           → Banco SQLite (gerado automaticamente)
│   └── core/
│       ├── aluno/          → Model, Controller, Service, Repository
│       ├── professor/
│       ├── materias/
│       ├── usuario/
│       ├── autenticacao/   → Autenticação Basic Auth
│       ├── validador/      → Validação de CPF, nome, idade
│       └── utils/
│           └── criar_db.py → Inicialização do banco
│
├── pasta_frontend/         → Interface Web (porta 5001)
│   ├── app.py
│   └── templates/
│       ├── login.html
│       ├── dashboard.html
│       ├── cad_aluno.html
│       ├── cad_professor.html
│       └── cad_materias.html
│
└── tests/                  → Testes automatizados (pytest)
    ├── test_validador.py
    ├── test_modelos.py
    ├── test_repository.py
    └── test_services.py
```

### Padrão utilizado

Cada módulo segue a separação em 4 camadas:

```
Controller  →  Service  →  Repository  →  SQLite
(rotas)       (regras)     (queries)     (banco)
```

---

## 🚀 Como rodar localmente

### Pré-requisitos
- Python 3.10+
- pip

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/edusenai.git
cd edusenai
```

### 2. Backend
```bash
cd pasta_backend
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
python core/utils/criar_db.py
python app.py
```
API disponível em: `http://localhost:5000`

### 3. Frontend
Abra um novo terminal:
```bash
cd pasta_frontend
python -m venv .venv
.venv\Scripts\activate
pip install flask
python app.py
```
Interface disponível em: `http://localhost:5001`

### 4. Testes
```bash
pip install pytest
python -m pytest tests/ -v
```

---

## 🔑 Acesso padrão

| Campo | Valor |
|---|---|
| Usuário | `senai` |
| Senha | `senai123` |

---

## 📡 Endpoints da API

### Alunos `/aluno`
| Método | Rota | Descrição |
|---|---|---|
| GET | `/aluno` | Lista todos os alunos |
| GET | `/aluno/<id>` | Busca aluno por ID |
| POST | `/aluno` | Cadastra novo aluno |
| PUT | `/aluno` | Atualiza aluno existente |
| DELETE | `/aluno/<id>` | Remove aluno |

### Professores `/professor`
| Método | Rota | Descrição |
|---|---|---|
| GET | `/professor` | Lista todos os professores |
| GET | `/professor/<id>` | Busca professor por ID |
| POST | `/professor` | Cadastra novo professor |
| PUT | `/professor` | Atualiza professor existente |
| DELETE | `/professor/<id>` | Remove professor |

### Matérias `/materias`
| Método | Rota | Descrição |
|---|---|---|
| GET | `/materias` | Lista todas as matérias |
| GET | `/materias/<id>` | Busca matéria por ID |
| POST | `/materias` | Cadastra nova matéria |
| PUT | `/materias/<id>` | Atualiza matéria existente |
| DELETE | `/materias/<id>` | Remove matéria |

### Autenticação `/autenticar`
| Método | Rota | Descrição |
|---|---|---|
| POST | `/autenticar` | Valida usuário e senha |

**Body esperado:**
```json
{ "usuario": "senai", "senha": "senai123" }
```

---

## 🛠️ Tecnologias utilizadas

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.11 |
| Backend | Flask + Flask-CORS |
| Frontend | HTML5 + CSS3 + JavaScript Vanilla |
| Banco de dados | SQLite 3 |
| Servidor produção | Gunicorn |
| Testes | pytest |
| Deploy | Render |

---

## ✅ Testes automatizados

30 testes cobrindo:
- Validação de CPF (algoritmo completo)
- Validação de nome e idade
- Modelos (to_JSON, propriedades)
- Repositórios (CRUD com banco temporário)
- Services (regras de negócio e tratamento de erros)

```
30 passed in 0.34s
```

---

## 👨‍💻 Autor

Desenvolvido por **Victor** — Projeto Final Python SENAI
