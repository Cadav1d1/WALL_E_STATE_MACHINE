from transitions import Machine


class Robot:
    def __init__(self):
        self.estado_actual = "Robot Apagado"
        self.basura_reciclable = 0

        states = [
            'Robot Apagado',
            'Robot Encendido-Posicion Home',
            'El robot exploro el terreno y encontro un objeto',
            'Objeto recolectado correctamente',
            'Objeto desechado correctamente',
            'Objetos soltados correctamente',
            'Parado de Emergencia'
        ]

        transitions = [
            {'trigger': 'encender', 'source': 'Robot Apagado', 'dest': 'Robot Encendido-Posicion Home'},
            {'trigger': 'seguir_camino', 'source': [
                'Robot Encendido-Posicion Home',
                'Objeto recolectado correctamente',
                'El robot exploro el terreno y encontro un objeto',
                'Objeto desechado correctamente',
                'Objetos soltados correctamente'], 'dest': 'El robot exploro el terreno y encontro un objeto'},
            {'trigger': 'recolectar_objeto', 'source': [
                'Robot Encendido-Posicion Home',
                'El robot exploro el terreno y encontro un objeto'], 'dest': 'Objeto recolectado correctamente'},
            {'trigger': 'apagar', 'source': [
                'Robot Encendido-Posicion Home',
                'El robot exploro el terreno y encontro un objeto',
                'Objeto recolectado correctamente',
                'Objeto desechado correctamente',
                'Objetos soltados correctamente'], 'dest': 'Robot Apagado'},
            {'trigger': 'botar_reciclable', 'source': [
                'Robot Encendido-Posicion Home',
                'El robot exploro el terreno y encontro un objeto',
                'Objeto recolectado correctamente',
                'Objeto desechado correctamente'], 'dest': 'Objeto desechado correctamente'},
            {'trigger': 'soltar_objetos', 'source': [
                'Robot Encendido-Posicion Home',
                'El robot exploro el terreno y encontro un objeto',
                'Objeto recolectado correctamente',
                'Objeto desechado correctamente'], 'dest': 'Objetos soltados correctamente'},
            {'trigger': 'parado_de_emergencia', 'source': [
                'Robot Encendido-Posicion Home',
                'El robot exploro el terreno y encontro un objeto',
                'Objeto recolectado correctamente',
                'Objeto desechado correctamente',
                'Objetos soltados correctamente'], 'dest': 'Parado de Emergencia'},
            {'trigger': 'continuar', 'source': 'Parado de Emergencia', 'dest': 'Robot Encendido-Posicion Home'}
        ]

        self.machine = Machine(model=self, states=states, transitions=transitions, initial='Robot Apagado')

    def encender(self):
        if self.estado_actual == "Robot Apagado":
            self.estado_actual = "Robot Encendido-Posicion Home"
            return "El robot se ha encendido"
        else:
            return "El robot ya está encendido"

    def seguir_camino(self):
        if self.estado_actual == "Robot Apagado":
            return "El robot está apagado. Enciéndelo para navegar por el camino"
        elif self.estado_actual == "Robot Encendido-Posicion Home" or self.estado_actual == "Objeto recolectado correctamente" or self.estado_actual == "El robot exploro el terreno y encontro un objeto" or self.estado_actual == "Objeto desechado correctamente" or self.estado_actual == "Objetos soltados correctamente":
            self.estado_actual = "El robot exploro el terreno y encontro un objeto"
            return "Navegando por el terreno"
        elif self.estado_actual == "El robot exploro el terreno y encontro un objeto":
            return "Ya se exploró el terreno y se encontró un objeto"

    def recolectar_objeto(self):
        if self.estado_actual == "Robot Encendido-Posicion Home":
            return "Estás en Home. Selecciona la opción de navegar por el terreno para encontrar objetos reciclables"
        elif self.estado_actual == "El robot exploro el terreno y encontro un objeto":
            self.basura_reciclable += 1
            self.estado_actual = "Objeto recolectado correctamente"
            return "Recolectando objetos"
        elif self.estado_actual == "Robot Apagado":
            return "El robot está apagado. Enciéndelo para recolectar objetos"
        else:
            return "Ya no hay más objetos que recoger en esta zona"

    def apagar(self):
        if self.estado_actual == "Robot Encendido-Posicion Home" or self.estado_actual == "El robot exploro el terreno y encontro un objeto" or self.estado_actual == "Objeto recolectado correctamente" or self.estado_actual == "Objeto desechado correctamente" or self.estado_actual == "Objetos soltados correctamente":
            self.estado_actual = "Robot Apagado"
            return "El robot se ha apagado"
        elif self.estado_actual == "Robot Apagado":
            return "El robot ya está apagado"

    def botar_reciclable(self):
        if self.estado_actual == "Robot Encendido-Posicion Home" or self.estado_actual == "El robot exploro el terreno y encontro un objeto" or self.estado_actual == "Objeto recolectado correctamente" or self.estado_actual == "Objeto desechado correctamente":
            if self.basura_reciclable > 0:
                self.basura_reciclable -= 1
                self.estado_actual = "Objeto desechado correctamente"
                return "Objeto reciclable botado correctamente"
            elif self.estado_actual == "Robot Apagado":
                return "El robot debe estar encendido para desechar reciclaje"
            else:
                return "No hay basura reciclable para botar"

    def soltar_objetos(self):
        if self.estado_actual == "Robot Apagado":
            return "El robot debe estar encendido para soltar objetos"
        elif self.estado_actual == "Robot Encendido-Posicion Home" or self.estado_actual == "El robot exploro el terreno y encontro un objeto" or self.estado_actual == "Objeto recolectado correctamente" or self.estado_actual == "Objeto desechado correctamente":
            basura_reciclable = self.basura_reciclable
            if basura_reciclable > 0:
                self.basura_reciclable = 0
                self.estado_actual = "Objetos soltados correctamente"
            return "Objetos soltados correctamente. Total objetos soltados: {}".format(basura_reciclable)

    def parado_de_emergencia(self):
        if self.estado_actual == "Robot Apagado":
            return "El robot no está encendido, por lo tanto no se puede hacer el parado de emergencia ya que el robot ya está inmovil"
        elif self.estado_actual == "Robot Encendido-Posicion Home" or self.estado_actual == "El robot exploro el terreno y encontro un objeto" or self.estado_actual == "Objeto recolectado correctamente" or self.estado_actual == "Objeto desechado correctamente" or self.estado_actual == "Objetos soltados correctamente":
            self.estado_actual = "Parado de Emergencia"
            return "Parado de emergencia. Robot apagado"
        elif self.estado_actual == "Parado de Emergencia":
            return "El robot ya está en modo de emergencia"

    def continuar(self):
        if self.estado_actual == "Parado de Emergencia":
            self.estado_actual = "Robot Encendido-Posicion Home"
            return "Continuando operaciones"
        else:
            return "El robot no está en Parado de Emergencia, por lo tanto nunca se interrumpieron las acciones del robot"
