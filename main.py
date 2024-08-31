import secrets
from flask import Flask,redirect, render_template,request,flash

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    user = 'henrique@gmail.com'
    senhaUser = '123'

    if email == user and senha == senhaUser:
        return render_template('usuario.html')
    else:
        flash('Usuário Inválido')
        return redirect('/')

    
    


if __name__ in "__main__":
    app.run(debug=True)