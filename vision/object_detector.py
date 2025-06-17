from ultralytics import YOLO
import cv2
import yaml

class ObjectDetector:
    def __init__(self, model_path='models/yolov8n.pt'):
        self.model = YOLO(model_path)
        
    def detect_objects(self, frame):
        results = self.model(frame)
        return results[0].boxes.data.tolist()  # [x1, y1, x2, y2, conf, class]