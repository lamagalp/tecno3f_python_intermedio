import tkinter as tk
from cliente.vista import Frame, barrita_menu

def main():
    ventana = tk.Tk()
    ventana.title('Listado Peliculas')
    ventana.iconbitmap('Tecno3F/Intermedio/material de clase/CRUD2.1/CRUD2.1/img/videocamara.ico')
    ventana.resizable(0,0)

    app = Frame(root = ventana)
    barrita_menu(ventana, app)
    

    ventana.mainloop()

if __name__ == '__main__':
    main()