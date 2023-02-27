import sqlite3
from tkinter import messagebox as mb
from patrones import patronnumerico


class BaseDeDatos:
    def __init__(self, *arg, **kwargs):
        try:
            con = self.conexion()
            cursor = con.cursor()
            cursor.execute(
                "CREATE TABLE productos\
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,\
                        codigo INTEGER(15) NOT NULL, \
                        producto varchar(20) NOT NULL, fecha_de_vencimiento DATE NOT NULL)"
            )
        except:
            pass

    def conexion(self):
        con = sqlite3.connect("productos.db")
        return con

    def Alta(self, codigo, producto, fecha):
        sql = "SELECT * FROM productos WHERE codigo = ?"
        con = self.conexion()
        cursor = con.cursor()
        text = cursor.execute(sql, (codigo,))
        if text.fetchall():
            mb.showerror("error", "El codigo ya se encuentra registrado")
            return
        sql = "INSERT INTO productos(codigo, producto, fecha_de_vencimiento) VALUES(?, ?, ?)"
        datos = (codigo, producto, fecha)
        cursor.execute(sql, datos)
        con.commit()

    def Baja(self, item):
        con = self.conexion()
        cursor = con.cursor()
        sql = "DELETE FROM productos WHERE id = ?;"
        element = (item["text"],)
        cursor.execute(sql, element)
        con.commit()

    def Actualizar(self, controlador, codigo, producto, fecha, item):
        con = self.conexion()
        cursor = con.cursor()
        if controlador == 0:
            if not patronnumerico.match(codigo):
                mb.showerror("Error", "El codigo debe ser numerico")
                return
            sql = "SELECT * FROM productos WHERE codigo = ?"
            text = cursor.execute(sql, (codigo,))
            if text.fetchall():
                mb.showerror("error", "El codigo ya se encuentra registrado")
                return
        sql = "UPDATE productos SET codigo=?, producto=?, fecha_de_vencimiento=? WHERE id=?;"
        element = (codigo, producto, fecha, item["text"])
        cursor.execute(sql, element)
        con.commit()

    def Buscar(
        self,
    ):
        con = self.conexion()
        cursor = con.cursor()
        sql = "SELECT * FROM productos ORDER BY id DESC"
        text = cursor.execute(sql)
        return text.fetchall()
