-- users 테이블 생성
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    provider_id VARCHAR(100) UNIQUE NOT NULL,  -- OAuth 제공자별 고유 ID
    provider VARCHAR(50) NOT NULL,             -- 제공자 이름 (e.g., Kakao, Google, Naver)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- user_profile 테이블 생성
CREATE TABLE IF NOT EXISTS user_profile (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100),
    age INTEGER,
    preferences JSONB,                         -- 선호도 정보 (예: {"taste": 0.5, "value": 0.75, ...})
    taste_profile JSONB,                       -- 입맛 정보 (예: {"sweet": 0.5, "salty": 0.75, ...})
    is_info_complete BOOLEAN DEFAULT FALSE,    -- 정보 입력 완료 여부
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
);