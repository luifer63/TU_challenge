import pytest
import login as login

def test_login():
    driver = login.setup()
    login.iniciar_sesion("doomie@gmail.com","doomie_pass", driver)
    login.cerrar_sesion(driver)
    login.quit(driver)
