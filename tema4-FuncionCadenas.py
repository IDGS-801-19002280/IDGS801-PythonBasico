
cadena="Universidad Tecnologica de León"

print(cadena)
#para poner en minusculas 
print(cadena.lower())
#para poner en mayusculas
print(cadena.upper())
#para poner inicial de cada palabar en mayuscula
print(cadena.title())
#para buscar caracter
print(cadena.find("de"))
#para contar caracter
print(cadena.count("a"))
#remplasa el valor principal por otro valor, en este caso repasa "a" por "4"
textoFinal=cadena.replace("a","4")
print(textoFinal)
#separa los caracteres
cadenaNueva=cadena.split(" ")
print(cadenaNueva)