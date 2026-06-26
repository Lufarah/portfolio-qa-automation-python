# 🚀 Automatización de Flujo de Compra End-to-End (Saucedemo)

Este proyecto contiene un script de automatización de pruebas funcionales para la plataforma de e-commerce de práctica **Saucedemo**, desarrollado en **Python** utilizando **Selenium WebDriver**.

El objetivo del proyecto es simular el comportamiento real de un usuario completando un flujo de compra completo, desde el inicio de sesión hasta la pantalla de confirmación.

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.14+
* **Herramienta de Automatización:** Selenium WebDriver
* **Entorno:** Aislado mediante Entorno Virtual (`venv`) de Python

## 📝 Casos de Prueba Automatizados
El script ejecuta de manera secuencial los siguientes casos de prueba (Test Cases):
1. **TC-01 (Login Exitoso):** Validación de ingreso con credenciales válidas (`standard_user`).
2. **TC-02 (Agregar al Carrito):** Interacción y selección del producto "Sauce Labs Backpack".
3. **TC-03 (Navegación al Carrito):** Verificación de ingreso al carrito de compras.
4. **TC-04 (Formulario de Despacho):** Llenado dinámico de los campos de datos del cliente (Nombre, Apellido, Código Postal).
5. **TC-05 (Finalizar Compra):** Confirmación de la orden y validación del mensaje de éxito en pantalla.

## 💡 Desafíos Superados & Aprendizajes
* **Manejo de Asincronismo:** Inicialmente me enfrenté a errores de sincronización (`NoSuchElementException`) debido a la velocidad de ejecución de Python vs la carga del navegador. Lo solucioné implementando **Esperas Explícitas (`WebDriverWait`)** con condiciones esperadas (`EC.element_to_be_clickable`), evitando el uso de pausas fijas ineficientes.
* **Aislamiento de Dependencias:** Configuración y uso de entornos virtuales (`venv`) en Windows para asegurar la portabilidad del código.

## ⚙️ Cómo Ejecutar el Proyecto

1. Clona este repositorio.
2. Abre la terminal en la raíz del proyecto y crea el entorno virtual:
   ```bash
   python -m venv .venv
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
5. Ejecuta la prueba:
   ```bash
   python tests_saucedemo/test_login_success.py


## 🌐 Módulo 2: Automatización de APIs (Backend)

Para complementar mis habilidades de automatización en el Frontend, agregué este módulo enfocado en pruebas de servicios y Backend.

### 🛠️ Tecnologías Utilizadas
* **Librería:** Requests (Python)
* **API de Pruebas:** JSONPlaceholder REST API

### 🚀 Casos de Prueba Automatizados
1. **TC-01: Crear Usuario (POST)**
   * **Objetivo:** Validar la creación de un registro enviando un payload JSON.
   * **Validación:** Status Code `201 Created` y retorno de ID por el servidor.
2. **TC-02: Leer Usuario (GET)**
   * **Objetivo:** Validar la obtención de datos de un usuario existente (ID 1).
   * **Validación:** Status Code `200 OK` y consistencia en la respuesta.