import axios from 'axios';

export const sendFeedback = async (menuName: string, liked: boolean) => {
  try {
    const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/feedback`, { menuName, liked });
    return response.data;
  } catch (error) {
    console.error("피드백 전송 실패", error);
    throw error;
  }
};