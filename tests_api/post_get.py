import requests

print("Iniciando prueba de API: Crear Usuario...")

url = "https://jsonplaceholder.typicode.com/users"

datos_usuario = {
    "name": "Lukucchi",
    "Username": "qa_automation"

}

respuesta = requests.post(url, json=datos_usuario)

# 4. REVISAR LA RESPUESTA
# Le pedimos a 'respuesta' su propiedad '.status_code' (código de estado)
if respuesta.status_code == 201:
    print("¡TC-01 API Exitoso! El usuario fue creado en el servidor.")
    print(respuesta.json())
else:
    print("❌ Algo falló, el servidor no devolvió el código 201.")


# ==========================================================
# TC-02: LEER USUARIO EXISTENTE (GET)
# ==========================================================
print("\nIniciando prueba de API: Leer Usuario ID 1...")

url_leer = "https://jsonplaceholder.typicode.com/users/1"

respuesta_get = requests.get(url_leer)

if respuesta_get.status_code == 200:
    print("¡TC-02 API Exitoso! El usuario existe y se leyó correctamente.")
    print("datos recibidos")
    print(respuesta_get.json())
else:
    print(
        f"❌ Falló el TC-02. El servidor respondió con otro código: {respuesta_get.status_code}")
