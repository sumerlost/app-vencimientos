import tkinter as tk


def registro_decorator(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print("Se ha agregado un nuevo registro al sistema")
        return resultado

    return wrapper


def limpiar_campos(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        for arg in args:
            if isinstance(arg, tk.Entry):
                arg.delete("0", "end")

    return wrapper
