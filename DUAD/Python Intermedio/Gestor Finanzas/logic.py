class Movement:
    def __init__(self, title, amount, category, movement_type):
        self.title = title
        self.amount = amount
        self.category = category
        self.movement_type = movement_type


class Category:
    def __init__(self, name):
        self.name = name


class FinanceManager:
    def __init__(self):
        self.movements = []
        self.categories = []

    def add_movement(self, movement):
        self.movements.append(movement)

    def add_category(self, category):
        self.categories.append(category)

    def total_income(self):
        total = 0
        for movement in self.movements:
            if movement.movement_type == "Ingreso":
                total = total + movement.amount
        return total

    def total_expenses(self):
        total = 0
        for movement in self.movements:
            if movement.movement_type == "Gasto":
                total = total + movement.amount
        return total

    def balance(self):
        return self.total_income() + self.total_expenses()


if __name__ == "__main__":
    manager = FinanceManager()
    manager.add_category(Category("Trabajo"))
    manager.add_movement(Movement("Salario", 1000, "Trabajo", "Ingreso"))
    manager.add_movement(Movement("Comida", -20, "Comida", "Gasto"))

    print("Income:", manager.total_income())
    print("Expenses:", manager.total_expenses())
    print("Balance:", manager.balance())