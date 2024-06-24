import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import Peliculas, Puntos, Usuarios, borrar_puntuacion, listar_generos, listar_puntuaciones, listar_usuarios, listar_peliculas , guardar_peli, editar_peli, borrar_peli, borrar_usuario, guardar_usuario, editar_usuario, guardar_puntuacion, editar_puntuacion, listar_usuarios_select

def barrita_menu(root, app):
    barra = tk.Menu(root)
    root.config(menu = barra, width=900 , height=600)
    menu_inicio = tk.Menu(barra, tearoff=0)

    menu_peliculas = tk.Menu(barra, tearoff=False)
    menu_peliculas.add_command(
    label="Listado Películas",
    accelerator="Ctrl+P",
    command=app.verPeliculas
    )
    barra.add_cascade(label="Películas", menu=menu_peliculas)
    
    menu_usuarios = tk.Menu(barra, tearoff=False)
    menu_usuarios.add_command(
    label="Listado Usuarios",
    accelerator="Ctrl+U",
    command=app.verUsuarios
    )
    barra.add_cascade(menu=menu_usuarios, label="Usuarios")

    menu_puntos = tk.Menu(barra, tearoff=False)
    menu_puntos.add_command(
    label="Listado Puntuaciones",
    accelerator="Ctrl+V",
    command=app.verPuntuaciones
    )
    barra.add_cascade(menu=menu_puntos, label="Puntuaciones")

    #submenu
    """ menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB') """
    barra.add_cascade(label='Salir', menu = menu_inicio)
    menu_inicio.add_command(label='Salir', command= root.destroy) 


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=900,height=600)
        self.root = root
        self.pack()
        self.id_peli = None
        self.id_usuario = None 
        self.id_puntos = None
        self.verPeliculas()
    
    def verPeliculas(self):
        self.limpiarFormFrame()
        self.label_form_pelis()
        self.input_form_pelis()        
        self.botones_pelis()
        self.mostrar_peliculas()
        self.footer()

    def verUsuarios(self):
        self.limpiarFormFrame()
        self.label_form_usuario()
        self.input_form_usuario()        
        self.botones_usuarios()
        self.mostrar_usuarios()
        self.footer()

    def verPuntuaciones(self):
        self.limpiarFormFrame()
        self.label_form_puntos()
        self.input_form_puntos()        
        self.botones_puntos()
        self.mostrar_puntos()
        self.footer()

    def eliminarTablas(self):
        if (hasattr(self, "tabla_peliculas")):
            self.tabla_peliculas.grid_remove()   
        if (hasattr(self, "scroll_peliculas")):
            self.scroll_peliculas.grid_remove()   
        if (hasattr(self, "tabla_usuarios")):
            self.tabla_usuarios.grid_remove()   
        if (hasattr(self, "scroll_usuarios")):
            self.scroll_usuarios.grid_remove() 
        if (hasattr(self, "tabla_puntos")):
            self.tabla_puntos.grid_remove()   
        if (hasattr(self, "scroll_puntos")):
            self.scroll_puntos.grid_remove()   


    def limpiarFormFrame(self):
        #labels
        if (hasattr(self,"label_nombre")):
            self.label_nombre.grid_remove()
        if (hasattr(self,"label_apellido")):
            self.label_apellido.grid_remove()
        if (hasattr(self,"label_pelicula")):
            self.label_pelicula.grid_remove()
        if (hasattr(self,"label_duracion")):
            self.label_duracion.grid_remove()
        if (hasattr(self,"label_genero")):
            self.label_genero.grid_remove()
        if (hasattr(self,"label_usuario")):
            self.label_usuario.grid_remove()
        if (hasattr(self,"label_puntos")):
            self.label_puntos.grid_remove()
        if (hasattr(self,"label_observaciones")):
            self.label_observaciones.grid_remove()
        #entries
        if (hasattr(self,"entry_nombre")):    
            self.entry_nombre.grid_remove()
        if (hasattr(self,"entry_apellido")):    
            self.entry_apellido.grid_remove()
        if (hasattr(self,"entry_pelicula")):    
            self.entry_pelicula.grid_remove()
        if (hasattr(self,"entry_duracion")):    
            self.entry_duracion.grid_remove()
        if (hasattr(self,"entry_genero")):    
            self.entry_genero.grid_remove()      
        if (hasattr(self,"entry_usuario")):    
            self.entry_usuario.grid_remove()      
        if (hasattr(self,"entry_puntos")):    
            self.entry_puntos.grid_remove()  
        if (hasattr(self,"entry_observaciones")):    
            self.entry_observaciones.grid_remove()      

        if (hasattr(self, "btn_alta")):
            self.btn_alta.grid_remove()
        if (hasattr(self, "btn_modi")):
            self.btn_modi.grid_remove()           
        if (hasattr(self, "btn_cance")):
            self.btn_cance.grid_remove()   
        if (hasattr(self, "btn_editar")):
            self.btn_editar.grid_remove()   
        if (hasattr(self, "btn_delete")):
            self.btn_delete.grid_remove()   

        if (hasattr(self, "btn_alta_usuario")):
            self.btn_alta_usuario.grid_remove()
        if (hasattr(self, "btn_modi_usuario")):
            self.btn_modi_usuario.grid_remove()           
        if (hasattr(self, "btn_cance_usuario")):
            self.btn_cance_usuario.grid_remove()     
        if (hasattr(self, "btn_editar_usuario")):
            self.btn_editar_usuario.grid_remove()   
        if (hasattr(self, "btn_delete_usuario")):
            self.btn_delete_usuario.grid_remove()   

        if (hasattr(self, "btn_alta_puntos")):
            self.btn_alta_puntos.grid_remove()
        if (hasattr(self, "btn_modi_puntos")):
            self.btn_modi_puntos.grid_remove()           
        if (hasattr(self, "btn_cance_puntos")):
            self.btn_cance_puntos.grid_remove()      
        if (hasattr(self, "btn_editar_puntos")):
            self.btn_editar_puntos.grid_remove()   
        if (hasattr(self, "btn_delete_puntos")):
            self.btn_delete_puntos.grid_remove()   

        self.eliminarTablas()


    def label_form_pelis(self):        

        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial',11,'bold'))
        self.label_nombre.grid(row= 0, column=0,pady=1)

        self.label_duracion = tk.Label(self, text="Duración: ")
        self.label_duracion.config(font=('Arial',11,'bold'))
        self.label_duracion.grid(row= 1, column=0,pady=1)

        self.label_genero = tk.Label(self, text="Genero: ")
        self.label_genero.config(font=('Arial',11,'bold'))
        self.label_genero.grid(row= 2, column=0,pady=1)    

    def input_form_pelis(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre)
        self.entry_nombre.config(width=50, state='disabled',font=('Arial',11))
        self.entry_nombre.grid(row=0, column=1,pady=1, ipadx=10)

        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self,textvariable=self.duracion)
        self.entry_duracion.config(width=50, state='disabled',font=('Arial',11))
        self.entry_duracion.grid(row=1, column=1,pady=1, ipadx=10)

        #aca limpiamos la lista de tuplas que nos retorna la funcion
        x = listar_generos()
        y = []
        for i in x:
            y.append(i[1])
    
        #concatenemos el nuevo array
        self.generos = ['Seleccione uno'] + y
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=50, state='disabled',font=('Arial',11))
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row=2, column=1,pady=1, ipadx=0)      

    def label_form_usuario(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial',11,'bold'))
        self.label_nombre.grid(row= 0, column=0,pady=1)

        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.config(font=('Arial',11,'bold'))
        self.label_apellido.grid(row= 1, column=0,pady=1)

    def input_form_usuario(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre)
        self.entry_nombre.config(width=50, state='disabled',font=('Arial',11))
        self.entry_nombre.grid(row= 0, column=1,pady=1, ipadx=10)

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self,textvariable=self.apellido)
        self.entry_apellido.config(width=50, state='disabled',font=('Arial',11))
        self.entry_apellido.grid(row= 1, column=1,pady=1, ipadx=10)              
        
    def label_form_puntos(self):
        self.label_pelicula = tk.Label(self, text="Película: ")
        self.label_pelicula.config(font=('Arial',11,'bold'))
        self.label_pelicula.grid(row= 0, column=0,pady=1)

        self.label_usuario = tk.Label(self, text="Usuario: ")
        self.label_usuario.config(font=('Arial',11,'bold'))
        self.label_usuario.grid(row= 1, column=0,pady=1)

        self.label_puntos = tk.Label(self, text="Puntuación: ")
        self.label_puntos.config(font=('Arial',11,'bold'))
        self.label_puntos.grid(row= 2, column=0,pady=1)

        self.label_observaciones = tk.Label(self, text="Observaciones: ")
        self.label_observaciones.config(font=('Arial',11,'bold'))
        self.label_observaciones.grid(row= 3, column=0,pady=1)
        
    def input_form_puntos(self):

        aux = listar_peliculas()        
        pelis = []
        for i in aux:
            pelis.append(i[1])
    
        print(aux)
        #concatenemos el nuevo array
        self.peliculas = ['Seleccione una'] + pelis
        self.entry_pelicula = ttk.Combobox(self, state="readonly")
        self.entry_pelicula['values'] = self.peliculas
        self.entry_pelicula.current(0)
        self.entry_pelicula.config(width=50, state='disabled',font=('Arial',11))
        self.entry_pelicula.bind("<<ComboboxSelected>>")
        self.entry_pelicula.grid(row=0, column=1,pady=1, ipadx=0)      


        aux2 = listar_usuarios_select()        
        usuarios = []
        for i in aux2:
            usuarios.append(i[1])
    
        #concatenemos el nuevo array
        self.usuarios = ['Seleccione un'] + usuarios
        self.entry_usuario = ttk.Combobox(self, state="readonly")
        self.entry_usuario['values'] = self.usuarios
        self.entry_usuario.current(0)
        self.entry_usuario.config(width=50, state='disabled',font=('Arial',11))
        self.entry_usuario.bind("<<ComboboxSelected>>")
        self.entry_usuario.grid(row=1, column=1,pady=1, ipadx=0)     

        self.puntos= tk.StringVar()
        self.entry_puntos = tk.Entry(self,textvariable=self.puntos)
        self.entry_puntos.config(width=50, state='disabled',font=('Arial',11))
        self.entry_puntos.grid(row=2, column=1,pady=1, ipadx=10)

        self.observaciones= tk.StringVar()
        self.entry_observaciones = tk.Entry(self,textvariable=self.observaciones)
        self.entry_observaciones.config(width=50, state='disabled',font=('Arial',11))
        self.entry_observaciones.grid(row=3, column=1,pady=1, ipadx=10)
 
    def botones_usuarios(self):
        self.btn_alta_usuario = tk.Button(self, text='Cargar', command=self.habilitar_campos_usuario)
        self.btn_alta_usuario.config(width= 10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='green',cursor='hand2',activebackground='#3FD83F',activeforeground='black')
        self.btn_alta_usuario.grid(row=0, column=2,padx=5, pady=1)

        self.btn_editar_usuario = tk.Button(self, text='Editar',command=self.editar_usuario)
        self.btn_editar_usuario.config(width= 10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='darkgreen',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar_usuario.grid(row=3, column=2,padx=5, pady=1)

        self.btn_delete_usuario = tk.Button(self, text='Borrar', command=self.eliminar_usuario)
        self.btn_delete_usuario.config(width= 10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='red',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete_usuario.grid(row=4, column=2,padx=5, pady=1)

        self.btn_modi_usuario = tk.Button(self, text='Guardar', command= self.guardar_campos_usuario)
        self.btn_modi_usuario.config(width= 10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='orange',cursor='hand2',activebackground='#7594F5',activeforeground='black',state='disabled')
        self.btn_modi_usuario.grid(row=1, column=2,padx=5, pady=1)

        self.btn_cance_usuario = tk.Button(self, text='Cancelar', command=self.bloquear_campos_usuario)
        self.btn_cance_usuario.config(width= 10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='grey',cursor='hand2',activebackground='#F35B5B',activeforeground='black',state='disabled')
        self.btn_cance_usuario.grid(row=2, column=2,padx=5, pady=1)

    def botones_pelis(self):
        self.btn_alta = tk.Button(self, text='Cargar', command=self.habilitar_campos)
        self.btn_alta.config(width=10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='green',cursor='hand2',activebackground='#3FD83F',activeforeground='black')
        self.btn_alta.grid(row=0,column=2,padx=5, pady=1)

        self.btn_editar = tk.Button(self, text='Editar',command=self.editar_registro)
        self.btn_editar.config(width=10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='darkgreen',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row=3, column=2,padx=5, pady=1)

        self.btn_delete = tk.Button(self, text='Borrar', command=self.eliminar_registro)
        self.btn_delete.config(width=10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='red',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row=4, column=2,padx=5, pady=1)

        self.btn_modi = tk.Button(self, text='Guardar', command= self.guardar_campos)
        self.btn_modi.config(width=10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='orange',cursor='hand2',activebackground='#7594F5',activeforeground='black',state='disabled')
        self.btn_modi.grid(row=1,column=2,padx=5, pady=1)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width=10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='grey',cursor='hand2',activebackground='#F35B5B',activeforeground='black',state='disabled')
        self.btn_cance.grid(row=2,column=2,padx=5, pady=1)
    
    def botones_puntos(self):
        self.btn_alta_puntos = tk.Button(self, text='Cargar', command=self.habilitar_campos_puntos)
        self.btn_alta_puntos.config(width=10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='green',cursor='hand2',activebackground='#3FD83F',activeforeground='black')
        self.btn_alta_puntos.grid(row=0,column=2,padx=5, pady=1)

        self.btn_editar_puntos = tk.Button(self, text='Editar',command=self.editar_puntos)
        self.btn_editar_puntos.config(width= 10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='darkgreen',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar_puntos.grid(row=3, column=2,padx=5, pady=1)

        self.btn_delete_puntos = tk.Button(self, text='Borrar ', command=self.eliminar_puntos)
        self.btn_delete_puntos.config(width= 10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='red',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete_puntos.grid(row=4, column=2,padx=5, pady=1)

        self.btn_modi_puntos = tk.Button(self, text='Guardar', command= self.guardar_campos_puntos)
        self.btn_modi_puntos.config(width=10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='orange',cursor='hand2',activebackground='#7594F5',activeforeground='black',state='disabled')
        self.btn_modi_puntos.grid(row=1,column=2,padx=5, pady=1)

        self.btn_cance_puntos = tk.Button(self, text='Cancelar', command=self.bloquear_campos_puntos)
        self.btn_cance_puntos.config(width=10,font=('Arial', 11,'bold'),fg ='#FFFFFF' , bg='grey',cursor='hand2',activebackground='#F35B5B',activeforeground='black',state='disabled')
        self.btn_cance_puntos.grid(row=2, column=2,padx=5, pady=1)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')
    
    def habilitar_campos_usuario(self):
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.btn_modi_usuario.config(state='normal')
        self.btn_cance_usuario.config(state='normal')
        self.btn_alta_usuario.config(state='disabled')

    def habilitar_campos_puntos(self):
        self.entry_pelicula.config(state='normal')
        self.entry_usuario.config(state='normal')
        self.entry_puntos.config(state='normal')
        self.entry_observaciones.config(state='normal')
        self.btn_modi_puntos.config(state='normal')
        self.btn_cance_puntos.config(state='normal')
        self.btn_alta_puntos.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_genero.current(0)
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.nombre.set('')
        self.duracion.set('')
        self.id_peli = None #reseteanis el id luego de eliminar
        self.btn_alta.config(state='normal')

    def bloquear_campos_puntos(self):
        self.entry_pelicula.config(state='disabled')
        self.entry_pelicula.current(0)
        self.entry_usuario.config(state='disabled')
        self.entry_usuario.current(0)
        self.entry_puntos.config(state='disabled')
        self.entry_observaciones.config(state='disabled')     
        self.btn_modi_puntos.config(state='disabled')
        self.btn_cance_puntos.config(state='disabled')    
        self.puntos.set('')
        self.observaciones.set('')
        self.id_puntos = None #reseteanis el id luego de eliminar
        self.btn_alta_puntos.config(state='normal')

    def bloquear_campos_usuario(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')      
        self.btn_modi_usuario.config(state='disabled')
        self.btn_cance_usuario.config(state='disabled')
        self.nombre.set('')
        self.apellido.set('')
        self.id_usuario = None #reseteanis el id luego de eliminar
        self.btn_alta_usuario.config(state='normal')

    def getGeneroId(self, desc):
        aux = listar_generos()              
        for n in aux:
            t = list(n)            
            if (t[1] == desc):
                return t[0]
        return None
        
    def getPeliculaId(self, desc):
        aux = listar_peliculas()      
        for n in aux:
            t = list(n)
            if (t[1] == desc):
                return t[0]
        return None
        
    def getUsuarioId(self, desc):
        aux = listar_usuarios()      
        for n in aux:
            t = list(n)          
            if ((t[1] + ' ' + t[2]) == desc):
                return t[0]
        return None

    def guardar_campos(self):
        pelicula = Peliculas(
            self.nombre.get(),
            self.duracion.get(),
            self.getGeneroId(self.entry_genero.get())
        )

        if self.id_peli == None:
            guardar_peli(pelicula)
        else:
            editar_peli(pelicula, int(self.id_peli))

        self.mostrar_peliculas()
        self.bloquear_campos()

    def guardar_campos_usuario(self):
        usuario = Usuarios(
            self.nombre.get(),
            self.apellido.get(),           
        )

        if self.id_usuario == None:
            guardar_usuario(usuario)
        else:
            editar_usuario(usuario, int(self.id_usuario))

        self.mostrar_usuarios()
        self.bloquear_campos_usuario()

    def guardar_campos_puntos(self):
        puntos = Puntos(
            self.getPeliculaId(self.entry_pelicula.get()),
            self.getUsuarioId(self.entry_usuario.get()),           
            self.puntos.get(),
            self.observaciones.get(),
        )
        print(puntos)        

        if self.id_puntos == None:
            guardar_puntuacion(puntos)
        else:
            editar_puntuacion(puntos, int(self.id_puntos))

        self.mostrar_puntos()
        self.bloquear_campos_puntos()

    def mostrar_peliculas(self):
        self.eliminarTablas()

        self.lista_p = listar_peliculas()
        #print(listar_peliculas())
        self.lista_p.reverse() #para invertir el orden
        self.tabla_peliculas = ttk.Treeview(self, columns=('Nombre','Duración','Genero'))
        self.tabla_peliculas.grid(row=5,column=1,padx=10 , pady=20)

        #self.tabla_peliculas.column("Nombre", anchor="s")    

        self.scroll_peliculas = ttk.Scrollbar(self, orient='vertical', command=self.tabla_peliculas.yview)
        self.scroll_peliculas.grid(row=5, column=5,sticky='nse')
        self.tabla_peliculas.configure(yscrollcommand= self.scroll_peliculas.set)

        self.tabla_peliculas.heading('#0',text='     ID', anchor="sw")
        self.tabla_peliculas.heading('#1',text='Nombre', anchor="sw")
        self.tabla_peliculas.heading('#2',text='Duración', anchor="sw")
        self.tabla_peliculas.heading('#3',text='Genero', anchor="sw")
       
        for p in self.lista_p:
            self.tabla_peliculas.insert('',0,text=p[0],values = (p[1],p[2],p[5]))     

    def mostrar_usuarios(self):
        self.eliminarTablas()

        self.lista_u = listar_usuarios()       
        self.lista_u.reverse() #para invertir el orden
        self.tabla_usuarios = ttk.Treeview(self, columns=('Nombre','Apellido'))
        self.tabla_usuarios.grid(row=5,column=1,padx=10, pady=20)

        self.scroll_usuarios = ttk.Scrollbar(self, orient='vertical', command=self.tabla_usuarios.yview)
        self.scroll_usuarios.grid(row=5, column=5,sticky='nse')
        self.tabla_usuarios.configure(yscrollcommand= self.scroll_usuarios.set)

        self.tabla_usuarios.heading('#0',text='     ID', anchor="sw")
        self.tabla_usuarios.heading('#1',text='Nombre', anchor="sw")
        self.tabla_usuarios.heading('#2',text='Apellido', anchor="sw")
       
        for u in self.lista_u:
            self.tabla_usuarios.insert('',0,text=u[0],
                              values = (u[1],u[2], ''))      
    def mostrar_puntos(self):
        self.eliminarTablas()

        self.lista_pu = listar_puntuaciones()
        self.lista_pu.reverse() #para invertir el orden
        self.tabla_puntos = ttk.Treeview(self, columns=('ID Película', 'Película', 'ID Usuario','Usuario','Puntuación', 'Observaciones'))
        self.tabla_puntos.grid(row=5,column=1, padx=10, pady=20)

        self.scroll_puntos = ttk.Scrollbar(self, orient='vertical', command=self.tabla_puntos.yview)
        self.scroll_puntos.grid(row=5, column=5,sticky='nse')
        self.tabla_puntos.configure(yscrollcommand= self.scroll_puntos.set)

        self.tabla_puntos.heading('#0',text='     ID', anchor="sw")
        self.tabla_puntos.heading('#1',text='ID Película', anchor="sw")
        self.tabla_puntos.heading('#2',text='Película', anchor="sw")
        self.tabla_puntos.heading('#3',text='ID Usuario', anchor="sw")
        self.tabla_puntos.heading('#4',text='Usuario', anchor="sw")
        self.tabla_puntos.heading('#5',text='Puntuación', anchor="sw")
        self.tabla_puntos.heading('#6',text='Observaciones', anchor="sw")
    
        for p in self.lista_pu:
            self.tabla_puntos.insert('',0,text=p[0],
                            values = (p[1],p[5],p[2],p[6],p[3],p[4]))
            #print(p)
      
    def editar_registro(self):
        try:
            self.id_peli = self.tabla_peliculas.item(self.tabla_peliculas.selection())['text']

            self.nombre_peli_e = self.tabla_peliculas.item(self.tabla_peliculas.selection())['values'][0]
            self.dura_peli_e = self.tabla_peliculas.item(self.tabla_peliculas.selection())['values'][1]
            self.gene_peli_e = self.tabla_peliculas.item(self.tabla_peliculas.selection())['values'][2]

            self.habilitar_campos()
            self.nombre.set(self.nombre_peli_e)
            self.duracion.set(self.dura_peli_e)
            self.entry_genero.current(self.generos.index(self.gene_peli_e))

        except:
            pass
    def eliminar_registro(self):
        try:
            self.id_peli = self.tabla_peliculas.item(self.tabla_peliculas.selection())['text']
            borrar_peli(int(self.id_peli))
            self.mostrar_peliculas()
            self.id_peli = None 
        except:
            pass

    def editar_usuario(self):
        try:
            self.id_usuario = self.tabla_usuarios.item(self.tabla_usuarios.selection())['text']

            self.nombre_usuario_e = self.tabla_usuarios.item(self.tabla_usuarios.selection())['values'][0]
            self.apellido_usuario_e = self.tabla_usuarios.item(self.tabla_usuarios.selection())['values'][1]
           
            self.habilitar_campos_usuario()
            self.nombre.set(self.nombre_usuario_e)
            self.apellido.set(self.apellido_usuario_e)          

        except:
            pass
    def eliminar_usuario(self):
        try:
            self.id_usuario = self.tabla_usuarios.item(self.tabla_usuarios.selection())['text']
            borrar_usuario(int(self.id_usuario))
            self.mostrar_usuarios()
            self.id_usuario = None 
        except:
            pass

    def editar_puntos(self):
        try:         
            self.id_puntos = self.tabla_puntos.item(self.tabla_puntos.selection())['text']            
            self.pelicula_e = self.tabla_puntos.item(self.tabla_puntos.selection())['values'][1]            
            self.usuario_e = self.tabla_puntos.item(self.tabla_puntos.selection())['values'][3]
            self.puntos_e = self.tabla_puntos.item(self.tabla_puntos.selection())['values'][4]
            self.observaciones_e = self.tabla_puntos.item(self.tabla_puntos.selection())['values'][5]
            self.habilitar_campos_puntos()
            self.entry_pelicula.current(self.peliculas.index(self.pelicula_e))
            self.entry_usuario.current(self.usuarios.index(self.usuario_e))
            self.puntos.set(self.puntos_e)
            self.observaciones.set(self.observaciones_e)

        except:
            pass
    def eliminar_puntos(self):
        try:
            self.id_puntos= self.tabla_puntos.item(self.tabla_puntos.selection())['text']
            borrar_puntuacion(int(self.id_puntos))
            self.mostrar_puntos()
            self.id_puntos= None 
        except:
            pass

    def footer(self):
        self.label_footer = tk.Label(self, text="Tecno 3F - Python Intermedio - 2024 - Baglivo Matías & Pinasco Marina")
        self.label_footer.config(font=('Arial',10,'bold'))
        self.label_footer.grid(row= 10, column=0,padx=10,pady=10, columnspan=4)
