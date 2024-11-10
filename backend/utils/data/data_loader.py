import os
import json

def load_menu_data():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    data_path = os.path.join(base_dir, "menu_data", "menu_data.json")
    
    with open(data_path, 'r', encoding='utf-8') as f:
        menu_data = json.load(f)
    return menu_data
