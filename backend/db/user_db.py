from db.database import get_connection
import os

def create_user(username, password_hash, email):
    """user_auth_db에 사용자 추가"""
    with get_connection(os.getenv("USER_DB_NAME")) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s) RETURNING id",
                (username, password_hash, email)
            )
            user_id = cursor.fetchone()[0]
            conn.commit()
            return user_id

def get_user_by_username(username):
    """username으로 사용자 정보 조회"""
    with get_connection(os.getenv("USER_DB_NAME")) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            return user
