from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Triquiapp(App):

    turno = "X"

    def jugar(self, boton):
        boton.text = self.turno
        if self.turno == "X":
            self.turno = "O"
        else:
            self.turno = "X"

    def build(self):
        tablero = BoxLayout(orientation="horizontal")
        tamaño_tablero = 10
        for columna in range(tamaño_tablero):
            columna = BoxLayout(orientation="vertical")
            tablero.add_widget(columna)
            for boton in range(tamaño_tablero):
                boton = Button()
                boton.bind(on_press=self.jugar)
                columna.add_widget(boton)

        return tablero


if __name__ == "__main__":
    Triquiapp().run()
