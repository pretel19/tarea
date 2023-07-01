import pymysql
import mysql.connector


class DAOUsuario:
    def connect(self):
        config = {
        'user': '66ccdhwm4p33qkazs9us',
        'password': 'pscale_pw_SGzB9mdS0ucXAt4hSHlk5BdTh6eS75m8EqBMjPKtwzd',
        'host': 'aws.connect.psdb.cloud',
        'database': 'alumnos',
        'port': 'tu_puerto'
            }

    # Crea la conexión
        return  mysql.connector.connect(host="aws.connect.psdb.cloud",user="66ccdhwm4p33qkazs9us",password="pscale_pw_SGzB9mdS0ucXAt4hSHlk5BdTh6eS75m8EqBMjPKtwzd",db="alumnos")
        #return pymysql.connect(host="aws.connect.psdb.cloud",user="66ccdhwm4p33qkazs9us",password="pscale_pw_SGzB9mdS0ucXAt4hSHlk5BdTh6eS75m8EqBMjPKtwzd",db="alumnos" )

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
