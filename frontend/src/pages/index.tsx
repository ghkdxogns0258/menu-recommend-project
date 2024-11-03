// src/pages/index.tsx
import { useEffect, useState } from 'react';
import { fetchMenuData, sendFeedback, Menu } from '../utils/menu_utils';
import MenuDisplay from '../components/menu_display';
import FeedbackButtons from '../components/feedback_buttons';

const HomePage: React.FC = () => {
    const [menu, setMenu] = useState<Menu | null>(null);

    // 메뉴 데이터 로드
    const loadMenu = async () => {
        const data = await fetchMenuData();
        setMenu(data);
    };

    // 좋아요 버튼 클릭 시 실행되는 함수
    const handleLike = async () => {
        if (menu) {
            await sendFeedback(menu.name, true); // 좋아요 피드백 전송
            loadMenu(); // 새로운 메뉴 불러오기
        }
    };

    // 싫어요 버튼 클릭 시 실행되는 함수
    const handleDislike = async () => {
        if (menu) {
            await sendFeedback(menu.name, false); // 싫어요 피드백 전송
            loadMenu(); // 새로운 메뉴 불러오기
        }
    };

    // 페이지 로드 시 메뉴 데이터를 처음 한 번 불러옴
    useEffect(() => {
        loadMenu();
    }, []);

    return (
        <div>
            <MenuDisplay menu={menu} />
            <FeedbackButtons onLike={handleLike} onDislike={handleDislike} />
        </div>
    );
};

export default HomePage;