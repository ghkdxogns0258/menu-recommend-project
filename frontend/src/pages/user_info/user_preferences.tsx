// src/pages/user_preferences.tsx
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import './user_form.css';
import { saveUserPreferences } from '../../utils/user_utils';

const UserPreferencesPage = () => {
  const router = useRouter();
  const [user_id, setUserId] = useState<string | null>(null);
  const [preferences, setPreferences] = useState({
    taste: 0,
    value: 0,
    health: 0,
    cooking: 0,
    greasiness: 0,
  });

  useEffect(() => {
    const storedUserId = sessionStorage.getItem('user_id');
    if (storedUserId) {
      setUserId(storedUserId);
    } else {
      alert("로그인 정보가 없습니다.");
      router.push('/login');
    }
  }, []);

  const handleChange = (field: keyof typeof preferences, value: number) => {
    setPreferences((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (user_id) {
      await saveUserPreferences(user_id, preferences);
      router.push('/user_info/user_taste_survey');
    } else {
      alert("페이지 이동 실패.");
    }
  };

  const preferenceLabels: Record<keyof typeof preferences, string> = {
    taste: '맛',
    value: '가성비',
    health: '건강',
    cooking: '조리시간',
    greasiness: '느끼함',
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} className="form">
        {Object.keys(preferences).map((key) => (
          <label key={key} className="form-label">
            {preferenceLabels[key as keyof typeof preferences]} 중요도:
            <select
              value={preferences[key as keyof typeof preferences]}
              onChange={(e) => handleChange(key as keyof typeof preferences, parseFloat(e.target.value))}
              className="form-select"
            >
              <option value={0}>전혀 중요하지 않음</option>
              <option value={0.25}>별로 중요하지 않음</option>
              <option value={0.5}>보통</option>
              <option value={0.75}>중요함</option>
              <option value={1}>매우 중요함</option>
            </select>
          </label>
        ))}
        <button type="submit" className="form-button">다음으로</button>
      </form>
    </div>
  );
};


export default UserPreferencesPage;
