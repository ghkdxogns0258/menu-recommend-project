import React from 'react';
import './login_sign_up.css';

const LoginSignUp: React.FC = () => {
  // OAuth 로그인 함수
  const handleOAuthLogin = (provider: string) => {
    window.location.href = `${process.env.REACT_APP_BACKEND_URL}/login/${provider}`;
  };

  return (
    <div className="wrapper">
      <div className="container">
        <h1>Sign In / Sign Up</h1>
        <div className="social-links">
          <div><button onClick={() => handleOAuthLogin('kakao')}><i className="fa fa-kakao" aria-hidden="true"></i> Kakao</button></div>
          <div><button onClick={() => handleOAuthLogin('google')}><i className="fa fa-google" aria-hidden="true"></i> Google</button></div>
          <div><button onClick={() => handleOAuthLogin('naver')}><i className="fa fa-naver" aria-hidden="true"></i> Naver</button></div>
        </div>
      </div>
    </div>
  );
};

export default LoginSignUp;