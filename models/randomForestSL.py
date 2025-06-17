from sklearn.ensemble import RandomForestClassifier
import joblib

# Datos de entrenamiento (features: color, forma, tamaño)
X_train = [[120, 1, 50], [30, 0, 20], ...]  # Ejemplo: [Hue, Shape (0=circle, 1=square), Area]
y_train = [0, 1, ...]  # 0=Plástico, 1=Metal, etc.

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, "clasificador.joblib")

# Cargar y predecir
model = joblib.load("clasificador.joblib")
prediction = model.predict([[130, 1, 60]])  # Ejemplo: Nuevo objeto
print("Clase predicha:", prediction)