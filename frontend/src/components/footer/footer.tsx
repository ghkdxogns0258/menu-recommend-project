'use client';

import React from 'react';
import { FiSearch, FiHeart, FiCompass, FiStar, FiBook } from 'react-icons/fi';
import './footer.css';

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <div className="footer-line">
        <div className="footer-icon footer-icon-large">
          <FiCompass size={42} title="추천받기" />
          <span className="icon-label">추천받기</span>
        </div>
      </div>
      <div className="footer-icons">
        <div className="footer-icon">
          <FiSearch size={24} title="검색" />
          <span className="icon-label">검색</span>
        </div>
        <div className="footer-icon">
          <FiHeart size={24} title="입맛" />
          <span className="icon-label">입맛</span>
        </div>
        <div className="footer-icon">
          <FiStar size={24} title="선호" />
          <span className="icon-label">선호</span>
        </div>
        <div className="footer-icon">
          <FiBook size={24} title="기록" />
          <span className="icon-label">기록</span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
