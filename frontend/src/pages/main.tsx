import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import FeedbackButtons from '../components/UI/feedback_buttons';
import { getMenuRecommendation, sendFeedback } from '../utils/menu_api';
import { getUserIdFromDatabase } from '../utils/db_api'; // DB에서 유저 ID 가져오기
import { resetUserModel } from '../utils/reset_api';
import Layout from '../app/layout'; // 공통 레이아웃 경로

const MainPage: React.FC = () => {
    const [recommendedMenu, setRecommendedMenu] = useState<string | null>(null);
    const [user_id, setuser_id] = useState<string | null>(null); // 사용자 ID 상태 추가
    const router = useRouter();

    // DB에서 유저 ID 가져오고 추천 메뉴 호출
    const fetchRecommendedMenu = async () => {
        try {
            const user_idFromDb = await getUserIdFromDatabase();
            console.log("유저 ID:", user_idFromDb); // 유저 ID 확인
            if (!user_idFromDb) {
                return;
            }
    
            setuser_id(user_idFromDb);
    
            // 추천 메뉴 API 호출
            const menu = await getMenuRecommendation(user_idFromDb);
            console.log("추천 메뉴 데이터:", menu); // 추천 메뉴 데이터 확인
            setRecommendedMenu(menu.menu_name); // API 응답의 menu_name 키 사용
        } catch (error) {
            console.error("메뉴 추천 오류:", error);
        }
    };
    
    

    const handleLike = async () => {
        if (recommendedMenu && user_id) {
            try {
                await sendFeedback(recommendedMenu, true, user_id);
                alert(`${recommendedMenu}에 좋아요를 눌렀습니다!`);
                fetchRecommendedMenu(); // 새로운 추천 메뉴 가져오기
            } catch (error) {
                console.error("좋아요 처리 오류:", error);
            }
        }
    };

    const handleDislike = async () => {
        if (recommendedMenu && user_id) {
            try {
                await sendFeedback(recommendedMenu, false, user_id);
                alert(`${recommendedMenu}에 싫어요를 눌렀습니다.`);
                fetchRecommendedMenu(); // 새로운 추천 메뉴 가져오기
            } catch (error) {
                console.error("싫어요 처리 오류:", error);
            }
        }
    };
    const handleResetModel = async () => {
        if (!user_id) {
          alert("사용자 ID가 없습니다. 로그인 후 다시 시도해주세요.");
          return;
        }
      
        try {
          await resetUserModel(user_id); // user_id는 null이 아님이 보장됨
          alert("모델이 초기화되었습니다!");
          fetchRecommendedMenu(); // 초기화 후 메뉴 새로 추천
        } catch (error) {
          console.error("모델 초기화 실패", error);
          alert("모델 초기화에 실패했습니다.");
        }
      };
    useEffect(() => {
        fetchRecommendedMenu();
    }, []);

    return (
        <Layout>
        <div>
            <h1>메인 페이지</h1>
            <pre>추천 상태: {JSON.stringify(recommendedMenu)}</pre>
            <pre>유저 ID: {JSON.stringify(user_id)}</pre>
            {recommendedMenu ? (
                <div>
                    <h2>오늘의 추천 메뉴: {recommendedMenu}</h2>
                    <FeedbackButtons onLike={handleLike} onDislike={handleDislike} />
                </div>
            ) : (
                <p>추천 메뉴를 불러오는 중입니다...</p>
            )}
            <button onClick={handleResetModel} style={{ backgroundColor: 'red', color: 'white' }}>
        모델 초기화
      </button>
        </div>
        </Layout>
    );
    
};

export default MainPage;