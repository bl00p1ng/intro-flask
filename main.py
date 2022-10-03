from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

# Lista de tareas
toDos = ['Estudiar Python', 'Estudiar JavaScript', 'Estudiar Inglés']


@app.route('/')
def index():
    # Obtnener IP del usuario
    user_ip = request.remote_addr
    # Redirigir a /hello
    response = make_response(redirect('/hello'))
    # Guardar IP en una cookie
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    # Obtener la IP del usuario desde una cookie
    user_ip = request.cookies.get('user_ip')

    context = {
        "user_ip": user_ip,
        "toDos": toDos
    }
    # Mostrar template con la IP del usuario
    return render_template('hello.html', **context)
