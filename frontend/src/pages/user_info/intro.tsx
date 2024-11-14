// pages/user_info/intro.tsx
import React from 'react';
import { useRouter } from 'next/router';
import { useEffect } from 'react';

const IntroPage = () => {
  const router = useRouter();

  useEffect(() => {
    const { user_id } = router.query;

    if (user_id) {
      sessionStorage.setItem('user_id', user_id as string);
      console.log("User ID stored in sessionStorage:", user_id);
    }
  }, [router.query]);

  const handleNextClick = () => {
    router.push('/user_info/user_preferences_page'); 
  };

  return (
    <div>
      <h2>어서오세요!</h2>
      <p>
        투잇(Today’s Eat)은 사용자님의 입맛을 기억하고, 추천 메뉴에 대한 피드백을 통해
        점점 더 맞춤형 메뉴를 제공하는 인공지능입니다.
      </p>
      <p>
        매일의 식사 고민을 덜어 드리며, 더욱 만족스러운 식사 경험을 만들어 드릴게요.
      </p>
      <p>우선, 사용자님에 대해 알고 싶어요!</p>
      <button onClick={handleNextClick}>다음으로</button>
    </div>
  );
};

export default IntroPage;
