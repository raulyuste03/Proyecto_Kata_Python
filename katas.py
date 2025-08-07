# PROYECTO LÓGICA: Katas de Python
# Autor: Raúl Yuste.
# Descripción: Resolución de todas las katas planteadas en el proyecto.
# Cada función incluye explicación y ejemplos de uso.

from functools import reduce

#--------------------------
# KATA 1: Frecuencia de letras en una cadena
def frecuencia_letras(cadena):
    """
    Devuelve un diccionario con la frecuencia de cada letra (ignora espacios).
    """
    # Elimina espacios de la cadena
    cadena = cadena.replace(" ", "")
    frecuencias = {}
    for letra in cadena:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias
# Ejemplo:
# print(frecuencia_letras("hola mundo"))

# ---------------------------------------------
# KATA 2: Doblar valores de una lista con map
def doblar_lista(lista):
    """
    Devuelve una nueva lista con el doble de cada número.
    """
    return list(map(lambda x: x * 2, lista))
# Ejemplo:
# print(doblar_lista([1,2,3]))

# ---------------------------------------------
# KATA 3: Filtrar palabras que contienen una palabra objetivo
def palabras_con_objetivo(lista_palabras, objetivo):
    """
    Devuelve las palabras que contienen la palabra objetivo.
    """
    return [palabra for palabra in lista_palabras if objetivo in palabra]
# Ejemplo:
# print(palabras_con_objetivo(['gato', 'perro', 'gatito'], 'gat'))

# ---------------------------------------------
# KATA 4: Diferencia entre valores de dos listas usando map
def diferencia_listas(lista1, lista2):
    """
    Devuelve una lista con la diferencia entre los elementos de dos listas.
    """
    return list(map(lambda x, y: x - y, lista1, lista2))
# Ejemplo:
# print(diferencia_listas([5,6,7], [2,2,2]))

# ---------------------------------------------
# KATA 5: Media y aprobado/suspenso
def evaluar_media(lista, nota_aprobado=5):
    """
    Calcula la media y devuelve (media, 'aprobado'/'suspenso').
    """
    media = sum(lista) / len(lista)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)
# Ejemplo:
# print(evaluar_media([4,6,7]))

# ---------------------------------------------
# KATA 6: Factorial recursivo
def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
# Ejemplo:
# print(factorial(5))

# ---------------------------------------------
# KATA 7: Lista de tuplas a lista de strings con map
def tuplas_a_strings(lista_tuplas):
    """
    Convierte una lista de tuplas en una lista de strings.
    """
    return list(map(lambda t: ' '.join(map(str, t)), lista_tuplas))
# Ejemplo:
# print(tuplas_a_strings([(1,2),(3,4)]))

# ---------------------------------------------
# KATA 8: División con manejo de excepciones
def dividir_numeros():
    """
    Solicita dos números al usuario y los divide, manejando excepciones.
    """
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        resultado = a / b
    except ValueError:
        print("Error: Debes introducir un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"División exitosa: {resultado}")
# Ejemplo: Llamar dividir_numeros() para probarlo

# ---------------------------------------------
# KATA 9: Excluir mascotas prohibidas con filter
def mascotas_permitidas(lista_mascotas):
    """
    Devuelve una lista excluyendo mascotas prohibidas en España.
    """
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista_mascotas))
# Ejemplo:
# print(mascotas_permitidas(['Perro','Mapache','Gato']))

# ---------------------------------------------
# KATA 10: Excepción personalizada si lista vacía
class ListaVaciaError(Exception):
    pass

def promedio_lista(lista):
    """
    Calcula el promedio de una lista o lanza excepción si está vacía.
    """
    if not lista:
        raise ListaVaciaError("La lista está vacía.")
    return sum(lista) / len(lista)
# Ejemplo de uso:
# try:
#     print(promedio_lista([]))
# except ListaVaciaError as e:
#     print(e)

