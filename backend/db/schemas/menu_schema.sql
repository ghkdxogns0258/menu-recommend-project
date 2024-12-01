CREATE TABLE IF NOT EXISTS menus (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,               -- 메뉴 이름
    description TEXT,                         -- 메뉴 설명
    cuisine_type VARCHAR(50),                 -- 요리 스타일 (예: 한식, 중식, 양식)
    menu_features JSONB NOT NULL,             -- 입맛 프로필 (예: {"sweet": 0.8, "salty": 0.7})
    time_morning BOOLEAN DEFAULT FALSE,       -- 아침에 적합한 메뉴 여부
    time_lunch BOOLEAN DEFAULT FALSE,         -- 점심에 적합한 메뉴 여부
    time_dinner BOOLEAN DEFAULT FALSE,        -- 저녁에 적합한 메뉴 여부
    weather_cold BOOLEAN DEFAULT FALSE,       -- 추운 날 적합한 메뉴 여부
    weather_hot BOOLEAN DEFAULT FALSE,        -- 더운 날 적합한 메뉴 여부
    weather_rainy BOOLEAN DEFAULT FALSE,      -- 비 오는 날 적합한 메뉴 여부
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
