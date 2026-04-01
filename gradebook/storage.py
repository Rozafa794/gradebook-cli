import json
import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DEFAULT_DATA = {
    "students": [],
    "courses": [],
    "enrollments": []
}

DATA_FILE = Path("data/gradebook.json")


def load_data(file_path=DATA_FILE):
    
    # Load gradebook data from a JSON file.
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logging.info("Data loaded successfully from %s", file_path)
            return data
    except FileNotFoundError:
        logging.warning("Data file not found. Starting with empty gradebook.")
        return DEFAULT_DATA.copy()
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in %s", file_path)
        print("Error: The gradebook data file is corrupted or invalid JSON.")
        return DEFAULT_DATA.copy()


def save_data(data, file_path=DATA_FILE):
    
    # Save gradebook data to a JSON file.
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        logging.info("Data saved successfully to %s", file_path)
    except OSError as error:
        logging.error("Failed to save data to %s: %s", file_path, error)
        print(f"Error: Could not save data. {error}")