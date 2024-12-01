import apiClient from './api_client';

/**
 * 메뉴 추천 API 호출
 * @param user_id 사용자 ID
 * @returns 추천된 메뉴 데이터
 */
export const getMenuRecommendation = async (user_id: string) => {
    try {
        const response = await apiClient.get(`/recommend?user_id=${user_id}`);
        return response.data;
    } catch (error) {
        console.error("메뉴 추천 실패", error);
        throw error;
    }
};

/**
 * 사용자 피드백 전송
 * @param menu_name 메뉴 이름
 * @param liked 좋아요 여부
 * @param user_id 사용자 ID
 * @returns 서버 응답 데이터
 */
export const sendFeedback = async (menu_name: string, liked: boolean, user_id: string) => {
    try {
        const response = await apiClient.post('/feedback', { menu_name, liked, user_id });
        return response.data;
    } catch (error) {
        console.error("피드백 전송 실패", error);
        throw error;
    }
};
