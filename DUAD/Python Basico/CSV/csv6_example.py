import csv

n = int(input("how many videogames? "))

with open("videogames.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # AQUÍ va el encabezado (1 sola vez, fuera del for)
    writer.writerow(["name", "genre", "developer", "classification"])
    
    for i in range(n):
        name = input("game name: ")
        genre = input("genre: ")
        developer = input("developer: ")
        classification = input("classification: ")
        # AQUÍ va cada videojuego (n veces, dentro del for)
        writer.writerow([name, genre, developer, classification])