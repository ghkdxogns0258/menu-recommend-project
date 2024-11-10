CREATE TABLE IF NOT EXISTS menus (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    cuisine_type VARCHAR(50),
    taste_profile JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);