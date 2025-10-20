import json
import os


DATA_DIR = os.path.join(os.getcwd(), 'data')
DATA_FILE = os.path.join(DATA_DIR, 'sessions.json')



os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)


def load_sessions():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ The JSON file is corrupt or empty. I am returning an empty list.")
            data = []
    return data


def save_sessions(sessions):
    with open(DATA_FILE, 'w') as f:
        json.dump(sessions, f, indent=2, ensure_ascii=False)
