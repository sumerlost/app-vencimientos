from tkinter import ttk
from tkinter import StringVar
from tkinter import Menu
from tkinter import CENTER
from modelo import FuncionesP
from tiempo import Tiempo

from PatronObservador import Observador


def principal(root):
    root.geometry("750x300")
    l_codigo = ttk.Label(root, text="codigo")
    l_producto = ttk.Label(root, text="Producto")
    l_fecha = ttk.Label(root, text="fecha vencimiento")
    b_agregar = ttk.Button(
        root,
        text="Agregar",
        command=lambda: FuncionesP().agregar(
            codigo.get(),
            producto.get(),
            fecha.get(),
            tree,
            e_codigo,
            e_fecha,
            e_producto,
        ),
    )
    b_borrar = ttk.Button(
        root, text="Borrar", command=lambda: FuncionesP().fborrar(tree, treeb)
    )
    b_buscar = ttk.Button(
        root,
        text="Buscar",
        command=lambda: FuncionesP().buscar(
            codigo.get(),
            producto.get(),
            fecha.get(),
            treeb,
            e_codigo,
            e_producto,
            e_fecha,
        ),
    )
    b_update = ttk.Button(
        root,
        text="actualizar",
        command=lambda: FuncionesP().update(
            codigo.get(),
            producto.get(),
            fecha.get(),
            tree,
            treeb,
            e_codigo,
            e_producto,
            e_fecha,
        ),
    )
    codigo = StringVar()
    producto = StringVar()
    fecha = StringVar()
    e_codigo = ttk.Entry(root, textvariable=codigo)
    e_producto = ttk.Entry(root, textvariable=producto)
    e_fecha = ttk.Entry(root, textvariable=fecha)

    # MENU #

    menuvoid = Menu(root)
    menuarchivo = Menu(menuvoid, tearoff=0)
    menufun = Menu(menuvoid, tearoff=0)
    menufun.add_command(
        label="Vencimientos cercanos", command=lambda: Tiempo().cerebro(treeb)
    )
    menuarchivo.add_command(
        label="Abrir", command=lambda: Observador().actualizar_tree(tree)
    )
    menuarchivo.add_separator()
    menuarchivo.add_command(label="Salir", command=root.quit)
    menuvoid.add_cascade(label="Archivo", menu=menuarchivo)
    menuvoid.add_cascade(label="funciones", menu=menufun)
    root.config(menu=menuvoid)

    root.resizable(width=False, height=False)
    root.title("Vencimientos")

    treeb = ttk.Treeview(root)
    treeb["columns"] = ("col1", "col2", "col3")
    treeb.column("#0", width=0, minwidth=0, anchor="w")
    treeb.column("col1", width=80, minwidth=80)
    treeb.column("col2", width=100, minwidth=100)
    treeb.column("col3", width=150, minwidth=150)
    tree = ttk.Treeview(root, selectmode="none")
    tree["columns"] = ("col1", "col2", "col3")
    tree.column("#0", width=0, minwidth=0, anchor="w")
    tree.column("col1", width=80, minwidth=80)
    tree.column("col2", width=100, minwidth=100)
    tree.column("col3", width=150, minwidth=150)

    tree.heading("col1", text="codigo", anchor=CENTER)
    tree.heading("col2", text="producto", anchor=CENTER)
    tree.heading("col3", text="fecha vencimiento", anchor=CENTER)
    l_codigo.place(x=10, y=20)
    l_producto.place(x=10, y=40)
    l_fecha.place(x=10, y=60)
    e_codigo.place(x=150, y=20)
    e_producto.place(x=150, y=40)
    e_fecha.place(x=150, y=60)
    tree.place(x=390, y=20)
    treeb.place(x=10, y=150, height=96, width=335)
    barrap = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    barrap.pack(side="right", fill="y")
    tree.configure(yscrollcommand=barrap.set)
    barrab = ttk.Scrollbar(root, orient="vertical", command=treeb.yview)
    barrab.place(x=350, y=170)
    treeb.configure(yscrollcommand=barrab.set)

    b_update.place(x=150, y=120)
    b_agregar.place(x=10, y=90)
    b_borrar.place(x=150, y=90)
    b_buscar.place(x=10, y=120)
    b_frame = ttk.LabelFrame(root)
