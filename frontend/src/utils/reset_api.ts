import apiClient from './api_client';

/**
 * 사용자 모델 초기화 API 호출
 * @param user_id 사용자 ID
 * @returns 서버 응답 데이터
 */
export const resetUserModel = async (user_id: string) => {
  try {
    const response = await apiClient.post('/reset-model', { user_id });
    console.log("모델 초기화 성공:", response.data);
    return response.data;
  } catch (error) {
    console.error("모델 초기화 실패", error);
    throw error;
  }
};
