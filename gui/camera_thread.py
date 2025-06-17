from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtGui import QImage
import cv2
from ultralytics import YOLO

class CameraThread(QThread):
    change_pixmap = pyqtSignal(QImage)  # Señal para enviar el frame procesado
    detection_data = pyqtSignal(list)    # Señal para enviar datos de detección (opcional)

    def __init__(self, model_path="models/yolov8n.pt"):
        super().__init__()
        self.model = YOLO(model_path)
        self.running = True

    def run(self):
        cap = cv2.VideoCapture(0)  # Cámara predeterminada
        while self.running:
            ret, frame = cap.read()
            if ret:
                # Detección con YOLO
                results = self.model(frame, verbose=False)
                annotated_frame = results[0].plot()  # Frame con detecciones dibujadas

                # Convertir OpenCV (BGR) a QImage (RGB)
                rgb_image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(
                    rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888
                )
                self.change_pixmap.emit(qt_image)

                # Opcional: Emitir datos de detección (coordenadas, clases)
                boxes = results[0].boxes.data.tolist()
                self.detection_data.emit(boxes) if boxes else None

        cap.release()

    def stop(self):
        self.running = False
        self.wait()