# ---------------------------------------------
# KATA 11: Solicita edad y valida
def solicitar_edad():
    """
    Solicita la edad y valida entrada numérica y rango.
    """
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Edad introducida: {edad}")

# ---------------------------------------------
# KATA 12: Longitud de cada palabra con map
def longitudes_palabras(frase):
    """
    Devuelve lista de longitudes de cada palabra en una frase.
    """
    return list(map(len, frase.split()))
# Ejemplo:
# print(longitudes_palabras("Hola mundo Python"))

# ---------------------------------------------
# KATA 13: Mayúsculas y minúsculas, sin repetir, con map
def mayus_minus_sin_repetir(conjunto):
    """
    Devuelve lista de tuplas con cada letra en mayúsculas y minúsculas, sin repeticiones.
    """
    conjunto = set(conjunto)
    return list(map(lambda c: (c.upper(), c.lower()), conjunto))
# Ejemplo:
# print(mayus_minus_sin_repetir('aabcC'))

# ---------------------------------------------
# KATA 14: Palabras que empiezan por una letra usando filter
def palabras_por_letra(lista_palabras, letra):
    """
    Devuelve palabras que empiezan por una letra específica.
    """
    return list(filter(lambda p: p.startswith(letra), lista_palabras))
# Ejemplo:
# print(palabras_por_letra(['casa','perro','coche'],'c'))

# ---------------------------------------------
# KATA 15: Lambda que suma 3 a cada número
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))
# Ejemplo:
# print(sumar_tres([1,2,3]))

# ---------------------------------------------
# KATA 16: Palabras más largas que n usando filter
def palabras_mas_largas(lista_palabras, n):
    """
    Devuelve palabras más largas que n caracteres.
    """
    return list(filter(lambda p: len(p) > n, lista_palabras))
# Ejemplo:
# print(palabras_mas_largas(['gato','elefante','sol'], 3))

# ---------------------------------------------
# KATA 17: Lista de dígitos a número usando reduce
from functools import reduce

def lista_a_numero(lista_digitos):
    """
    Convierte una lista de dígitos en el número correspondiente.
    Devuelve 0 si la lista está vacía.
    """
    return reduce(lambda acc, d: acc * 10 + d, lista_digitos, 0)

# ---------------------------------------------
# KATA 18: Extraer estudiantes con nota >= 90 con filter
def estudiantes_sobresalientes(lista_estudiantes):
    """
    Filtra estudiantes con calificación mayor o igual a 90.
    """
    return list(filter(lambda est: est['calificacion'] >= 90, lista_estudiantes))
# Ejemplo:
# print(estudiantes_sobresalientes([{'nombre':'Ana','edad':20,'calificacion':95},{'nombre':'Luis','edad':19,'calificacion':80}]))

# ---------------------------------------------
# KATA 19: Lambda para filtrar impares
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
# Ejemplo:
# print(filtrar_impares([1,2,3,4,5]))

# ---------------------------------------------
# KATA 20: Filter para valores int
def solo_enteros(lista):
    """
    Devuelve solo los valores int de una lista.
    """
    return list(filter(lambda x: isinstance(x, int), lista))
# Ejemplo:
# print(solo_enteros([1, 'a', 2, 'b', 3]))

# ---------------------------------------------
# KATA 21: Lambda para calcular el cubo
cubo = lambda n: n ** 3
# Ejemplo:
# print(cubo(4))

# ---------------------------------------------
# KATA 22: Producto total de lista numérica con reduce
def producto_total(lista):
    """
    Calcula el producto total de una lista de números.
    """
    return reduce(lambda x, y: x * y, lista)
# Ejemplo:
# print(producto_total([2,3,4]))

# ---------------------------------------------
# KATA 23: Concatenar palabras con reduce
def concatenar_palabras(lista_palabras):
    """
    Concatena una lista de palabras en un string.
    """
    return reduce(lambda a, b: a + b, lista_palabras)
# Ejemplo:
# print(concatenar_palabras(['hola','mundo']))

