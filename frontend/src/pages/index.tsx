import { useEffect, useState } from 'react';
import axios from 'axios';
import { API_URL } from '../../config/env';

type Menu = {
    menu: string;
    attributes: string[];
};

const HomePage: React.FC = () => {
    const [menu, setMenu] = useState<Menu | null>(null);

    useEffect(() => {
        const fetchMenu = async () => {
            try {
                const response = await axios.get(`${API_URL}/recommend`);
                setMenu(response.data);
            } catch (error) {
                console.error("Failed to fetch menu", error);
            }
        };

        fetchMenu();
    }, []);

    return (
        <div>
            <h1>오늘의 추천 메뉴</h1>
            {menu ? (
                <div>
                    <h2>{menu.menu}</h2>
                    <p>특징: {menu.attributes.join(", ")}</p>
                </div>
            ) : (
                <p>메뉴를 불러오는 중...</p>
            )}
        </div>
    );
};

export default HomePage;
