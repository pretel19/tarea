#from flask import Flask
from flask import render_template, Flask,flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario

from dao.DAOProducto import DAOProducto

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()
db2 = DAOProducto()
ruta='/usuario'
ruta2='/producto'


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route(ruta+'/')
# @app.route('/usuario/')
def index():
    data = db.read(None)

    return render_template('cuadro1/index.html', data = data)
####producto###############

@app.route(ruta2+'/')
# @app.route('/usuario/')
def index2():
    data = db2.read(None)

    return render_template('cuadro2/index.html', data = data)



@app.route(ruta+'/add/')
def add():
    return render_template('/cuadro1/add.html')

########producto##################

@app.route(ruta2+'/add/')
def add2():
    return render_template('/cuadro2/add.html')

####

@app.route(ruta+'/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo pedido creado")
        else:
            flash("ERROR, al crear pedido")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
###########producto###########

@app.route(ruta2+'/addusuario', methods = ['POST', 'GET'])
def addusuario2():
    if request.method == 'POST' and request.form['save']:
        if db2.insert(request.form):
            flash("Nuevo pedido creado")
        else:
            flash("ERROR, al crear pedido")

        return redirect(url_for('index2'))
    else:
        return redirect(url_for('index2'))
    
    
    
    
@app.route(ruta+'/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('cuadro1/update.html', data = data)
    
###########producto
    
@app.route(ruta2+'/update/<int:id>/')
def update2(id):
    data = db2.read(id);

    if len(data) == 0:
        return redirect(url_for('index2'))
    else:
        session['update'] = id
        return render_template('cuadro2/update.html', data = data)
    
    

@app.route(ruta+'/updateusuario', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
    
#######producro

@app.route(ruta2+'/updateusuario', methods = ['POST'])
def updateusuario2():
    if request.method == 'POST' and request.form['update']:

        if db2.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index2'))
    else:
        return redirect(url_for('index2'))
    
    
    
    
    

@app.route(ruta+'/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('cuadro1/delete.html', data = data)
    
##############producto
@app.route(ruta2+'/delete/<int:id>/')
def delete2(id):
    data = db2.read(id);

    if len(data) == 0:
        return redirect(url_for('index2'))
    else:
        session['delete'] = id
        return render_template('cuadro2/delete.html', data = data)
    



@app.route(ruta+'/deleteusuario', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
    
######## producto
@app.route(ruta2+'/deleteusuario', methods = ['POST'])
def deleteusuario2():
    if request.method == 'POST' and request.form['delete']:

        if db2.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index2'))
    else:
        return redirect(url_for('index2'))
    
    








#@app.route('/index3')
#def add():
#    return render_template('index3.html')


if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
