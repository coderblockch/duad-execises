import csv

def get_game():
    name = input("game name: ")
    genre = input("genre: ")
    developer = input("developer: ")
    classification = input("classification: ")
    return [name, genre, developer, classification]

def save_games(games):
    with open("videogames.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "genre", "developer", "classification"])
        for game in games:
            writer.writerow(game)

# --- parte principal ---
n = int(input("how many videogames? "))
games = []

for i in range(n):
    game = get_game()
    games.append(game)

save_games(games)
print("archivo guardado!")