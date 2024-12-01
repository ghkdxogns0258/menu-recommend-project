import apiClient from './api_client';

/**
 * 세션 동기화 API 호출
 * @returns user_id 반환
 */
export const syncSession = async (): Promise<string | null> => {
    try {
        const response = await apiClient.get('/sync-session');
        return response.data.user_id;
    } catch (error) {
        console.error("세션 동기화 실패:", error);
        return null;
    }
};
