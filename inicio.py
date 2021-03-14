from PyQt5.QtWidgets import *
from aplicacion import Simplex
from aplicacion2 import Pert
from vista.ui_programaPert import Ui_MainWindow
import locale
from PyQt5.QtGui import QIcon, QPixmap
import sys
import os

class Main(QDialog):


    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Investigación de Operaciones')

        #Resolver ruta
        def resolver_ruta(ruta_relativa):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, ruta_relativa)
            return os.path.join(os.path.abspath('.'), ruta_relativa)
            
        self.nombre_icono = resolver_ruta("./icono_1.png")
        self.nombre_icono_app = resolver_ruta("./icono_1.png")
        self.setWindowIcon(QIcon(self.nombre_icono))
        self.ui.label_10.setPixmap(QPixmap(self.nombre_icono_app))


        # Eventos
        self.ui.actionSIMPLEX.triggered.connect(self.mostrarSimplex)
        self.ui.actionPERT.triggered.connect(self.mostrarPert)
        #cambiamos las fechas a español
        locale.setlocale(locale.LC_ALL, "es_MX.UTF-8")



    #Funcion para mostrar la interfaz de Simplex
    def mostrarSimplex(self):
        self.ui.frame_2.setVisible(False)
        self.ui.widgetP.setVisible(False)
        self.ui.widgetS.setVisible(True)
        self.simplex = Simplex(self.ui)


    #Funcion para mostrar la interfaz de PERT
    def mostrarPert(self):
        self.ui.frame_2.setVisible(False)
        self.ui.widgetS.setVisible(False)
        self.ui.widgetP.setVisible(True)
        self.pert = Pert(self.ui, self.nombre_icono)
        


     
        




if __name__ == "__main__":
    app =  QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    GUI = Main()
    GUI.show()
    sys.exit(app.exec_())