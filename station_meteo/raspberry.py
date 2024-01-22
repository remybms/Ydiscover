import time
import board
import busio
import adafruit_bme680
import RPi.GPIO as GPIO

GPIO_PIN = 18

# Configuration du capteur BME680
i2c = busio.I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# Configuration de la broche GPIO en mode d'entrée
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        # Lecture des données du capteur BME680
        temperature = bme680.temperature
        humidity = bme680.humidity
        pressure = bme680.pressure
        gas = bme680.gas

        # Lecture de l'état de la broche GPIO
        gpio_state = GPIO.input(GPIO_PIN)

        # Affichage des données
        print(f"Température: {temperature:.2f}°C")
        print(f"Humidité: {humidity:.2f}%")
        print(f"Pression: {pressure:.2f} hPa")
        print(f"Gaz: {gas} ohms")
        print(f"État GPIO: {gpio_state}")

        # Attente avant la prochaine lecture
        time.sleep(1)

except KeyboardInterrupt:
    # Gestion de l'interruption par l'utilisateur (Ctrl+C)
    print("Programme interrompu par l'utilisateur")

finally:
    # Nettoyage des ressources GPIO
    GPIO.cleanup()
