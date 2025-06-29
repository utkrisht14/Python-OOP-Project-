class Milk:
    def __init__(self, amount_ml: int, temperature: int):
        self.amount_ml = amount_ml
        self.temperature = temperature

    def describe(self):
        print(f"Milk: {self.amount_ml}ml at {self.temperature}°C.")


class Coffee:
    def __init__(self, name: str, temperature: int, price: float, milk: Milk = None):
        self.name = name
        self.temperature = temperature
        self.price = price
        self.milk = milk  # Composition

    def describe(self):
        print(f"This is a {self.name} served at {self.temperature}°C. Price: €{self.price:.2f}")
        if self.milk:
            self.milk.describe()


class Espresso(Coffee):
    def __init__(self):
        super().__init__("Espresso", 80, 2.50)  # No milk


class Latte(Coffee):
    def __init__(self):
        steamed_milk = Milk(amount_ml=150, temperature=65)
        super().__init__("Latte", 70, 3.50, milk=steamed_milk)


class CoffeeMachine:
    def __init__(self, machine_name: str):
        self.machine_name = machine_name

    def brew_coffee(self, coffee_type: Coffee) -> Coffee:
        print(f"{self.machine_name} is brewing {coffee_type.name}...")
        return coffee_type


class Barista:
    def __init__(self, name: str, coffee_machine: CoffeeMachine):
        self.name = name
        self.coffee_machine = coffee_machine

    def make_coffee(self, coffee: Coffee):
        print(f"{self.name} is preparing your coffee.")
        brewed = self.coffee_machine.brew_coffee(coffee)
        brewed.describe()


# Example usage
machine = CoffeeMachine("BrewMaster Pro")
barista = Barista("Lela", machine)

espresso = Espresso()
latte = Latte()

barista.make_coffee(espresso)
print()
barista.make_coffee(latte)
