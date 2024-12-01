import os
import json

def load_menu_data():
    """
    JSON 파일에서 메뉴 데이터를 로드합니다.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    data_path = os.path.join(base_dir, "menu_data", "menu_data.json")

    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            menu_data = json.load(f)
            return menu_data
    except FileNotFoundError:
        print(f"Error: File not found at {data_path}")
        return []
    except json.JSONDecodeError:
        print("Error: JSON Decode Error")
        return []