# ---------------------------------------------
# KATA 24: Diferencia total en una lista con reduce
from functools import reduce

def diferencia_total(lista):
    """
    Calcula la diferencia total de los valores de una lista.
    Si la lista está vacía, devuelve 0.
    """
    return reduce(lambda x, y: x - y, lista, 0)
# ---------------------------------------------
# KATA 25: Contar caracteres de una cadena
def contar_caracteres(cadena):
    """
    Devuelve el número de caracteres de una cadena.
    """
    return len(cadena)
# Ejemplo:
# print(contar_caracteres("Hola mundo"))

# ---------------------------------------------
# KATA 26: Lambda para el resto de la división
resto_division = lambda x, y: x % y
# Ejemplo:
# print(resto_division(10, 3))

# ---------------------------------------------
# KATA 27: Promedio de una lista de números
def promedio(lista):
    """
    Calcula el promedio de una lista.
    """
    return sum(lista) / len(lista)
# Ejemplo:
# print(promedio([4,6,8]))

# ---------------------------------------------
# KATA 28: Primer elemento duplicado en una lista
def primer_duplicado(lista):
    """
    Devuelve el primer elemento duplicado en la lista.
    """
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None
# Ejemplo:
# print(primer_duplicado([1,2,3,2,4]))

# ---------------------------------------------
# KATA 29: Enmascarar con # excepto los últimos 4 caracteres
def enmascarar_variable(var):
    """
    Convierte una variable a string y enmascara todos menos los últimos 4 caracteres con '#'.
    """
    s = str(var)
    return '#'*(len(s)-4) + s[-4:] if len(s) > 4 else s
# Ejemplo:
# print(enmascarar_variable('123456789'))

# ---------------------------------------------
# KATA 30: Anagramas
def son_anagramas(palabra1, palabra2):
    """
    Devuelve True si son anagramas.
    """
    return sorted(palabra1) == sorted(palabra2)
# Ejemplo:
# print(son_anagramas('amor', 'roma'))

# ---------------------------------------------
# KATA 31: Buscar nombre en lista, excepción si no está
def buscar_nombre():
    """
    Solicita lista de nombres y un nombre a buscar, lanza excepción si no está.
    """
    try:
        lista = input("Introduce nombres separados por coma: ").split(",")
        nombre = input("Introduce el nombre a buscar: ")
        if nombre not in lista:
            raise Exception("Nombre no encontrado.")
    except Exception as e:
        print(e)
    else:
        print("¡Nombre encontrado!")

# ---------------------------------------------
# KATA 32: Buscar puesto de un empleado
def buscar_puesto(nombre, lista_empleados):
    """
    Busca el puesto de un empleado en la lista.
    """
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre:
            return empleado["puesto"]
    return "Esta persona no trabaja aquí."
# Ejemplo:
# empleados = [{"nombre": "Juan", "puesto": "Jefe"}, {"nombre": "Ana", "puesto": "Analista"}]
# print(buscar_puesto("Ana", empleados))

# ---------------------------------------------
# KATA 33: Lambda suma de dos listas elemento a elemento
suma_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))
# Ejemplo:
# print(suma_listas([1,2],[3,4]))

# ---------------------------------------------
# KATA 34: Clase Árbol
class Arbol:
    """
    Clase para representar un árbol con tronco y ramas.
    """
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    def crecer_tronco(self):
        self.tronco += 1
    def nueva_rama(self):
        self.ramas.append(1)
    def crecer_ramas(self):
        self.ramas = [r+1 for r in self.ramas]
    def quitar_rama(self, pos):
        if 0 <= pos < len(self.ramas):
            self.ramas.pop(pos)
    def info_arbol(self):
        return {"tronco": self.tronco, "num_ramas": len(self.ramas), "long_ramas": self.ramas}
# Ejemplo de uso al final del archivo.

