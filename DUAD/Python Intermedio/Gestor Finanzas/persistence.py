import json
from logic import Movement, Category, FinanceManager


def save_data(manager, filename="finance_data.json"):
    data = {
        "movements": [],
        "categories": []
    }
    # Convertir cada movimiento a diccionario
    for movement in manager.movements:
        data["movements"].append({
            "title": movement.title,
            "amount": movement.amount,
            "category": movement.category,
            "movement_type": movement.movement_type
        })
    # Convertir cada categoría a diccionario
    for category in manager.categories:
        data["categories"].append({
            "name": category.name
        })
    # Guardar en el archivo
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
from logic import Movement, Category, FinanceManager


def load_data(filename="finance_data.json"):
    manager = FinanceManager()
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        for cat in data["categories"]:
            manager.add_category(Category(cat["name"]))
        for mov in data["movements"]:
            manager.add_movement(Movement(
                mov["title"], mov["amount"], mov["category"], mov["movement_type"]
            ))
    except FileNotFoundError:
        pass  # si no existe el archivo, empieza vacío
    return manager

if __name__ == "__main__":
    # Crear un manager con datos
    manager = FinanceManager()
    manager.add_category(Category("Trabajo"))
    manager.add_movement(Movement("Salario", 1000, "Trabajo", "Ingreso"))
    
    # Guardar
    save_data(manager)
    print("Datos guardados!")
    
    # Cargar
    loaded = load_data()
    print("Movimientos cargados:", len(loaded.movements))
    print("Primer movimiento:", loaded.movements[0].title)

