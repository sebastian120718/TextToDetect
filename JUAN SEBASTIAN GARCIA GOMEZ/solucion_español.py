import re

texto = (" En el año 2025, 20 médicos cuidan juntos. ¡Hola! ¿Te gusta la medicina? "
"El cielo saludable, las estrellas (★) brillan. 16 niños sanan, 15.50 horas de consulta. "
"Lista: termómetro, bata, receta. El costo es $75.20. ¿Sabías que el código #3344 es especial? "
"La vida es salud, @todos participan. El tiempo pasa, 17 días de atención. ¡Cuida! "
"El número especial es 1010. ¿Qué harías con 48.90 pesos? La respuesta está en la lista: curar, ayudar, escuchar. "
"¡Cuida tu salud! 100 palabras, 17 enteros, 3 decimales, 2 listas. ")


palabras = len(re.findall(r"\w+", texto, re.UNICODE)) + len(re.findall(r",", texto))


decimales = re.findall(r"\d+\.\d+", texto)


enteros = re.findall(r"\d+", texto)

# Listas
listas = re.findall(r"[Ll]ista:\s*([^\.!?\n]+)", texto)

print("Palabras:", palabras)       
print("Enteros:", len(enteros))   
print("Decimales:", len(decimales))
print("Listas:", len(listas))      
