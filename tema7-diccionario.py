
#un tipo de dato que nos pemite almacenar distintos tipos de datos asociados de un key valor
#son definidos atraves de llaves
miDiccionario={"Matricula":123456, "Nombre":"Dario", "edad":23}

print(type(miDiccionario))
print(miDiccionario)

#esto es para cambiar el valor de una cosa
miDiccionario["Nombre"]="Panfilo"
print(miDiccionario)

print(miDiccionario["edad"])
print(miDiccionario.values())
print(miDiccionario.keys())
