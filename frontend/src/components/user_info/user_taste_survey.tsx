// src/components/user_info/user_taste_survey.tsx
import React, { useState } from 'react';

interface UserTasteSurveyProps {
  onSubmit: (tastes: {
    sweet: number;
    salty: number;
    spicy: number;
    sour: number;
    umami: number;
  }) => void;
}

const UserTasteSurvey: React.FC<UserTasteSurveyProps> = ({ onSubmit }) => {
  const [tastes, setTastes] = useState({
    sweet: 0,
    salty: 0,
    spicy: 0,
    sour: 0,
    umami: 0,
  });

  const handleChange = (taste: keyof typeof tastes, value: number) => {
    setTastes(prev => ({ ...prev, [taste]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(tastes);
  };

  return (
    <form onSubmit={handleSubmit}>
      {Object.keys(tastes).map((key) => (
        <label key={key}>
          {key} 선호도:
          <select
            value={tastes[key as keyof typeof tastes]}
            onChange={(e) => handleChange(key as keyof typeof tastes, parseFloat(e.target.value))}
          >
            <option value={0}>전혀 선호하지 않음 (0)</option>
            <option value={0.25}>약간 선호 (0.25)</option>
            <option value={0.5}>보통 (0.5)</option>
            <option value={0.75}>선호 (0.75)</option>
            <option value={1}>매우 선호 (1)</option>
          </select>
        </label>
      ))}
      <button type="submit">완료</button>
    </form>
  );
};

export default UserTasteSurvey;