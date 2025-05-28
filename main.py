
from Kiki import Kiki
from Order import Order
from DeliveryMethod import DeliveryMethod, Train, Broom, Walk
from LogBook import saveLog, loadLog
from Shop import Shop
from Order import OrderFactory
from rich import print
from rich.panel import Panel

# Utility functions for formatting
def print_header(title):
    print("\n" + "="*40)
    print(f"[bold magenta]{title.center(40)}[/bold magenta]")
    print("="*40)

def print_subheader(text):
    print(f"[bold cyan]{text}[/bold cyan]")

def print_line():
    print("[dim]" + "-"*40 + "[/dim]")

def main():
    kiki = Kiki(input("Enter your character's name: "))
    shop = Shop()
    orders = OrderFactory.generate_orders()
    broom = Broom()
    walk = Walk()
    travelMethods = {
        "1": broom,
        "2": walk,
        "3": Train(),
    }

    while True:
        print_header(f"{kiki.name}'s Delivery Service")
        print(f"[yellow]Coins: {kiki.coin} | Stamina: {kiki.stamina}[/yellow]")
        print_line()
        print("1. 📜 View Orders")
        print("2. 📦 Deliver an Order")
        print("3. 💤 Rest (100 coins)")
        print("4. 📖 View Log")
        print("5. 💾 Save & Exit")
        print("6. 🛍️ Visit Shop")
        print_line()

        choice = input("Choose an option: ")

        # View Orders
        if choice == "1":
            print_subheader("Today's Orders")
            for i, order in enumerate(orders):
                content = (
                    f"📦 [bold]Item:[/bold] {order.item}\n"
                    f"👤 [bold]Customer:[/bold] {order.customerName}\n"
                    f"📍 [bold]Destination:[/bold] {order.destination}\n"
                    f"⚖️  [bold]Weight:[/bold] {order.itemWeight} kg"
                )
                print(Panel(content, title=f"[{i + 1}] Delivery Order", border_style="cyan"))

            if not orders:
                print("[red]No orders for today[/red]")
            input("\nPress Enter to return to the main menu...")
            continue

        # Deliver an Order
        elif choice == "2":
            try:
                idx = int(input("Choose order number: ")) - 1
                method_choice = input("Delivery method (1. Broom, 2. Walk, 3. Train - 50 coins): ")
                method = travelMethods[method_choice]
                order = orders.pop(idx)
                kiki.deliver(order, method)
            except (ValueError, IndexError):
                print("[red]Invalid order number. Please try again.[/red]")
            except KeyError:
                print("[red]Invalid delivery method selected.[/red]")
            input("\nPress Enter to return to the main menu...")
            continue

        # Rest
        elif choice == "3":
            if kiki.spendCoin(100):
                kiki.rest()
                print("[green]You rested! New orders have arrived.[/green]")
                orders.clear()
                orders.extend(OrderFactory.generate_orders())
            else:
                print("[red]Not enough coins to rest![/red] (100 coins required)")
            input("\nPress Enter to return to the main menu...")
            continue

        # View Log
        elif choice == "4":
            log_entries = kiki.viewLog()
            if not log_entries:
                print("[dim]No activities recorded yet.[/dim]")
            else:
                print("\n[bold cyan]Activity Log[/bold cyan]")
                for entry in log_entries:
                    if entry["type"] == "delivery":
                        d = entry["details"]
                        print(f"• Delivered {d['item']} to {d['customer']} at {d['destination']} via {d['method']} (+{d['reward']} coins)")
                    elif entry["type"] == "rest":
                        print(f"• {entry['details']}")
            input("\nPress Enter to return to the main menu...")

        # Visit Shop
        elif choice == "6":
            shop.displayShop(kiki)
            choice = input("Choose an item to buy: ")
            shop.buy(choice, kiki, broom, walk)
            input("\nPress Enter to return to the main menu...")

        # Save & Exit
        elif choice == "5":
            saveLog(kiki.viewLog())
            print("[bold green]Log saved! Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main()
