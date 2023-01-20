
nombres=["Juan","Mario","Laura"]
numeros=[1,2,3,4,5,6,7,8,9]

datos=[1,2,3,"Mario",True]

nombres[0]="Chucky"

print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

nombres.append("Dario")
print(nombres)
nombres.insert(2,"Chencha")
print(nombres)

nombres.extend(["Cleotilde",2,23,5])
print(nombres)

nombres.remove("Cleotilde")
print(nombres)
#para eliminar el ultimo elemento
nombres.pop()
print(nombres)

n=["Juan"]
n2=n*5
print(n2)

del nombres[0]
print(nombres)