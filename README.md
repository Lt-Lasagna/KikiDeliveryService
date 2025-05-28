# KikiDeliveryService

The Cat Sanctuary 

Credits:

Mustafa Alazzawi

Yamen Alamer

Adilya Makaeva


Project for Basic Programming 2
# 📦 Kiki’s Delivery Service – A Python Simulation Game

Welcome to **Kiki’s Delivery Service**, a whimsical, text-based simulation game where you play as a young witch managing a magical delivery business in a cozy town.

This project blends Ghibli-inspired storytelling with RPG mechanics and showcases clean Python architecture, file handling, modular design, and terminal UI enhancements.

---

## 🎮 Features

- **Deliver Orders**  
  Choose between Broom, Walk, or Train to deliver packages across magical destinations.

- **Dynamic Events**  
  Random events can impact your delivery with rewards or penalties.

- **Rest & Recover**  
  Spend coins to rest and restore your stamina.

- **Shop System**  
  Buy consumables or upgrade your transport methods to boost efficiency.

- **Persistent Activity Log**  
  Every action is logged and saved using JSON, allowing continuity between sessions.

- **Stylized Terminal UI**  
  Uses the `rich` library for vibrant headers, borders, and feedback.

---

## 🧱 Project Structure

| File                | Description                                        |
|---------------------|----------------------------------------------------|
| `main.py`           | Game loop and menu navigation                      |
| `Kiki.py`           | Player logic and delivery behavior                 |
| `Order.py`          | Order creation and random generation               |
| `Shop.py`           | Shop menu and item purchase logic                  |
| `Events.py`         | Random delivery events                             |
| `DeliveryMethod.py` | Broom, Walk, and Train definitions                 |
| `LogBook.py`        | Saving/loading player logs                         |

---

## 💻 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/kiki-delivery-game.git
   cd kiki-delivery-game
Install dependencies:
pip install rich


Run the game:
python main.py

