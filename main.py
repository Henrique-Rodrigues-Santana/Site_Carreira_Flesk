import secrets
import json
from flask import Flask,redirect, render_template,request,flash

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    with open('dados.json') as usuarioTemp :
        usuarios = json.load(usuarioTemp)
        contador = 0

        for usuario in usuarios:
            contador += 1

            if usuario['email'] == 'admin@gmail.com' and usuario['senha'] == 'admin':
                return redirect('/admin')

            if usuario['email'] == email and usuario['senha'] == senha:
                return render_template('usuario.html')
            
            if contador >= len(usuarios):
                flash('Email ou senha invalidos')
                return redirect('/')

    
    


if __name__ in "__main__":
    app.run(debug=True)