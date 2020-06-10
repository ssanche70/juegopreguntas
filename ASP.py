import pandas as pd
import random
from random import sample

"""
Se asigna una variable para abrir el documento df

----------

La funcion menu esta activa hasta que el jugador seleccione jugar o salir
"""
df = pd.read_csv('C:\\Users\\Sebastian Sanchez\\Downloads\\Data.csv')


def menu():

    print('Menu')
    print('1------Jugar')
    print('2------Salir')
    op = input('Seleccione una opcion')
    if op == '1':
        preguntar()
    elif op == '2':
        exit()
    else:
        menu()

"""
respuestas es una variable aleatoria entre 2 y el numero de filas
num_fil --> Determina el numero de filas 
ale --> aleatorio entre las preguntas
imprime la pregunta y las cuatro respuestas, estas en orden diferente al de la lista original
ans es la variable donde se almacena lo que el usuario respondió
dfe guarda las respuesas correctas en un arreglo
el if verifica si la respuesta es correcta y corresponde a la pregunta
si acierta, el jugador podrrá seguir jugando
si no el juego vuelve al menú

"""


def preguntar():
    respuestas = sample(range(2, 6), 4)
    num_fil = len(df.axes[0])
    ale = random.randint(0,num_fil -1)
    print(df.iloc[ale,1] + '\n A: ' + df.iloc[ale,respuestas[0]] + '\n B: ' + df.iloc[ale,respuestas[1]] + '\n C: '
          + df.iloc[ale,respuestas[2]] + '\n D: ' + df.iloc[ale,respuestas[3]])

    ans = str(input('Su respuesta: Copie y pegue la que usted crea correcta,'))
    #dfe = df['V'].values
    #for index, row in df.iterrows():
        #val = row['#']
        #val2 = val - 1
    if ans == df.iloc[ale,2]:
        print('CORRECTO')
        preguntar()
    else:
        print('Perdiste')
        menu()

menu()

#for index, row in df.iterrows():
    #val = row['#']
    #print(type(index))
#num_fil = len(df.axes[0])
#ale = random.randint(0,num_fil -1)
#print(df.index[ale])
#print(len(df.axes[0]))
#print(ale)
#print(df.iloc[ale,2])
"""
def siguiente_pregunta():
    for i, j in p2.items():
        print(j)
    ans = input('Su respuesta')
    if ans == 'A':
        print('Correcto')
        siguiente_pregunta()
    else:
        print('Perdiste')
        menu()

def jugar():
    siguiente_pregunta()

"""







