// src/pages/completion_page.tsx
import React from 'react';
import { useRouter } from 'next/router';

const CompletionPage: React.FC = () => {
    const router = useRouter();

    const handleStartClick = () => {
        router.push('/main'); // Next.js 라우터로 메인 페이지로 이동
    };

    return (
        <div>
            <h2>감사합니다!</h2>
            <p>이제 모든 준비가 끝났습니다. 즐거운 식사 되세요!</p>
            <button onClick={handleStartClick}>시작하기</button>
        </div>
    );
};

export default CompletionPage;