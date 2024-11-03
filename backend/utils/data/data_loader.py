import json
import os

# 메뉴 데이터 불러오기 함수 정의
def load_menu_data():
    # JSON 파일 경로 설정
    data_path = os.path.join(os.path.dirname(__file__), "../../data/menu_data.json")
    
    # JSON 파일 열기 (읽기 모드, UTF-8 인코딩)
    with open(data_path, 'r', encoding='utf-8') as f:
        # JSON 파일을 파싱하여 Python 딕셔너리로 변환
        menu_data = json.load(f)
    return menu_data  # 메뉴 데이터를 반환