import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def proyecto_flujo_compra():
    print("Iniciando navegador...")
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        # Abrir la tienda de pruebas
        url = "https://www.saucedemo.com/"
        print(f"Abriendo: {url}")
        driver.get(url)
        time.sleep(2)

        # ==========================================================
        # TC-01: LOGIN EXITOSO
        # ==========================================================
        print("Ejecutando TC-01: Login...")

        campo_usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        )
        campo_usuario.send_keys("standard_user")

        campo_usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        campo_usuario.send_keys("secret_sauce")

        boton_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        boton_login.click()
        time.sleep(2)
        # Espera para ver si logueó con éxito

        # Validar si entramos a la página de inventario
        if "inventory.html" in driver.current_url:
            print("¡TC-01 Completado con éxito!")
        else:
            print("Falló el inicio de sesión.")
            return  # Detiene la ejecución si el login falla

        # ==========================================================
        # TC-02: AGREGAR PRODUCTO AL CARRITO
        # ==========================================================
        print("Ejecutando TC-02: Agregar producto...")

        boton_add_to_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        boton_add_to_cart.click()
        time.sleep(2)

        # ==========================================================
        # TC-03: IR AL CARRITO
        # ==========================================================
        print("Ejecutando TC-03: Ir al carrito...")

        boton_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        )
        boton_cart.click()
        time.sleep(2)

        # ==========================================================
        # TC-04: FORMULARIO DE DESPACHO (CHECKOUT)
        # ==========================================================
        print("Ejecutando TC-04: Formulario de despacho...")

        boton_checkout = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        boton_checkout.click()
        time.sleep(2)

        campo_checkout = driver.find_element(By.ID, "first-name")
        campo_checkout.send_keys("Pepe")
        campo_checkout = driver.find_element(By.ID, "last-name")
        campo_checkout.send_keys("Rojas")
        campo_checkout = driver.find_element(By.ID, "postal-code")
        campo_checkout.send_keys("79100")

        boton_checkout = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        boton_checkout.click()
        time.sleep(2)

        # ==========================================================
        # TC-05: FINALIZAR COMPRA
        # ==========================================================
        print("Ejecutando TC-05: Finalizar compra...")

        boton_finish = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        boton_finish.click()
        time.sleep(2)

        # VALIDACIÓN FINAL
        if "checkout-complete.html" in driver.current_url:
            print(
                "¡PROYECTO TERMINADO! El flujo de compra completo fue automatizado con éxito.")
        else:
            print("La compra no se completó correctamente.")

    except Exception as e:
        print(f"Ocurrió un error en la automatización: {e}")

    finally:
        print("Cerrando navegador...")
        driver.quit()


if __name__ == "__main__":
    proyecto_flujo_compra()
