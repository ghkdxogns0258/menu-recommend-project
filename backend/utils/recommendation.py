from datetime import datetime

def calculate_menu_score(user_preferences, menu, current_weather):
    """
    메뉴 추천 점수를 계산합니다.
    - user_preferences: 사용자 선호도(JSON)
    - menu: 메뉴 데이터(JSON)
    - current_weather: 현재 날씨 정보
    """
    score = 0

    # 1. 사용자 선호도 반영
    for taste, weight in user_preferences.get("taste", {}).items():
        menu_taste = menu["taste_profile"].get(taste, 0)
        score += weight * menu_taste

    # 2. 시간대 적합성 반영
    now = datetime.now()
    time_key = f"time_{['morning', 'lunch', 'dinner'][now.hour // 8]}"
    if menu["features"].get(time_key):
        score += 0.2  # 시간 적합성 가중치

    # 3. 날씨 적합성 반영
    weather_key = f"weather_{current_weather}"
    if menu["features"].get(weather_key):
        score += 0.3  # 날씨 적합성 가중치

    return score

def filter_recent_menus(menu_name, recent_menus):
    """
    최근 선택 메뉴를 필터링합니다.
    - menu_name: 현재 평가 중인 메뉴 이름
    - recent_menus: 최근 선택된 메뉴 리스트
    """
    return menu_name not in recent_menus
