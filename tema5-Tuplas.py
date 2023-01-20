
tupla=(1,2,3)
print(tupla)

print(type(tupla))

tupla2=(7,"Chucky",True,21.7,17+7j)
print(tupla2)

#se puede acceder a los elementos desde su indice
print(tupla2[1])
print(tupla2[4])
#para mostrar el ultimo elemento de la tupla
print(tupla2[-1])
#muestra los valores dentro del rango establecido 
print(tupla2[0:3])
print(tupla2[:3])
print(tupla2[3:])

a,b,c=tupla

print(a)
print(c)

tuplaN=tupla+tupla2
print(tuplaN)
print(tupla.count(2))

