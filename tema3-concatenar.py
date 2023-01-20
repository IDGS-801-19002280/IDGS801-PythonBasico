
texto1= "Hola"
texto2= "Mundo!!"
textoFinal= texto1+" "+texto2
print(textoFinal)

print("El saludo es %s %s " % (texto1,texto2))

#en parentesis se puede seleccionar el orden de los valores, la frace se alteraria
cadena="Saludar dos: {} {} ".format(texto1,texto2)
print(cadena)

cadena="Saludar tres: {x} {y} ".format(x=texto1,y=texto2)
print(cadena)