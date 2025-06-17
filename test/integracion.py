# Pseudocódigo de integración
def main():
    # 1. Iniciar GUI
    gui = RobotGUI()

    # 2. Capturar imagen con YOLO
    model = YOLO("yolov8n.pt")
    results = model(frame)

    # 3. Clasificar objeto
    object_class = results[0].names[int(results[0].boxes.cls[0])]

    # 4. Calcular ruta con A*
    path = nx.astar_path(G, start_pos, end_pos)

    # 5. Mover brazo robótico (vía Arduino)
    arduino.write(f"MOVE {path}\n".encode())

    # 6. Mostrar resultados en GUI
    gui.update_status(f"Objeto {object_class} movido a {path[-1]}")