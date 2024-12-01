// src/pages/user_taste_survey.tsx
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import './user_form.css';
import { saveUserTastes } from '../../utils/user_utils';

const UserTasteSurveyPage = () => {
  const router = useRouter();
  const [user_id, setuser_id] = useState<string | null>(null);
  const [tastes, setTastes] = useState({
    sweet: 0,
    salty: 0,
    spicy: 0,
    sour: 0,
    umami: 0,
  });

  useEffect(() => {
    const storeduser_id = sessionStorage.getItem('user_id');
    if (storeduser_id) {
      setuser_id(storeduser_id);
    }
  }, []);

  const handleChange = (taste: keyof typeof tastes, value: number) => {
    setTastes((prev) => ({ ...prev, [taste]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (user_id) {
      await saveUserTastes(user_id, tastes);
      router.push('/user_info/completion');
    } else {
      alert("로그인 정보가 없습니다.");
    }
  };

  const tasteLabels: Record<keyof typeof tastes, string> = {
    sweet: '단맛',
    salty: '짠맛',
    spicy: '매운맛',
    sour: '신맛',
    umami: '감칠맛',
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} className="form">
        {Object.keys(tastes).map((key) => (
          <label key={key} className="form-label">
            {tasteLabels[key as keyof typeof tastes]} 선호도:
            <select
              value={tastes[key as keyof typeof tastes]}
              onChange={(e) => handleChange(key as keyof typeof tastes, parseFloat(e.target.value))}
              className="form-select"
            >
              <option value={0}>전혀 선호하지 않음</option>
              <option value={0.25}>약간 선호</option>
              <option value={0.5}>보통</option>
              <option value={0.75}>선호</option>
              <option value={1}>매우 선호</option>
            </select>
          </label>
        ))}
        <button type="submit" className="form-button">완료</button>
      </form>
    </div>
  );
};


export default UserTasteSurveyPage;
