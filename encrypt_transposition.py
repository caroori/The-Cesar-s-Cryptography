#Encriptador de Transposición
#Este encriptador organiza las letras del mensaje según una clave ingresada por el usuario. 
#Las letras del mensaje se reorganizan en una cuatrícula según la clave proporcionada

# Definir el alfabeto
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Función para encriptar un mensaje usando cifrado de transposición
def encriptar_transposicion(mensaje, clave):
  """
  Encripta un mensaje usando un cifrado de transposición.

  Args:
    mensaje: El mensaje a encriptar.
    clave: La clave para la transposición.

  Returns:
    El mensaje encriptado.
  """

  # Determinar el número de filas en la cuadrícula de transposición
  filas = len(mensaje) // clave
  if len(mensaje) % clave != 0:
    filas += 1

  # Crear la cuadrícula de transposición
  cuadricula = [[' ' for _ in range(clave)] for _ in range(filas)]

  # Rellenar la cuadrícula con el mensaje
  indice = 0
  for i in range(filas):
    for j in range(clave):
      if indice < len(mensaje):
        cuadricula[i][j] = mensaje[indice]
        indice += 1

  # Leer la cuadrícula columna por columna para obtener el mensaje encriptado
  mensaje_encriptado = ""
  for j in range(clave):
    for i in range(filas):
      mensaje_encriptado += cuadricula[i][j]

  return mensaje_encriptado

# Función para desencriptar un mensaje usando cifrado de transposición
def desencriptar_transposicion(mensaje, clave):
  """
  Desencripta un mensaje usando un cifrado de transposición.

  Args:
    mensaje: El mensaje a desencriptar.
    clave: La clave para la transposición.

  Returns:
    El mensaje desencriptado.
  """

  # Determinar el número de filas en la cuadrícula de transposición
  filas = len(mensaje) // clave
  if len(mensaje) % clave != 0:
    filas += 1

  # Crear la cuadrícula de transposición
  cuadricula = [[' ' for _ in range(clave)] for _ in range(filas)]

  # Rellenar la cuadrícula con el mensaje de manera transpuesta
  indice = 0
  for j in range(clave):
    for i in range(filas):
      if indice < len(mensaje):
        cuadricula[i][j] = mensaje[indice]
        indice += 1

  # Leer la cuadrícula fila por fila para obtener el mensaje desencriptado
  mensaje_desencriptado = ""
  for i in range(filas):
    for j in range(clave):
      mensaje_desencriptado += cuadricula[i][j]

  return mensaje_desencriptado

# Opciones del programa
opciones = {
  "encriptar": encriptar_transposicion,
  "desencriptar": desencriptar_transposicion
}

# Obtener la opción deseada por el usuario
opcion = input("¿Qué desea hacer? (encriptar/desencriptar): ")

# Si la opción es válida
if opcion in opciones:
  # Obtener el mensaje del usuario
  mensaje = input("Ingrese el mensaje: ")

  # Obtener la clave del usuario
  clave = int(input("Ingrese la clave: "))

  # Aplicar la opción deseada
  resultado_mensaje = opciones[opcion](mensaje, clave)

  # Imprimir el resultado
  print("Resultado:", resultado_mensaje)

# Si la opción no es válida
else:
  print("Opción inválida.")
