import json
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "new_words.json")

def save(text, selected, input_lang):
    now = datetime.now()
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

        if input_lang == "Chinese":
            data["Chinese"].append({
                "text": text,
                "selected": selected,
                "time": now.isoformat()

            })

        else:
            data["English"].append({
            "text": text,
            "selected": selected,
            "time": now.isoformat()
            })

    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def check():
    with open(JSON_PATH, "r", encoding="utf-8") as file:
    
        data = json.load(file)
    now = datetime.now()
    cutoff = now - timedelta(days=30)

    english_list = [entry for entry in data["English"] if datetime.fromisoformat(entry["time"]) > cutoff ]

    chinese_list = [entry for entry in data["Chinese"] if datetime.fromisoformat(entry["time"]) > cutoff ]

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "Chinese": chinese_list, "English" : english_list
        },f,  ensure_ascii=False, indent=4)

