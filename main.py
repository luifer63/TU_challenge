# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import login as login


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = login.setup()
    login.iniciar_sesion("doomie@gmail.com", "doomiepass", driver)
    login.cerrar_sesion(driver)
    login.quit(driver)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
