// src/pages/index.tsx
import React from 'react';
import { useRouter } from 'next/router';

const IndexPage: React.FC = () => {
    const router = useRouter();

    const handleStartClick = () => {
        router.push('/auth/auth_pages'); // auth 페이지로 이동
    };

    return (
        <div>
            <h2>환영합니다!</h2>
            <p>시작하려면 버튼을 클릭하세요.</p>
            <button onClick={handleStartClick}>시작하기</button>
        </div>
    );
};

export default IndexPage;