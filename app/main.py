from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app)

# Função para inicializar o banco de dados SQLite
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Rota para adicionar uma nova pergunta e resposta ao histórico
@app.route('/history', methods=['POST'])
def add_to_history():
    data = request.get_json()
    question = data.get('question')
    answer = data.get('answer')

    if not question or not answer:
        return jsonify({"error": "Question and answer are required"}), 400

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO history (question, answer) VALUES (?, ?)', (question, answer))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"}), 201

# Rota para obter o histórico de perguntas e respostas
@app.route('/history', methods=['GET'])
def get_history():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history')
    rows = cursor.fetchall()
    conn.close()

    history = [{"id": row[0], "question": row[1], "answer": row[2]} for row in rows]
    return jsonify(history)

# Rota para deletar um item específico do histórico pelo ID
@app.route('/history/<int:id>', methods=['DELETE'])
def delete_history(id):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM history WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"}), 200

# Rota para atualizar uma pergunta e resposta no histórico pelo ID
@app.route('/history/<int:id>', methods=['PUT'])
def update_history(id):
    data = request.get_json()
    question = data.get('question')
    answer = data.get('answer')

    if not question or not answer:
        return jsonify({"error": "Question and answer are required"}), 400

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('UPDATE history SET question = ?, answer = ? WHERE id = ?', (question, answer, id))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"}), 200



if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5002)
