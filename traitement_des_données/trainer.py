from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

temperature = np.array([25, 28, 24, 20, 22])
humidite = np.array([60, 65, 70, 75, 80])
vitesse_vent = np.array([10, 15, 12, 8, 10])

previsions = np.array([0.1, 0.2, 0.0, 0.3, 0.1])


donnees_entree = np.column_stack((temperature, humidite, vitesse_vent))

X_train, X_test, y_train, y_test = train_test_split(donnees_entree, previsions, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, predictions))
print(f"Erreur quadratique moyenne : {rmse}")

nouvelles_donnees = np.array([[26, 68, 14]])
nouvelle_prevision = model.predict(nouvelles_donnees)
print(f"Prévision pour de nouvelles données : {nouvelle_prevision[0]}")
