// src/components/user_info/user_preferences.tsx
import React, { useState } from 'react';

interface UserPreferencesProps {
  onSubmit: (preferences: {
    taste: boolean;
    value: boolean;
    health: boolean;
    cooking: boolean;
    greasiness: boolean;
  }) => void;
}

const UserPreferences: React.FC<UserPreferencesProps> = ({ onSubmit }) => {
  const [preferences, setPreferences] = useState({
    taste: false,
    value: false,
    health: false,
    cooking: false,
    greasiness: false,
  });

  const handleChange = (field: keyof typeof preferences) => {
    setPreferences(prev => ({ ...prev, [field]: !prev[field] }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(preferences);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        <input type="checkbox" checked={preferences.taste} onChange={() => handleChange('taste')} />
        맛이 중요해!
      </label>
      <label>
        <input type="checkbox" checked={preferences.value} onChange={() => handleChange('value')} />
        가성비가 중요해!
      </label>
      <label>
        <input type="checkbox" checked={preferences.health} onChange={() => handleChange('health')} />
        건강이 중요해!
      </label>
      <label>
        <input type="checkbox" checked={preferences.cooking} onChange={() => handleChange('cooking')} />
        조리법이 중요해!
      </label>
      <label>
        <input type="checkbox" checked={preferences.greasiness} onChange={() => handleChange('greasiness')} />
        느끼함이 중요해!
      </label>
      <button type="submit">다음으로</button>
    </form>
  );
};

export default UserPreferences;