# ---------------------------------------------
# KATA 35: Clase UsuarioBanco
class UsuarioBanco:
    """
    Representa a un usuario bancario con saldo y cuenta corriente.
    """
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    def retirar_dinero(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            raise ValueError("Saldo insuficiente.")
    def transferir_dinero(self, otro_usuario, cantidad):
        """ 
        Transfiere cantidad desde self a otro_usuario.
        """
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            otro_usuario.saldo += cantidad
        else:
            raise ValueError("Saldo insuficiente en el usuario origen.")
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
# Ejemplo de uso al final del archivo.

# ---------------------------------------------
# KATA 36: Funciones de procesamiento de texto
def contar_palabras(texto):
    """
    Devuelve un diccionario con la frecuencia de cada palabra.
    """
    palabras = texto.split()
    freq = {}
    for palabra in palabras:
        freq[palabra] = freq.get(palabra, 0) + 1
    return freq

def reemplazar_palabras(texto, original, nueva):
    """
    Reemplaza palabra_original por palabra_nueva.
    """
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    """
    Elimina todas las apariciones de una palabra.
    """
    return " ".join([p for p in texto.split() if p != palabra])

def procesar_texto(texto, opcion, *args):
    """
    Procesa el texto según la opción indicada.
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        return "Opción no válida."
# Ejemplo:
# print(procesar_texto("hola hola adiós", "contar"))
# print(procesar_texto("hola adiós mundo", "reemplazar", "hola", "hello"))
# print(procesar_texto("hola adiós mundo", "eliminar", "adiós"))

# ---------------------------------------------
# KATA 37: Día, tarde o noche según la hora
def momento_del_dia():
    """
    Solicita la hora y dice si es de día, tarde o noche.
    """
    try:
        hora = int(input("Introduce la hora (0-23): "))
        if hora < 0 or hora > 23:
            raise ValueError("Hora fuera de rango.")
        if 6 <= hora < 12:
            print("Es de día.")
        elif 12 <= hora < 20:
            print("Es tarde.")
        else:
            print("Es de noche.")
    except ValueError as e:
        print(f"Error: {e}")

# ---------------------------------------------
# KATA 38: Calificación en texto según la nota
def calificacion_texto(nota):
    """
    Devuelve la calificación textual según la nota.
    """
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota fuera de rango"
# Ejemplo:
# print(calificacion_texto(85))

# ---------------------------------------------
# KATA 39: Área de figura según parámetros
def area_figura(figura, datos):
    """
    Calcula el área según la figura y los datos proporcionados.
    """
    if figura == "rectangulo":
        return datos[0] * datos[1]
    elif figura == "circulo":
        return 3.1416 * datos[0] ** 2
    elif figura == "triangulo":
        return (datos[0] * datos[1]) / 2
    else:
        return "Figura no soportada"
# Ejemplo:
# print(area_figura("rectangulo", (4, 5)))

# ---------------------------------------------
# KATA 40 y 41: Descuento en tienda online con condicionales
def compra_con_descuento():
    """
    Calcula y devuelve el precio final aplicando un posible descuento.
    """
    try:
        precio = float(input("Introduce el precio original (€): "))
        tiene_cupon = input("¿Tienes cupón de descuento? (si/no): ").strip().lower()
        descuento = 0.0
        if tiene_cupon == "si":
            valor = float(input("Valor del cupón (€): "))
            if valor > 0:
                descuento = valor
            else:
                print("El valor del cupón no es válido, se ignora.")
        final = max(precio - descuento, 0)
        print(f"Precio final: {final:.2f} €")
    except ValueError:
        print("Error: Debes introducir valores numéricos válidos.")
# --- Ejemplo de uso de clases  ---
if __name__ == "__main__":
    # Árbol
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    print(arbol.info_arbol())
    
    # Usuarios banco
    alicia = UsuarioBanco("Raúl", 100, True)
    bob = UsuarioBanco("Yuste", 50, True)
    bob.agregar_dinero(20)
    alicia.transferir_dinero(bob, 80)
    alicia.retirar_dinero(50)
    print(alicia.saldo, bob.saldo)
