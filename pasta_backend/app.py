from flask import Flask
from flask_cors import CORS                         
from core.aluno.aluno_controller import aluno_bp
from core.professor.professor_controller import professor_bp
from core.usuario.usuario_controller import usuario_bp
from core.materias.materias_controller import materias_bp


app = Flask(__name__)
CORS(app)     

# registrar o controllers
app.register_blueprint(aluno_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(materias_bp)



if __name__ == "__main__":
    app.run()