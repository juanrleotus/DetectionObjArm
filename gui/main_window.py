from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from .camera_thread import CameraThread  # Importar el nuevo QThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Brazo Robótico con YOLO")
        self.setGeometry(100, 100, 800, 600)

        # Widgets
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Label para la cámara
        self.label_camera = QLabel()
        self.label_camera.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_camera)

        central_widget.setLayout(layout)

        # Inicializar hilo de la cámara
        self.camera_thread = CameraThread()
        self.camera_thread.change_pixmap.connect(self.update_image)
        self.camera_thread.start()

    def update_image(self, qt_image):
        """Actualiza el QLabel con el nuevo frame de la cámara"""
        self.label_camera.setPixmap(QPixmap.fromImage(qt_image).scaled(
            self.label_camera.width(),
            self.label_camera.height(),
            Qt.KeepAspectRatio
        ))

    def closeEvent(self, event):
        """Detener el hilo al cerrar la ventana"""
        self.camera_thread.stop()
        event.accept()