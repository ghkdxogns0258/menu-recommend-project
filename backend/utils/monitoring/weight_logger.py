import os
import json
import atexit

def save_weights(model, epoch, log_dir="logs/weights"):
    """모델의 가중치를 파일에 저장하는 함수.
    
    Args:
        model: 가중치를 저장할 모델
        epoch (int): 현재 에포크 번호
        log_dir (str): 가중치 저장 디렉토리 경로
    """
    os.makedirs(log_dir, exist_ok=True)
    
    # 모델의 가중치 추출
    weights = {name: param.tolist() for name, param in model.named_parameters()}
    
    # JSON 파일로 저장
    with open(os.path.join(log_dir, f"weights_epoch_{epoch}.json"), "w") as f:
        json.dump(weights, f)

def clear_logs(log_dir="logs/weights"):
    """로그 디렉토리 내의 모든 파일을 삭제하는 함수.
    
    Args:
        log_dir (str): 가중치가 저장된 디렉토리 경로
    """
    if os.path.exists(log_dir):
        for file_name in os.listdir(log_dir):
            file_path = os.path.join(log_dir, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(f"Cleared all weight logs in {log_dir}.")

# 서버 종료 시 clear_logs 함수를 호출하도록 등록
atexit.register(clear_logs)