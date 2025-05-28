
from DeliveryMethod import DeliveryMethod, Broom, Walk
from rich import print

# Helper functions for formatted output
def print_header(title):
    print("\n" + "=" * 40)
    print(f"[bold magenta]{title.center(40)}[/bold magenta]")
    print("=" * 40)

def print_subheader(text):
    print(f"[bold cyan]{text}[/bold cyan]")

def print_line():
    print("[dim]" + "-" * 40 + "[/dim]")

class Shop:
    def __init__(self):
        # Regular food/drink items that restore stamina
        self.items = {
            "1": {"name": "Bread", "price": 10, "restore": 15},
            "2": {"name": "Cookies And Cappuccino", "price": 20, "restore": 30},
            "3": {"name": "English Breakfast", "price": 35, "restore": 50},
        }

        # Upgrade items that improve travel methods
        self.upgradeItems = {
            "4": {"name": "Upgrade Broom", "price": 300},
            "5": {"name": "Upgrade Shoes", "price": 350},
        }

    def displayShop(self, chara):
        """
        Display the shop menu including consumables and upgrades.
        """
        print_header("Magic Shop")
        print(f"[yellow]You have {chara.coin} coins[/yellow]\n")

        print_subheader("🍞 Consumables")
        for i, item in self.items.items():
            print(f"{i}. {item['name']:<25} {item['price']:>3} coins → +{item['restore']} stamina")

        print_subheader("🧹 Upgrades")
        for i, upgrade in self.upgradeItems.items():
            print(f"{i}. {upgrade['name']:<25} {upgrade['price']:>3} coins")

        print_line()

    def buy(self, choice, kiki, broom, walking):
        """
        Process purchase based on player's choice.
        Handles both upgrades and consumables.
        """
        # Handle upgrade items
        if choice in self.upgradeItems:
            upgrade = self.upgradeItems[choice]

            if choice == "4":  # Broom upgrade
                if not broom.isUpgraded:
                    if kiki.spendCoin(upgrade["price"]):
                        broom.UpgradedBroom()
                    else:
                        print("Not enough coins to upgrade the Broom.")
                else:
                    print("Broom is already upgraded.")

            elif choice == "5":  # Walking upgrade
                if not walking.isUpgraded:
                    if kiki.spendCoin(upgrade["price"]):
                        walking.UpgradedWalk()
                    else:
                        print("Not enough coins to upgrade Shoes.")
                else:
                    print("Shoes are already upgraded.")

        # Handle regular consumable items
        elif choice in self.items:
            item = self.items[choice]
            if kiki.spendCoin(item["price"]):
                kiki.stamina = min(100, kiki.stamina + item["restore"])
                print(f"You bought {item['name']} and restored {item['restore']} stamina!")
            else:
                print("Not enough coins to buy this item.")

        # Handle invalid inputs
        else:
            print("Invalid choice. Please enter a valid item number.")
