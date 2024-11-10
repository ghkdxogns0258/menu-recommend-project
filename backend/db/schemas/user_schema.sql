CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    provider_id VARCHAR(100) UNIQUE NOT NULL,  -- OAuth 제공자별 고유 ID
    provider VARCHAR(50) NOT NULL,             -- 제공자 이름 (e.g., Kakao, Google, Naver)
    email VARCHAR(100) UNIQUE,                 -- 사용자 이메일
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_profile (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100),
    age INTEGER,
    preferences JSONB,                         -- e.g., {"taste": true, "value": true, ...}
    dietary_restrictions JSONB,                -- e.g., {"sweet": true, "salty": false, ...}
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
);