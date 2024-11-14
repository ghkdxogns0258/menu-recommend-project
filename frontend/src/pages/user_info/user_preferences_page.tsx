// src/pages/user_preferences_page.tsx
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import UserPreferences from '../../components/user_info/user_preferences';
import { saveUserPreferences } from '../../utils/user_utils';

const UserPreferencesPage = () => {
  const router = useRouter();
  const [userId, setUserId] = useState<string | null>(null);

  useEffect(() => {
    const storedUserId = sessionStorage.getItem('user_id');
    console.log("Fetched userId from sessionStorage:", storedUserId); // 디버깅용
    if (storedUserId) {
      setUserId(storedUserId);
    } else {
      alert("로그인 정보가 없습니다.");
      router.push('/login'); // 로그인 페이지로 리다이렉트
    }
  }, []);

  const handlePreferencesSubmit = async (preferences: {
    taste: number;
    value: number;
    health: number;
    cooking: number;
    greasiness: number;
  }) => {
    if (userId) {
      await saveUserPreferences(userId, preferences);
      router.push('/user_info/user_taste_survey_page');
    } else {
      alert("페이지 이동 실패.");
    }
  };

  return (
    <div>
      <UserPreferences onSubmit={handlePreferencesSubmit} />
    </div>
  );
};

export default UserPreferencesPage;