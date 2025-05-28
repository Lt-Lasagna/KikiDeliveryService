
class DeliveryMethod:
    def __init__(self, name: str, staminaCost: int, timeMinutes: int):
        self.name = name                  # Method name (e.g., Broom, Walk, Train)
        self.staminaCost = staminaCost    # Stamina required to use this method
        self.timeMinutes = timeMinutes    # Travel time in minutes (for flavor)

# Broom travel option
class Broom(DeliveryMethod):
    def __init__(self):
        super().__init__("Broom", staminaCost=25, timeMinutes=30)
        self.isUpgraded = False           # Upgrade status

    def UpgradedBroom(self):
        """
        Reduces stamina and time cost when upgraded.
        """
        if not self.isUpgraded:
            self.staminaCost = 15
            self.timeMinutes = 20
            self.isUpgraded = True
            print("The Broom has been upgraded")
        else:
            print("You have already upgraded the Broom")

# Walking travel option
class Walk(DeliveryMethod):
    def __init__(self):
        super().__init__("Walk", staminaCost=75, timeMinutes=60)
        self.isUpgraded = False

    def UpgradedWalk(self):
        """
        Reduces stamina and time cost when upgraded.
        """
        if not self.isUpgraded:
            self.staminaCost = 40
            self.timeMinutes = 45
            self.isUpgraded = True
            print("The Walking has been upgraded")
        else:
            print("You have already upgraded the Walking")

# Train travel option (costs stamina + coins)
class Train(DeliveryMethod):
    def __init__(self):
        super().__init__("Train", staminaCost=10, timeMinutes=15)
        self.coinCost = 50  # Coins required to ride the train

    # Future idea: add a "Train Pass" item to reduce or waive cost
