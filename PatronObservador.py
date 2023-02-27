from Sql import BaseDeDatos


class Observador:
    def __init__(self) -> None:
        pass

    def actualizar_tree(self, tree):
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        resultado = BaseDeDatos().Buscar()
        for x in resultado:
            tree.insert("", 0, text=x[0], values=(x[1], x[2], x[3]))


class Observable:
    def __init__(self):
        self.observador = None

    def eliminar_observador(self):
        self.observador = None

    def notificar_observador(self, tree):
        if self.observador:
            self.observador.actualizar_tree(tree)

    def registrar_observador(self, observador):
        self.observador = observador
