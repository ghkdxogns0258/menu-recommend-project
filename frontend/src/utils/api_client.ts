// utils/apiClient.ts
import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_BACKEND_URL, // 백엔드 URL을 환경 변수에서 가져옴
  
  withCredentials: true, // CORS 요청에 자격 증명 포함 (예: 세션 쿠키)
  headers: {
    'Content-Type': 'application/json', // 기본 Content-Type 설정
  },
});
export default apiClient;
