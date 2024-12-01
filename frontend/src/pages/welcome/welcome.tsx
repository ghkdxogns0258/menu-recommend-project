// src/pages/welcome/welcome.tsx
import React from 'react';
import { useRouter } from 'next/router';
import styles from './welcome.module.css'; // 기존 스타일 유지

interface WelcomePageProps {
    onStartClick: () => void;
  }

const WelcomePage: React.FC<WelcomePageProps> = ({ onStartClick }) => {
  const router = useRouter();

  const handleStartClick = () => {
    router.push('/auth/auth'); // 클릭 시 인증 페이지로 이동
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Today's Eat</h1>
      <p className={styles.subtitle}>오늘...뭐먹지?</p>
      <button className={styles.button} onClick={handleStartClick}>
        <span role="img" aria-label="yum" className={styles.emoji}>
          😋
        </span>
        <span className={styles.buttonText}>Click!</span>
      </button>
    </div>
  );
};

export default WelcomePage;
