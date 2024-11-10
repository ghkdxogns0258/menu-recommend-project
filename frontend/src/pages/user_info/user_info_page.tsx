// src/pages/user_info_page.tsx
import React from 'react';
import UserPreferences from '../../components/user_info/user_preferences';
import UserTasteSurvey from '../../components/user_info/user_taste_survey';
import { saveUserPreferences, saveUserTastes } from '../../utils/user_utils';

const UserInfoPage = () => {
  const handleRegisterSubmit = async (preferences: {
    taste: boolean;
    value: boolean;
    health: boolean;
    cooking: boolean;
    greasiness: boolean;
  }) => {
    await saveUserPreferences(preferences); // 데이터 전송 로직은 utils에서 처리
  };

  const handleTasteSubmit = async (tastes: string[]) => {
    await saveUserTastes(tastes); // 데이터 전송 로직은 utils에서 처리
  };

  return (
    <div>
      <UserPreferences onSubmit={handleRegisterSubmit} />
      <UserTasteSurvey onSubmit={handleTasteSubmit} />
    </div>
  );
};

export default UserInfoPage;