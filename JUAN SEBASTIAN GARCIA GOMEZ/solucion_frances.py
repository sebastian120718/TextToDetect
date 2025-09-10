import re

texto = ("Salut! En 2025, 18 médecins soignent ensemble. Liste: thermomètre, blouse, ordonnance. "
"Le prix est de 73,40€. Les étoiles (★) brillent la nuit. 14 chats guérissent, 13 chiens aident. "
"Le code #5566 est spécial. 17 jours de soins, 11 jours de repos. @tous soignent. "
"Le numéro magique est 1020. Que feriez-vous avec 51,70€? "
"La réponse est dans la liste: guérir, aider, écouter. "
"Prenez soin de votre santé! 100 mots, 17 entiers, 3 décimaux, 2 listas.")


palabras = len(re.findall(r"\w+", texto, re.UNICODE)) + len(re.findall(r",", texto))


decimales = re.findall(r"\d+[.,]\d+", texto)


enteros = re.findall(r"\d+", texto)


listas = re.findall(r"[Ll]iste?:\s*([^\.!?\n]+)", texto)

print("Palabras:", palabras)       
print("Enteros:", len(enteros))    
print("Decimales:", len(decimales))
print("Listas:", len(listas))    
