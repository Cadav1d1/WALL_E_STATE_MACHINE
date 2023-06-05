import tkinter as tk
from tkinter import messagebox
from Robot import Robot
from PIL import Image, ImageTk

class RobotUI(tk.Tk):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        
        image_logo = Image.open("logo.png")
        image_logo = image_logo.resize((600, 200))
        photo_logo = ImageTk.PhotoImage(image_logo)

        # Mostrar la imagen del logo en un widget Label
        self.label_logo = tk.Label(self, image=photo_logo)
        self.label_logo.image = photo_logo  # Guardar una referencia para evitar que la imagen sea eliminada por el recolector de basura
        self.label_logo.pack()
        
        image = Image.open("Wally.jpg.png")
        self.photo = ImageTk.PhotoImage(image)

        self.label_imagen = tk.Label(self, image=self.photo)
        self.label_imagen.pack()

        self.title("WALL*E")
        self.geometry("5000x5000")

        # Variables de estado y basura
        self.label_estado = tk.Label(self, text="Estado actual: {}".format(self.robot.estado_actual))
        self.label_estado.pack()

        self.label_basura_reciclable = tk.Label(self, text="Basura reciclable: {}".format(self.robot.basura_reciclable))
        self.label_basura_reciclable.pack()

    

        # Botones de acciones
        self.button_encender = tk.Button(self, text="Encender Robot", command=self.encender_robot)
        self.button_encender.pack()

        #self.button_apagar = tk.Button(self, text="Apagar Robot", command=self.apagar_robot)
        #self.button_apagar.pack()

        
        # Botón y función para seguir el camino
        self.button_seguir_camino = tk.Button(self, text="Navegando terreno", command=self.seguir_camino)
        self.button_seguir_camino.pack() 

        self.button_recolectar_objeto = tk.Button(self, text="Recolectar Objeto", command=self.recolectar_objeto)
        self.button_recolectar_objeto.pack()

        self.button_botar_reciclable = tk.Button(self, text="Botar Basura Reciclable", command=self.botar_reciclable)
        self.button_botar_reciclable.pack()

        """self.button_botar_no_reciclable = tk.Button(self, text="Botar Basura No Reciclable", command=self.botar_no_reciclable)
        self.button_botar_no_reciclable.pack()"""

        self.button_soltar_objetos = tk.Button(self, text="Soltar Objetos", command=self.soltar_objetos)
        self.button_soltar_objetos.pack()

        self.button_parado_emergencia = tk.Button(self, text="Parado de Emergencia", command=self.parado_emergencia)
        self.button_parado_emergencia.pack()

        self.button_continuar = tk.Button(self, text="Continuar", command=self.continuar)
        self.button_continuar.pack()
        
        self.button_apagar = tk.Button(self, text="Apagar Robot", command=self.apagar_robot)
        self.button_apagar.pack()

    def encender_robot(self):
        mensaje = self.robot.encender()
        self.actualizar_estado(mensaje)

    def apagar_robot(self):
        mensaje = self.robot.apagar()
        self.actualizar_estado(mensaje)

    def recolectar_objeto(self):
        mensaje = self.robot.recolectar_objeto()
        self.actualizar_estado(mensaje)

    def botar_reciclable(self):
        mensaje = self.robot.botar_reciclable()
        self.actualizar_estado(mensaje)

    """def botar_no_reciclable(self):
        mensaje = self.robot.botar_no_reciclable()
        self.actualizar_estado(mensaje)"""

    def soltar_objetos(self):
        mensaje = self.robot.soltar_objetos()
        self.actualizar_estado(mensaje)

    def parado_emergencia(self):
        mensaje = self.robot.parado_de_emergencia()
        self.actualizar_estado(mensaje)

    def continuar(self):
        mensaje = self.robot.continuar()
        self.actualizar_estado(mensaje)

    def seguir_camino(self):
        mensaje = self.robot.seguir_camino()
        self.actualizar_estado(mensaje)

    def actualizar_estado(self, mensaje):
        self.label_estado.config(text="Estado actual: {}".format(self.robot.estado_actual))
        self.label_basura_reciclable.config(text="Basura reciclable: {}".format(self.robot.basura_reciclable))
        #self.label_basura_no_reciclable.config(text="Basura no reciclable: {}".format(self.robot.basura_no_reciclable))
        messagebox.showinfo("Mensaje", mensaje)
