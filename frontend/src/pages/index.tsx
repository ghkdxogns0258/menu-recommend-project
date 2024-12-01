// src/pages/index.tsx
import React, { useEffect } from 'react';
import { useRouter } from 'next/router';
import WelcomePage from '../pages/welcome/welcome';

const IndexPage: React.FC = () => {
  const router = useRouter();

  useEffect(() => {
    // `user_id`가 세션에 저장되어 있는지 확인하고 저장
    fetch('/get-session-user-id')
      .then(response => response.json())
      .then(data => {
        if (data.user_id) {
          sessionStorage.setItem('user_id', data.user_id);
        }
      });
  }, []);

  const handleStartClick = () => {
    router.push('/auth/auth');
  };

  return <WelcomePage onStartClick={handleStartClick} />;
};

export default IndexPage;