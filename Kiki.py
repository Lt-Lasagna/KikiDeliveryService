
from DeliveryMethod import DeliveryMethod
from Order import Order
from Events import randomEvent
from datetime import datetime

# Constant for max stamina
maxStamina = 100

# Main character class
class Kiki:
    def __init__(self, name, stamina=100):
        self.name = name                # Character's name
        self.stamina = stamina          # Current stamina
        self.coin = 10                  # Starting coins
        self.log = []                   # Activity log (deliveries and rests)

    def rest(self):
        """
        Fully restore stamina and log the rest.
        """
        self.stamina = maxStamina
        self.log.append({
            "type": "rest",
            "details": "You took a restful break.",
            "timestamp": datetime.now().isoformat()
        })
        print(f"You have rested and your stamina is now {self.stamina}")

    def viewLog(self):
        """
        Return the activity log.
        """
        return self.log

    def addCoin(self, amount):
        """
        Add coins to the character's balance.
        """
        self.coin += amount

    def spendCoin(self, amount):
        """
        Spend coins if enough are available.
        Returns True if the purchase was successful.
        """
        if self.coin >= amount:
            self.coin -= amount
            return True
        else:
            return False

    def deliver(self, order: Order, method: DeliveryMethod):
        """
        Attempt to deliver an order using the selected delivery method.
        - Deducts stamina
        - Triggers a random event
        - Grants coin reward based on item weight
        - Logs the delivery
        """
        reward = int(order.itemWeight * 10)

        # Check if enough stamina to proceed
        if self.stamina < method.staminaCost:
            print("You don't have enough stamina.\nDelivery unsuccessful.")
            return

        # Check for Train-specific coin cost
        if method.name == "Train":
            if not self.spendCoin(method.coinCost):
                print(f"You don't have enough coins to use the Train! (Requires {method.coinCost} coins)")
                return
            else:
                print(f"You spent {method.coinCost} coins to use the Train.")

        # Perform delivery
        try:
            eventMessage = randomEvent(self)
            print(f"[Event] {eventMessage}")
            self.stamina -= method.staminaCost
            self.addCoin(reward)

            self.log.append({
                "type": "delivery",
                "details": {
                    "item": order.item,
                    "customer": order.customerName,
                    "destination": order.destination,
                    "method": method.name,
                    "reward": reward
                },
                "timestamp": datetime.now().isoformat()
            })

            print(
                f"Delivery successful! {order.item} for {order.customerName} via {method.name}.\n"
                f"Stamina: {self.stamina} | Coins: {self.coin}"
            )
        except Exception as e:
            print(f"[Delivery Error] {e}")
