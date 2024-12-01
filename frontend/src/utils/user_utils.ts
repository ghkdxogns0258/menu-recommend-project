import axios from './api_client';

// 선호도 저장 함수
export const saveUserPreferences = async (user_id: string, preferences: object) => {
  try {
    console.log("Sending preferences data:", { user_id: user_id, preferences });  // 로그 추가
    // 선호도 전송
    const response = await axios.post('/user/preferences', {
      user_id: user_id,
      preferences,
    });
    alert("정보가 저장되었습니다!");
    return response.data;
  } catch (error) {
    console.error("정보 저장 실패", error);
    throw error;
  }
};

// 입맛 정보 저장 함수
export const saveUserTastes = async (user_id: string, tastes: {
  sweet: number;
  salty: number;
  spicy: number;
  sour: number;
  umami: number;
}) => {
  try {
    console.log("Sending taste data:", { user_id: user_id, tastes });  
    // 입맛 정보 전송
    const response = await axios.post('/user/tastes', {
      user_id: user_id,
      tastes, // tastes 객체를 그대로 전송
      is_info_complete: true,
    });
    alert("입맛 정보가 저장되었습니다!");
    return response.data;
  } catch (error) {
    console.error("입맛 정보 저장 실패", error);
    throw error;
  }
};

