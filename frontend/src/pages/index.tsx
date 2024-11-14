import React, { useEffect } from 'react';
import { useRouter } from 'next/router';

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
    router.push('/auth/auth_pages');
  };

  return (
    <div>
      <h2>환영합니다!</h2>
      <p>시작하려면 버튼을 클릭하세요.</p>
      <button onClick={handleStartClick}>시작하기</button>
    </div>
  );
};

export default IndexPage;