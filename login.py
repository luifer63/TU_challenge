import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import localizadores as loc


def setup():
    options = uc.ChromeOptions()
    options.user_data_dir = "c:\\temp\\profile"
    options.add_argument('--user-data-dir=c:\\temp\\profile2')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    driver = uc.Chrome(options=options)
    driver.implicitly_wait(60)
    driver.get("http://www.gmail.com")
    driver.maximize_window()
    return driver


def iniciar_sesion(email, password, driver):
    try:
        driver.find_element(By.XPATH,loc.NUEVA_CUENTA).click()
    except:
        print("No se encuentra mensaje")
    else:
        print("Se encuentra mensaje")
    finally:
        driver.find_element(By.XPATH,loc.INGRESE_EMAIL).send_keys(email)

    driver.find_element(By.XPATH,loc.BOTON_SIGUIENTE).click()
    wait = WebDriverWait(driver, 10)
    elementPass = wait.until(EC.element_to_be_clickable((By.XPATH,loc.INGRESE_PASSW)))
    elementPass.send_keys(password)
    driver.find_element(By.XPATH,loc.BOTON_SIGUIENTE).click()
    wait = WebDriverWait(driver, 30)
    logo = wait.until(EC.element_to_be_clickable((By.XPATH, loc.LOGO_PRINCIPAL)))



def cerrar_sesion(driver):
    driver.find_element(By.XPATH,loc.MENU_CIERRE).click()
    action = ActionChains(driver)
    action.pause(10).send_keys().send_keys(Keys.TAB * 3).send_keys(Keys.RETURN).pause(10).perform()


def quit(driver):
    driver.quit()






