import re

texto = (" En el año 2025, 20 médicos cuidan juntos. ¡Hola! ¿Te gusta la medicina? "
"El cielo saludable, las estrellas (★) brillan. 16 niños sanan, 15.50 horas de consulta. "
"Lista: termómetro, bata, receta. El costo es $75.20. ¿Sabías que el código #3344 es especial? "
"La vida es salud, @todos participan. El tiempo pasa, 17 días de atención. ¡Cuida! "
"El número especial es 1010. ¿Qué harías con 48.90 pesos? La respuesta está en la lista: curar, ayudar, escuchar. "
"¡Cuida tu salud! 100 palabras, 17 enteros, 3 decimales, 2 listas. ")

# Palabras (solo letras, incluyendo tildes y ñ)
patron_palabras = r"[A-Za-zÁÉÍÓÚáéíóúÑñ]+"
palabras = re.findall(patron_palabras, texto)

# Decimales (números con punto)
patron_decimal = r"\d+\.\d+"
decimales = re.findall(patron_decimal, texto)

# Enteros (cualquier número, incluidas las partes enteras y decimales)
patron_entero = r"\d+"
enteros = re.findall(patron_entero, texto)

# Listas (ejemplo: "Lista: ...")
patron_lista = r"[Ll]ista:\s*([^\.!?\n]+)"
listas = re.findall(patron_lista, texto)

print("Palabras:", len(palabras))
print("Enteros:", len(enteros))   # Aquí deben salir 17
print("Decimales:", len(decimales))
print("Listas:", len(listas))
