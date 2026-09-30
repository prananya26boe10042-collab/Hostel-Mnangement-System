import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "hostel_data.json"


def default_rooms():
    """Create the initial room list used when the project runs for the first time."""
    rooms = []
    for floor in range(1, 4):
        for number in range(1, 5):
            room_no = f"{floor}0{number}"
            rooms.append({
                "room_no": room_no,
                "capacity": 2,
                "occupants": []
            })
    return rooms


def default_data():
    return {
        "students": [],
        "rooms": default_rooms(),
        "payments": [],
        "complaints": []
    }


def initialize_storage():
    """Create the data folder and JSON file if they do not already exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        save_data(default_data())


def load_data():
    """Load all hostel data from the JSON file."""
    initialize_storage()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Data file could not be read. A fresh data file was created.")
        data = default_data()
        save_data(data)

    # Make sure older/incomplete data files still contain all required sections.
    data.setdefault("students", [])
    data.setdefault("rooms", default_rooms())
    data.setdefault("payments", [])
    data.setdefault("complaints", [])

    return data


def save_data(data):
    """Save all hostel data to the JSON file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
