export const loginWithOAuth = (provider: string) => {
    // OAuth 로그인 URL을 설정하여 사용자를 해당 URL로 리다이렉트
    window.location.href = `${process.env.REACT_APP_BACKEND_URL}/login/${provider}`;
  };  