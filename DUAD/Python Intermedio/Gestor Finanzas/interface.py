import FreeSimpleGUI as sg
from logic import FinanceManager, Category, Movement
from persistence import save_data, load_data


def add_category_window():
    layout = [
        [sg.Text("Enter the category name:")],
        [sg.Input(key="-CATEGORY-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    window = sg.Window("Add Category", layout)
    category_name = None
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "Save":
            category_name = values["-CATEGORY-"]
            break
    window.close()
    return category_name


def add_movement_window(movement_type, categories):
    if not categories:
        sg.popup("Error: You need to add a category first!")
        return None
    category_names = [category.name for category in categories]
    layout = [
        [sg.Text(f"Add {movement_type}")],
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category:"), sg.Combo(category_names, key="-CATEGORY-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    window = sg.Window(f"Add {movement_type}", layout)
    result = None
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "Save":
            title = values["-TITLE-"]
            amount = values["-AMOUNT-"]
            category = values["-CATEGORY-"]

            if not title or not amount or not category:
                sg.popup("Error: All fields are required!")
                continue

            try:
                float(amount)
            except ValueError:
                sg.popup("Error: Amount must be a number!")
                continue

            result = {
                "title": title,
                "amount": amount,
                "category": category
            }
            break
    window.close()
    return result


def get_table_data(manager):
    data = []
    for movement in manager.movements:
        data.append([movement.title, movement.amount, movement.category, movement.movement_type])
    return data


def main_window():
    manager = load_data()
    headers = ["Title", "Amount", "Category", "Type"]
    layout = [
        [sg.Text("Personal Finance Manager", font=("Any", 16))],
        [sg.Table(values=get_table_data(manager), headings=headers, key="-TABLE-", auto_size_columns=True, num_rows=10, justification="center")],
        [sg.Button("Add Category"), sg.Button("Add Income"), sg.Button("Add Expense"), sg.Button("Exit")]
    ]
    window = sg.Window("Finance Manager", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Add Category":
            name = add_category_window()
            if name:
                manager.add_category(Category(name))
                save_data(manager)
                sg.popup(f"Category '{name}' added!")
        if event == "Add Income":
            result = add_movement_window("Income", manager.categories)
            if result:
                movement = Movement(result["title"], float(result["amount"]), result["category"], "Ingreso")
                manager.add_movement(movement)
                window["-TABLE-"].update(values=get_table_data(manager))
                save_data(manager)
                sg.popup(f"Income '{result['title']}' added!")
        if event == "Add Expense":
            result = add_movement_window("Expense", manager.categories)
            if result:
                movement = Movement(result["title"], -float(result["amount"]), result["category"], "Gasto")
                manager.add_movement(movement)
                window["-TABLE-"].update(values=get_table_data(manager))
                save_data(manager)
                sg.popup(f"Expense '{result['title']}' added!")
    window.close()


if __name__ == "__main__":
    main_window()
