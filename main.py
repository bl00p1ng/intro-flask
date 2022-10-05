from urllib import response
from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

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


@app.route('/platzi')
def platzi():
    # Redirigir a Platzi.com
    response = make_response(redirect('https://platzi.com'))

    return response


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)
