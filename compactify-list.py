

prev = [-1,0,1,2,3,4,5,6]
key = [-1,-1,-1,-1,-1,-1,-1,-1]
next = [1,2,3,4,5,6,7,-1]


freeList = 0
L = -1  

def printMemoria():
	#global prev
	#global key 
	print ("\nEstado de los arreglos que representan la memoria:")
	print ("prev: " + str(prev))
	print ("key : " + str(key))
	print ("next: " + str(next))
	print("L: " + str(L))
	print("freeList: " + str(freeList))

def printList():
	print ("Lista Actual:")
	aux = L
	print("(", end="", flush=True)
	while aux != -1:
		print(key[aux], end=' ', flush=True)
		aux = next[aux]
	print(")", end="\n", flush=True)


def allocateObject():
	global freeList
	if (freeList == -1):
		print ("error, falta de espacio")
		return -1
	else:
		aux = freeList
		freeList = next[aux]
		return aux ## posicion asignada al nuevo "objeto" 



def freeListObject(x): ## x es el apuntador o posicion del objeto a liberrar
	prev[freeList] = x
	next[x] = freeList
	prev[x] = -1
	key[x] = -1




def crearObjeto(x):
	pointer = allocateObject()
	
	auxL = L # el apuntador a la lista anterior
	
	if not (pointer == -1): # hay espacio
		
		prev[pointer] = -1 # inserto siempre al comienzo de la lista
		key[pointer] = x
		next[pointer] = auxL # apunto al comienzo de la lista

		if (auxL != -1):
			prev[auxL] = pointer
			
		return pointer
 	
def borrarObjeto(x): # x es el apuntador al objeto a borrar
	
	global freeList

	# Actualizo los apuntadores de los elementos previo y siguiente al que voy a borrar
	if not (prev[x] ==-1): # hay un elemento previo
		next[prev[x]] = next[x]
	if not (next[x] == -1): # hay un elemento siguiente
		prev[next[x]] = prev[x]
	# libero la memoria del objeto
	freeListObject(x)
	freeList = x



def compactifyList():
	global L
	global freeList

	auxList = L
	numElems = 0
	if (freeList == -1): # no casillas hay vacias
		return
	else:
		i = 0 
		while (auxList != -1):
			intercambiar(i, auxList)
			auxList = next[auxList]
			i = i+1
		
		#auxList = next[auxList]
		#intercambiar(i, auxList)
				
		L = 0
		freeList = i+1



def intercambiar(p1, p2):
	
	print ("Intercambio: " + str(p1) + ","  + str(p2))
	key[p1], key[p2] = key[p2], key[p1]
	
	next[prev[p1]], next[prev[p2]] = next[prev[p2]], next[prev[p1]]
	prev[p1], prev[p2] = prev[p2], prev[p1]
	
	prev[next[p1]], prev[next[p2]] = prev[next[p2]], prev[next[p1]]
	next[p1], next[p2] = next[p2], next[p1]
	

print("memoria inicial")
printMemoria()
printList()

L = crearObjeto(21)
print("inserte 21")
printMemoria()
printList()

L = crearObjeto(15)
print("inserte 15")
printMemoria()
printList()

'''L = crearObjeto(17)
print("inserte 17")
#printMemoria()
#printList()

L = crearObjeto(13)
print("inserte 13")
printMemoria()
printList()

print("Borro el elemento en la posicion 0 de la memoria")
borrarObjeto(0)
printMemoria()
printList()

#print("Compacto la memoria")
#compactifyList()
#printMemoria()
#printList()
'''





