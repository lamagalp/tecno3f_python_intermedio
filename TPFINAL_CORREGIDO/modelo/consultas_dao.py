from .conneciondb import ConeccionDB

def crear_tabla():    
    conn = ConeccionDB()

    sql = '''
            CREATE TABLE IF NOT EXISTS Genero(
            ID INTEGER NOT NULL, 
            Nombre VARCHAR(50),
            PRIMARY KEY (ID AUTOINCREMENT)
            );

            CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER NOT NULL, 
            Nombre VARCHAR(150),
            Duracion VARCHAR(4),
            Genero INTEGER,
            PRIMARY KEY (ID AUTOINCREMENT),
            FOREIGN KEY (Genero) References Genero(ID)
            );

            CREATE TABLE IF NOT EXISTS Usuarios(
            ID INTEGER NOT NULL, 
            Nombre VARCHAR(50),
            Apellido VARCHAR(50),
            PRIMARY KEY (ID AUTOINCREMENT)
            );

            CREATE TABLE IF NOT EXISTS Puntuaciones(
            ID INTEGER NOT NULL, 
            Pelicula INTEGER NOT NULL,
			Usuario INTEGER NOT NULL,      
            Puntuacion INTEGER NOT NULL,
            Observaciones VARCHAR(200),                
            PRIMARY KEY (ID AUTOINCREMENT),
            FOREIGN KEY (Pelicula) References Peliculas(ID)
            FOREIGN KEY (Usuario) References Usuarios(ID)
            );           
            '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()

    except:
        pass

def listar_generos():
    conn = ConeccionDB()
    listar_generos = []
    sql = """
            SELECT * FROM Genero
         """
    
    try:
        conn.cursor.execute(sql)
        listar_generos = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_generos
    except:
        pass
def listar_usuarios():
    conn = ConeccionDB()
    listar_usuarios = []
    sql = """
            SELECT * FROM Usuarios
         """
    
    try:
        conn.cursor.execute(sql)
        listar_usuarios = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_usuarios
    except:
        pass

def listar_usuarios_select():
    conn = ConeccionDB()
    listar_usuarios = []
    sql = """
            SELECT ID, Nombre || ' ' || Apellido FROM Usuarios
         """
    
    try:
        conn.cursor.execute(sql)
        listar_usuarios = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_usuarios
    except:
        pass

def listar_peliculas():
    conn = ConeccionDB()
    listar_peliculas = []
    sql = """
            SELECT * FROM Peliculas as p
            inner join Genero as g
            on p.Genero = g.ID           
         """
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except:
        pass

def listar_puntuaciones():
    conn = ConeccionDB()
    listar_puntos = []
    sql = """
            SELECT  p.ID, Pelicula, Usuario, Puntuacion, Observaciones, pe.Nombre , u.Nombre || ' ' || u.Apellido FROM Puntuaciones as p
            inner join Peliculas as pe
            on p.Pelicula = pe.ID           
            inner join Usuarios as u
            on p.Usuario = u.ID           
         """
    #print(sql)
    try:
        conn.cursor.execute(sql)
        listar_puntos = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_puntos
    except:
        pass

class Peliculas:
    def __init__(self, nombre,duracion, genero):
        self.id_peliculas = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero       

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion}, {self.genero}]'

class Usuarios:
    def __init__(self, nombre,apellido):
        self.id_usuarios = None
        self.nombre = nombre
        self.apellido = apellido
 

    def __str__(self):
        return f'Usuario[{self.nombre},{self.apellido}]'

class Puntos:
    def __init__(self, pelicula,usuario, puntos, observaciones):
        self.id_puntos = None
        self.pelicula = pelicula
        self.usuario = usuario
        self.puntuacion = puntos
        self.observaciones = observaciones
 

    def __str__(self):
        return f'Puntuacion[{self.pelicula},{self.usuario},{self.puntuacion},{self.observaciones}]'

def guardar_peli(pelicula):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Peliculas (Nombre,Duracion,Genero)
            VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.genero});
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()
def editar_peli(pelicula, id):
    conn = ConeccionDB()

    sql = f"""
            UPDATE Peliculas
            SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}',Genero = {pelicula.genero}
            WHERE ID = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()
def borrar_peli(id):
    conn = ConeccionDB()

    sql = f"""
            DELETE FROM Peliculas
            WHERE ID = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()

def guardar_usuario(usuario):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Usuarios (Nombre,Apellido)
            VALUES('{usuario.nombre}','{usuario.apellido}');
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()
def editar_usuario(usuario, id):
    conn = ConeccionDB()

    sql = f"""
            UPDATE Usuarios
            SET Nombre = '{usuario.nombre}', Apellido = '{usuario.apellido}'
            WHERE ID = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()
def borrar_usuario(id):
    conn = ConeccionDB()

    sql = f"""
            DELETE FROM Usuarios
            WHERE ID = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()

def guardar_puntuacion(puntuacion):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Puntuaciones (Puntuacion,Observaciones, Pelicula, Usuario)
            VALUES('{puntuacion.puntuacion}','{puntuacion.observaciones}','{puntuacion.pelicula}','{puntuacion.usuario}');
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()
def editar_puntuacion(puntuacion, id):
    conn = ConeccionDB()
    #print(puntuacion)
    sql = f"""
            UPDATE Puntuaciones
            SET Puntuacion = '{puntuacion.puntuacion}', Observaciones = '{puntuacion.observaciones}', Pelicula = '{puntuacion.pelicula}', Usuario = '{puntuacion.usuario}'
            WHERE ID = {id};
            """
    #print(sql)
    conn.cursor.execute(sql)
    conn.cerrar_con()
def borrar_puntuacion(id):
    conn = ConeccionDB()

    sql = f"""
            DELETE FROM Puntuaciones
            WHERE ID = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()