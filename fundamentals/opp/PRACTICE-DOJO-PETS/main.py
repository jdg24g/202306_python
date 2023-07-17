from ninja import *
from mascota import *


ninja1 = Ninja('Jose','Lopez',chancho,['galleta','chocolate','torta'],['pollo','carne','salsa'])
ninja1.alimentar()
ninja1.caminar()
ninja1.bañar()

print(ninja1.mascotas.name)

gatito = Gato('Gato','Siames',['croqueta,pescado'],"Miau")
gatito.ruido()

perrito = Perro('Rojo','Beagle',['Croqueta','Hueso','Asado'],'wau wau')