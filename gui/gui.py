from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
import sys


class RobotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de Brazo Robótico")
        self.setGeometry(100, 100, 800, 600)

        # Botones
        self.btn_start = QPushButton("Iniciar Detección", self)
        self.btn_start.move(50, 50)
        self.btn_start.clicked.connect(self.start_detection)

        # Etiqueta para la cámara
        self.camera_label = QLabel(self)
        self.camera_label.setGeometry(200, 50, 600, 400)

    def start_detection(self):
        # Aquí iría el código de YOLO + OpenCV
        print("Detección iniciada")


app = QApplication(sys.argv)
window = RobotGUI()
window.show()
sys.exit(app.exec_())