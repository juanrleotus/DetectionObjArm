from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage
import cv2
from ultralytics import YOLO

class CameraThread(QThread):
    change_pixmap = pyqtSignal(QImage)  # Señal para enviar el frame procesado
    detection_data = pyqtSignal(list)    # Señal para enviar datos de detección

    def __init__(self, model_path="models/yolov8n.pt"):
        super().__init__()
        self.model = YOLO(model_path)
        self.running = True
        self.serial_connection = None  # Inicializar conexión serial

    def run(self):
        cap = cv2.VideoCapture(0)
        while self.running:
            ret, frame = cap.read()
            if ret:
                # Detección con YOLO
                results = self.model(frame, verbose=False)
                annotated_frame = results[0].plot()  # Frame con detecciones dibujadas

                # Filtrar solo envases (clase bottle = 39)
                for box in results[0].boxes:
                    if int(box.cls) == 39:  # Solo procesar botellas
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        height_px = y2 - y1
                        height_cm = self.pixels_to_cm(height_px)
                        
                        # Clasificar por tamaño
                        target_position = "sector_A" if height_cm >= 19 else "sector_B"
                        x_center = (x1 + x2) // 2
                        y_top = y1
                        
                        if self.serial_connection:
                            self.move_arm(x_center, y_top, target_position)

                # Convertir OpenCV (BGR) a QImage (RGB)
                rgb_image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                
                # Emitir la imagen procesada
                self.change_pixmap.emit(qt_image)

        cap.release()

    def move_arm(self, x_pixel, y_pixel, sector):
        """Convertir coordenadas de pantalla a ángulos de servo"""
        ancho_max_px = 640  # Resolución de tu cámara
        alto_max_px = 480
    
        angle_base = int((x_pixel / ancho_max_px) * 180)
        angle_hombro = int((y_pixel / alto_max_px) * 90)
    
        if self.serial_connection:
            command = f"BASE:{angle_base},HOMBRO:{angle_hombro},SECTOR:{sector}\n"
            self.serial_connection.write(command.encode())

    def pixels_to_cm(self, pixels):
        """Convertir píxeles a centímetros (ajusta el factor según tu configuración)"""
        return pixels * (19 / 100)  # Ejemplo: 100 píxeles = 19 cm

    def stop(self):
        self.running = False
        self.wait()
