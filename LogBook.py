
import json
import os

def saveLog(log, filename='data/deliveries.json'):
    """
    Saves the log (a list of delivery/rest events) to a JSON file.
    Automatically creates the directory if it doesn't exist.
    """
    if not log:
        print("No log entries to save.")
        return

    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Save log to JSON
        with open(filename, 'w') as f:
            json.dump(log, f, indent=4)

        print("Log saved successfully.")
    except Exception as e:
        print(f"[Error saving log] {e}")

def loadLog(filename='data/deliveries.json'):
    """
    Loads the delivery/rest log from a JSON file.
    Returns an empty list if the file is missing or corrupt.
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"[Error decoding log file] {e}")
        return []
    except Exception as e:
        print(f"[Error loading log] {e}")
        return []
