import pandas as pd

# Dades inicials
notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]

# Llistes per emmagatzemar les dades transformades
notas_arregladas = []
noms_complets = []
notes_textuals = []
llista_final = []

# Ajustar les notes per assegurar-se que cap nota no superi el 10
for nota in notes:
    notas_arregladas.append(nota + 1 if nota < 10 else nota)

# Generar noms complets i emmagatzemar-los a noms_complets
for nom, cognom in zip(alumnes, cognoms):
    noms_complets.append(f"{nom} {cognom}")

# Assignar qualificacions textuals segons la nota
for n in notas_arregladas:
    if n == 10:
        notes_textuals.append("Matrícula d'honor")
    elif n < 5:
        notes_textuals.append("Suspès")
    elif 5 <= n <= 6:
        notes_textuals.append("Aprovat")
    elif 6 < n < 7:
        notes_textuals.append("Bé")
    elif 7 <= n < 9:
        notes_textuals.append("Notable")
    else:
        notes_textuals.append("Excel·lent")

# Crear un diccionari per a cada alumne amb les seves dades
for n, nom, q in zip(notas_arregladas, noms_complets, notes_textuals):
    llista_final.append({"nom_alumne": nom, "nota": n, "qualificacio": q})

# Convertir la llista de diccionaris en un DataFrame de pandas
df = pd.DataFrame(llista_final)

# Imprimir el DataFrame resultant
print(df)

# Guardar el DataFrame en un arxiu CSV
df.to_csv("dades.csv", index=False)
