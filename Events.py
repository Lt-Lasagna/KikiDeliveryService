import random

def randomEvent(kiki):
    """
    Simulates a random event during delivery.
    Applies an effect to the player and returns a message.
    """

    # List of event definitions, each with:
    # - a name (for reference)
    # - a probability weight (chance)
    # - an effect function applied to Kiki
    # - a message for feedback
    events = [
        {
            "name": "Gust of Wind",
            "chance": 0.2,
            "effect": lambda k: setattr(k, "stamina", max(0, k.stamina - 10)),
            "message": "A strong wind pushed Kiki off course! She lost extra stamina."
        },
        {
            "name": "Friendly Cat Delivery",
            "chance": 0.15,
            "effect": lambda k: setattr(k, "coin", k.coin + 10),
            "message": "A helpful cat helped carry the package. You earned a tip!"
        },
        {
            "name": "Package Mishap",
            "chance": 0.1,
            "effect": lambda k: setattr(k, "coin", max(0, k.coin - 5)),
            "message": "The package got slightly damaged. You lost 5 coins in repairs."
        },
        {
            "name": "Whispers of the Yellow King",
            "chance": 0.08,
            "effect": lambda k: (
                setattr(k, "stamina", max(0, k.stamina - 15)),
                print("You feel a presence... something ancient is watching.")
            ),
            "message": "You heard whispers from beyond... You lost 15 stamina."
        },
        {
            "name": "Stand Encounter: ZA WARUDO!",
            "chance": 0.12,
            "effect": lambda k: setattr(k, "coin", max(0, k.coin - random.randint(5, 15))),
            "message": "Time froze! Someone stole coins while you were frozen!"
        },
        {
            "name": "Nothing Happens",
            "chance": 0.35,
            "effect": lambda k: None,
            "message": "The delivery went smoothly!"
        }
    ]

    try:
        # Randomly select one event based on weights
        chosen = random.choices(events, weights=[e["chance"] for e in events], k=1)[0]
        chosen["effect"](kiki)  # Apply the effect to Kiki
        return chosen["message"]
    except Exception as e:
        print("[Event Error]", e)
        return "Something went wrong during the delivery event."
