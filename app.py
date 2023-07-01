from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()
ruta='/create'
ruta2='/login'


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route(ruta+'/')
def index():
    return render_template('/usuario/add.html')
    # data = db.read(None)

    #return render_template('usuario/index.html', data = data)
####producto###############





@app.route(ruta+'/add/')
def add():
    return render_template('/usuario/add.html')

@app.route('/create/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nsesion iniciada")
            return render_template('index.html')
        else:
            flash("ERROR, al iniciar sesion")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    

@app.route(ruta2+'/')
def index2():
    return render_template('/usuario/add.html')
    # data = db.read(None)

    #return render_template('usuario/index.html', data = data)
####producto###############



@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
