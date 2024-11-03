import logging
import os

# 로그 파일이 저장될 디렉터리 경로 설정
log_dir = os.path.join(os.path.dirname(__file__), "../../logs")
os.makedirs(log_dir, exist_ok=True)  # 로그 디렉터리 생성 (존재하지 않으면 생성)

# 로깅 기본 설정
logging.basicConfig(
    level=logging.INFO,  # 로깅 레벨 설정
    format="%(asctime)s - %(levelname)s - %(message)s",  # 로깅 메시지 포맷 설정
    handlers=[
        logging.FileHandler(os.path.join(log_dir, "app.log")),  # 로그 파일로 출력
        logging.StreamHandler()  # 콘솔에도 로그 출력
    ]
)

# 로거 인스턴스 생성
logger = logging.getLogger(__name__)
