from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'aula_13_10'
}

# Função para conectar ao banco de dados
def connect_db():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

def inserir_dados(table, fields):
    if request.method == 'POST':
        values = [request.form[field] for field in fields]
        conn = connect_db()
        cursor = conn.cursor()
        query = f'INSERT INTO {table} ({", ".join(fields)}) VALUES ({", ".join(["%s"] * len(fields))})'
        cursor.execute(query, tuple(values))
        conn.commit()
        conn.close()
        return f'Dados inseridos na tabela {table} com sucesso.'

@app.route('/index', methods=['POST'])
def inserir_setor():
    return inserir_dados('setor', ['nome'])

@app.route('/inserir_cargo', methods=['POST'])
def inserir_cargo():
    return inserir_dados('cargos', ['nome', 'id_setor'])

@app.route('/inserir_funcionario', methods=['POST'])
def inserir_funcionario():
    return inserir_dados('funcionarios', ['primeiro_nome', 'sobrenome', 'data_admissao', 'status_funcionario', 'id_setor'])

if __name__ == '__main__':
    app.run(debug=True)
