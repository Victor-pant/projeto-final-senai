from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = "senai_escola_2024"

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/professores')
def cad_professor():
    return render_template('cad_professor.html')

@app.route('/alunos')
def cad_aluno():
    return render_template('cad_aluno.html')

@app.route('/materias')
def cad_materias():
    return render_template('cad_materias.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
