// src/pages/user_taste_survey_page.tsx
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import UserTasteSurvey from '../../components/user_info/user_taste_survey';
import { saveUserTastes } from '../../utils/user_utils';

const UserTasteSurveyPage = () => {
  const router = useRouter();
  const [userId, setUserId] = useState<string | null>(null);

  useEffect(() => {
    const storedUserId = sessionStorage.getItem('user_id');
    if (storedUserId) {
      setUserId(storedUserId);
    }
  }, []);

  const handleTasteSubmit = async (tastes: {
    sweet: number;
    salty: number;
    spicy: number;
    sour: number;
    umami: number;
  }) => {
    if (userId) {
      await saveUserTastes(userId, tastes);
      router.push('/user_info/completion_page');
    } else {
      alert("로그인 정보가 없습니다.");
    }
  };

  return (
    <div>
      <UserTasteSurvey onSubmit={handleTasteSubmit} />
    </div>
  );
};

export default UserTasteSurveyPage;