import React from 'react';
import { FiUser } from 'react-icons/fi'; // 사용자 아이콘
import './header.css'; // 스타일 파일

const Header = () => {
  return (
    <header className="header">
      <div className="header-icon">😋 투잇!</div>
      <div className="header-menu">
        <button className="header-button">
          <FiUser size={24} className="user-icon" />
        </button>
      </div>
    </header>
  );
};

export default Header;
