import pymysql

class DAOProducto:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_poo" )

    def read(self, id):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM producto order by nombre asc")
            else:
                cursor.execute("SELECT * FROM producto where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO producto(nombre,telefono,email) VALUES(%s, %s, %s)", (data['nombre'],data['telefono'],data['email'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE producto set nombre = %s, telefono = %s, email = %s where id = %s", (data['nombre'],data['telefono'],data['email'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM producto where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
