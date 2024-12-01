// src/app/layout.tsx
import Footer from '../components/footer/footer'; // 푸터 컴포넌트 경로
import Header from '../components/header/header'; // 헤더 컴포넌트 경로
import './layout.css'

const Layout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="layout">
      <Header />
      <main className="content">{children}</main>
      <Footer />
    </div>
  );
};

export default Layout;
