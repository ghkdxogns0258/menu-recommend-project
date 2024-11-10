// src/components/user_info/user_taste_survey.tsx
import React, { useState } from 'react';

interface UserTasteSurveyProps {
  onSubmit: (tastes: string[]) => void;
}

const UserTasteSurvey: React.FC<UserTasteSurveyProps> = ({ onSubmit }) => {
  const [tastes, setTastes] = useState<string[]>([]);

  const handleCheckboxChange = (taste: string) => {
    setTastes(prevTastes =>
      prevTastes.includes(taste)
        ? prevTastes.filter(t => t !== taste)
        : [...prevTastes, taste]
    );
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(tastes);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label><input type="checkbox" onChange={() => handleCheckboxChange('sweet')} /> 단맛</label>
      <label><input type="checkbox" onChange={() => handleCheckboxChange('salty')} /> 짠맛</label>
      <label><input type="checkbox" onChange={() => handleCheckboxChange('spicy')} /> 매운맛</label>
      <label><input type="checkbox" onChange={() => handleCheckboxChange('sour')} /> 신맛</label>
      <label><input type="checkbox" onChange={() => handleCheckboxChange('umami')} /> 감칠맛</label>
      <button type="submit">완료</button>
    </form>
  );
};

export default UserTasteSurvey;