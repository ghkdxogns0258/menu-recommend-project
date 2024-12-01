import axios from 'axios';

// 환경 변수 출력
console.log("REACT_APP_BACKEND_URL:", process.env.REACT_APP_BACKEND_URL);

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';

/**
 * DB에서 사용자 ID를 가져옵니다.
 * @returns {Promise<string | null>} 사용자 ID (로그인 상태가 아니면 null 반환)
 */
export const getUserIdFromDatabase = async (): Promise<string | null> => {
    try {
        console.log("Using BACKEND_URL:", BACKEND_URL); // 백엔드 URL 확인
        const response = await axios.get(`${BACKEND_URL}/auth/user-id`, {
            withCredentials: true, // 쿠키를 포함한 인증 정보 전송
        });
        if (response.data && response.data.user_id) {
            console.log("Fetched user_id:", response.data.user_id); // 가져온 user_id 로그
            return response.data.user_id;
        } else {
            console.warn("user_id not found in response.");
            return null;
        }
    } catch (error) {
        console.error("Failed to fetch user ID from database:", error);
        return null;
    }
};