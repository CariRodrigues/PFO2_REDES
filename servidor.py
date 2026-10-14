import sqlite3
from flask import Flask, request, jsonify, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DB_NAME = "database.db"

# Inicializamos la DB
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    #Tabla para almacenar usuarios con contraseña hasheada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#Ejecutamos la inicialización
init_db()

#Endpoint: Registro de usuarios (POST /registro)
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    password = data.get('contraseña')
    if not usuario or not password:
        return jsonify({"mensaje": "Faltan datos de usuario o contraseña"}), 400
    hashed_password = generate_password_hash(password)
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)", (usuario, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({"mensaje": f"Usuario '{usuario}' registrado con éxito"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"mensaje": "El nombre de usuario ya existe"}), 400


#Endpoint: Inicio de sesión (POST /login)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    password = data.get('contraseña')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash from usuarios WHERE usuario = ?", (usuario,))
    row = cursor.fetchone()
    conn.close()
    if row and check_password_hash(row[0], password):
        return jsonify({"mensaje": f"Bienvenido/a {usuario}, inicio de sesión exitoso"}), 200
    else: 
        return jsonify({"mensaje": "usuario o contraseña incorrectas"}), 401

#Endpoint: Gestión de tareas (GET /tareas)
@app.route('/tareas', methods=['GET'])
def tareas():
    html_welcome = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenida - Sistema de Tareas</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
            .card { background: white; padding: 20px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡Bienvenido/a al Sistema de Gestión de Tareas!</h1>
            <p>Has accedido correctamente </p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_welcome)

if __name__ == '__main__':
    app.run(debug=True, port=5000)