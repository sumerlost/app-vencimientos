from tkinter import messagebox as mb
from Sql import BaseDeDatos
from tiempo import Tiempo
from patrones import patronnumerico
from Decoradores import registro_decorator
from Decoradores import limpiar_campos
from PatronObservador import Observable
from PatronObservador import Observador


# def actualizar_tree(tree):
#     records = tree.get_children()
#     for element in records:
#         tree.delete(element)
#     sql = "SELECT * FROM productos ORDER BY id DESC"
#     con = BaseDeDatos().conexion()
#     cursor = con.cursor()
#     datos = cursor.execute(sql)
#     resultado = datos.fetchall()
#     for x in resultado:
#         tree.insert("", 0, text=x[0], values=(x[1], x[2], x[3]))


class FuncionesP(Observable):
    def __init__(self) -> None:
        super().__init__()
        self.observador = Observador()
        self.registrar_observador(self.observador)

    @registro_decorator
    @limpiar_campos
    def agregar(self, codigo, producto, fecha, tree, e_codigo, e_producto, e_fecha):
        if Tiempo().formato_fecha(fecha) == True:
            pass
        else:
            return
        for x in codigo, producto, fecha:
            if not x:
                mb.showerror("error", "debe llenar los tres campos")
                return
        if not patronnumerico.match(codigo):
            mb.showerror("Error", "El codigo debe ser numerico")
            return
        BaseDeDatos().Alta(codigo, producto, fecha)
        self.notificar_observador(tree)

    def fborrar(self, tree, treeb):
        selec = treeb.focus()
        item = treeb.item(selec)
        BaseDeDatos().Baja(item)

        self.notificar_observador(tree)
        treeb.delete(selec)

    @limpiar_campos
    def update(
        self, codigo, producto, fecha, tree, treeb, e_codigo, e_producto, e_fecha
    ):
        selec = treeb.focus()
        item = treeb.item(selec)
        controlador = 0
        if not codigo:
            codigo = item["values"][0]
            controlador = 1
        if not producto:
            producto = item["values"][1]
        if not fecha:
            fecha = item["values"][2]

        if Tiempo().formato_fecha(fecha) == True:
            pass
        else:
            return
        BaseDeDatos().Actualizar(controlador, codigo, producto, fecha, item)
        treeb.delete(selec)
        self.notificar_observador(tree)

    @limpiar_campos
    def buscar(self, codigo, producto, fecha, treeb, e_codigo, e_producto, e_fecha):
        records = treeb.get_children()
        for element in records:
            treeb.delete(element)
        cont = 1
        control = 4
        for x in codigo, producto, fecha:
            if control != 4:
                if x:
                    mb.showerror("error", "solo puede buscar por uno de los campos")
                    return
            if x:
                control = cont
                busqueda = x
            cont += 1
        if control == 4:
            mb.showerror("error", "debe llenar un campo")
            return
        if control == 1:
            busqueda = int(busqueda)
        if control == 2:
            busqueda = str(busqueda)
        if control == 3:
            busqueda = str(busqueda)
        control = int(control)
        valores = BaseDeDatos().Buscar()
        for x in valores:
            if busqueda == x[control]:
                treeb.insert("", "end", text=x[0], values=(x[1], x[2], x[3]))
        if not treeb.get_children():
            mb.showinfo("", "no se encontraron resultados")
