import re

texto = ("Ciao! Nel 2025, 19 medici curano insieme. Lista: termometro, camice, ricetta. "
"Il prezzo è €70,80. Le stelle (★) brillano sopra la clinica. 13 gatti curano, 12 cani aiutano. "
"Il codice #7788 è speciale. 16 giorni di cura, 12 di riposo. @tutti curano. "
"Il numero magico è 1030. Cosa faresti con 45,90€? La risposta è nella lista: curare, aiutare, ascoltare. "
"Prenditi cura della tua salute! 100 parole, 16 interi, 3 decimali, 2 listas.")

patron_palabras = r"[\wÁÉÍÓÚáéíóúÑñÀ-ÿ#@€★]+"
palabras = len(re.findall(patron_palabras, texto)) + len(re.findall(r",", texto))

# Decimales
decimales = re.findall(r"\d+,\d+", texto)


enteros = re.findall(r"\d+", texto)

# Listas
listas = re.findall(r"[Ll]ista:\s*([^\.!?\n]+)", texto)

print("Palabras:", palabras)        
print("Enteros:", len(enteros))     
print("Decimales:", len(decimales)) 
print("Listas:", len(listas))    
