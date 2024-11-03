import { Menu } from '../utils/menu_utils';

type MenuDisplayProps = {
    menu: Menu | null;
};

const MenuDisplay: React.FC<MenuDisplayProps> = ({ menu }) => {
    return (
        <div>
            <h1>오늘의 추천 메뉴</h1>
            {menu ? (
                <>
                    <h2>{menu.name}</h2>
                    <p>특징: {menu.features.join(", ")}</p>
                </>
            ) : (
                <p>메뉴를 불러오는 중...</p>
            )}
        </div>
    );
};

export default MenuDisplay;
