// src/components/user_info/user_preferences.tsx
import React, { useState } from 'react';

interface UserPreferencesProps {
  onSubmit: (preferences: {
    taste: number;
    value: number;
    health: number;
    cooking: number;
    greasiness: number;
  }) => void;
}

const UserPreferences: React.FC<UserPreferencesProps> = ({ onSubmit }) => {
  const [preferences, setPreferences] = useState({
    taste: 0,
    value: 0,
    health: 0,
    cooking: 0,
    greasiness: 0,
  });

  const handleChange = (field: keyof typeof preferences, value: number) => {
    setPreferences(prev => ({ ...prev, [field]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(preferences);
  };

  return (
    <form onSubmit={handleSubmit}>
      {Object.keys(preferences).map((key) => (
        <label key={key}>
          {key} 중요도:
          <select
            value={preferences[key as keyof typeof preferences]}
            onChange={(e) => handleChange(key as keyof typeof preferences, parseFloat(e.target.value))}
          >
            <option value={0}>전혀 중요하지 않음 (0)</option>
            <option value={0.25}>별로 중요하지 않음 (0.25)</option>
            <option value={0.5}>보통 (0.5)</option>
            <option value={0.75}>중요함 (0.75)</option>
            <option value={1}>매우 중요함 (1)</option>
          </select>
        </label>
      ))}
      <button type="submit">다음으로</button>
    </form>
  );
};

export default UserPreferences;