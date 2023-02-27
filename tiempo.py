from tkinter import messagebox as mb
import datetime as dt
from Sql import BaseDeDatos
from patrones import patronfecha


class Tiempo:
    def __init__(self, *arg, **kwargs):
        pass

    def formato_fecha(self, fecha):
        if patronfecha.match(fecha):
            dia, mes, año = fecha.split("/")
            if int(año) > 68:
                mb.showerror("error", "fuera de rango de años (hasta 2068")
                return
            try:
                fecha = dt.datetime.strptime(fecha, "%d/%m/%y")
            except:
                mb.showerror("error", "el mes tiene menos dias")
                return
            if fecha < dt.datetime.today():
                mb.showerror("error", "fecha invalida (pasado)")
                return
        else:
            try:
                dia, mes, año = fecha.split("/")
            except:
                mb.showerror("error", "usar formato: dd/mm/aa")
                return
            if int(dia) > 31:
                mb.showerror("error", "dias maximos: 31")
                return
            if int(mes) > 12:
                mb.showerror("error", "meses maximos: 12")
                return
            if int(año) > 99:
                mb.showerror(
                    "error", "ingresar el año solo con sus ultimos dos digitos"
                )
                return
        año = int(año)
        if año < 10:
            mb.showerror("error", "fecha invalida (pasado)")
            return False
        return True

    def cerebro(self, treeb):
        hoy = dt.datetime.now().strftime("%d/%m/%y")
        hoy = dt.datetime.strptime(hoy, "%d/%m/%y")

        con = BaseDeDatos().conexion()
        cursor = con.cursor()
        sql = "SELECT * FROM productos"
        text = cursor.execute(sql)
        valores = text.fetchall()
        fechas = []
        for x in valores:
            fecha = x[3]
            fecha = dt.datetime.strptime(fecha, "%d/%m/%y")
            delta = fecha - hoy
            if delta < dt.timedelta(weeks=1):
                fechas = [x]
        if fechas:
            mb.showinfo("alerta", "vencimientos cerca, presentados en pantalla")
            for x in fechas:
                treeb.insert("", "end", text=x[0], values=(x[1], x[2], x[3]))
        else:
            mb.showinfo("", "no hay vencimientos cercanos")
