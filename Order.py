
import random

class Order:
    def __init__(self, customerName: str, item: str, destination: str, itemWeight: float):
        self.customerName = customerName     # Who placed the order
        self.item = item                     # What is being delivered
        self.destination = destination       # Where it needs to go
        self.itemWeight = itemWeight         # Weight in kilograms

    def __str__(self):
        """
        Returns a simple string representation of the order.
        Useful for quick debugging.
        """
        return f"{self.customerName} {self.item} {self.destination} {self.itemWeight}"

# Factory class to generate randomized orders
class OrderFactory:
    # Predefined lists of possible values
    CUSTOMER_NAMES = [
        "Madame Rosa", "Hastur", "Mr. Osono", "Lily", "Patches",
        "Josuke Higashikata", "Giorno Giovanna", "Dio Brando"
    ]

    ITEMS = [
        "Cake", "Letter", "Jar of Honey", "Mysterious Crown", "Music Box",
        "Book", "Bread", "Moonlight Greatsword", "Book of Forbidden Names",
        "Witch’s Hat", "Strange Egg", "Stand Arrow"
    ]

    DESTINATIONS = [
        "Clock Tower", "Bizarre Town", "Hilltop House", "Toy Shop", "Library",
        "Lost Carcosa", "Anor Londo", "Bakery by the Sea",
        "Howl’s Moving Castle", "Crescent Isles", "Witch’s Market"
    ]

    @staticmethod
    def generate_orders(n=5):
        """
        Generate a list of n random delivery orders.
        Each includes customer, item, destination, and a random weight.
        """
        orders = []
        for _ in range(n):
            customer = random.choice(OrderFactory.CUSTOMER_NAMES)
            item = random.choice(OrderFactory.ITEMS)
            destination = random.choice(OrderFactory.DESTINATIONS)
            weight = round(random.uniform(0.5, 5.0), 1)  # weight in kg
            orders.append(Order(customer, item, destination, weight))
        return orders
