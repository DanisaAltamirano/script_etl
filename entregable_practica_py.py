# -*- coding: utf-8 -*-
"""Entregable-Practica.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NLCsEyTkWOYn8jf0iJKoj6-I_xbtWeWW
"""

import requests

url = "https://www.themealdb.com/api/json/v1/1/search.php?f=a"  # Reemplaza esta URL con la URL de la API que deseas consumir

response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de respuesta HTTP 200)
if response.status_code == 200:
    data = response.json()  # Convierte la respuesta JSON en un diccionario de Python
    print(data)
else:
    print(f"La solicitud falló con el código de respuesta: {response.status_code}")

import requests
import pandas as pd 

# Realiza una solicitud GET a la API y obtén los datos
url = "https://www.themealdb.com/api/json/v1/1/search.php?f=a"
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de respuesta HTTP 200)
if response.status_code == 200:
    data = response.json()
    meals = data.get("meals", [])  # Obtén la lista de comidas desde los datos

    # Crea un DataFrame a partir de la lista de comidas
    df = pd.DataFrame(meals)

    # Ahora tienes un DataFrame "df" que contiene los datos de la API
    print(df)
else:
    print(f"La solicitud falló con el código de respuesta: {response.status_code}")

import pandas as pd

tabla_texto = df.to_string(index=False)

print(tabla_texto)

nombres_columnas_indexados= list(enumerate(df.columns))
print(nombres_columnas_indexados)

for index, nombre_columna in nombres_columnas_indexados:
    print(f"Columna {index}: {nombre_columna}")

# Elimina las primeras tres letras de todos los nombres de las columnas
nuevos_nombres = {columna: columna[3:] for columna in df.columns}
df = df.rename(columns=nuevos_nombres)

print(df)

nuevos_nombres = {"eal": "Id_Meal"}
df = df.rename(columns=nuevos_nombres)

print(df)

# Convertir los nombres de las columnas a una lista
lista_de_columnas = list(df.columns)
print("Lista de nombres de las columnas:")
print(lista_de_columnas)

nombres_de_columnas_lista = list(df.columns)
print("Nombres de las columnas uno debajo del otro:")
for nombre_columna in nombres_de_columnas_lista:
    print(nombre_columna)

# Selecciona solo las columnas especificadas
columnas_seleccionadas = [
    'Id_Meal', 'Meal', 'DrinkAlternate', 'Category', 'Area',
    'Instructions', 'MealThumb', 'Tags', 'Youtube'
]
df = df[columnas_seleccionadas]

# Muestra el DataFrame resultante
print(df)

# Muestra el total de filas y columnas
total_filas, total_columnas = df.shape


total_filas,
print(f"Total de filas: {total_filas}")
print(f"Total de columnas: {total_columnas}")