
import axios from './apiClient';

export const saveUserPreferences = async (preferences: object) => {
  try {
    const response = await axios.post('/user/preferences', preferences);
    alert("정보가 저장되었습니다!");
    return response.data;
  } catch (error) {
    console.error("정보 저장 실패", error);
    throw error;
  }
};

export const saveUserTastes = async (tastes: string[]) => {
  try {
    const response = await axios.post('/user/tastes', { tastes });
    alert("입맛 정보가 저장되었습니다!");
    return response.data;
  } catch (error) {
    console.error("입맛 정보 저장 실패", error);
    throw error;
  }
};