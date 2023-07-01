import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="alumnos" )

    def read(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM alumnos ")
            else:
                cursor.execute("SELECT * FROM alumnos where id = %s ", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO alumnos(username,nombre,apellido,clave) VALUES(%s,%s, %s, %s)", (data['username'],data['nombre'],data['apellido'],data['clave'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE usuario set nombre = %s, telefono = %s, email = %s where id = %s", (data['nombre'],data['telefono'],data['email'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM alumnos where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
