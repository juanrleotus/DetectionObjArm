import yaml
import sys
from vision.object_detector import ObjectDetector
from pathfinding.path_planner import PathPlanner
from gui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication

def main():
    # Cargar configuración
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    
    # Inicializar módulos
    detector = ObjectDetector(config['vision']['model_path'])
    planner = PathPlanner(config['pathfinding']['map_file'])
    
    # Iniciar GUI
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())