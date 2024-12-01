// src/pages/completion.tsx
import React from 'react';
import { useRouter } from 'next/router';
import './completion.css'; 

const CompletionPage: React.FC = () => {
  const router = useRouter();

  const handleStartClick = () => {
    router.push('/main');
  };

  return (
    <div className="completion-container">
      <h2 className="completion-title">감사합니다!</h2>
      <p className="completion-text">이제 모든 준비가 끝났습니다. 즐거운 식사 되세요!</p>
      <button className="completion-button" onClick={handleStartClick}>
        시작하기
      </button>
    </div>
  );
};

export default CompletionPage;
