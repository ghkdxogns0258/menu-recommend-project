import os
import torch
from threading import Lock
from torch import optim
from model.recommendation_model import MenuRecommendationNet
from utils.training.file_manager import get_weights_path

class ModelManager:
    """
    사용자별 모델 및 옵티마이저 상태를 관리하는 클래스.
    - 캐싱 및 파일 락을 통해 효율성과 동시성을 개선.
    """
    def __init__(self, input_size, num_menus):
        self.models = {}  # 사용자별 모델 캐시
        self.optimizers = {}  # 사용자별 옵티마이저 캐시
        self.locks = {}  # 사용자별 파일 락
        self.input_size = input_size
        self.num_menus = num_menus

    def get_model(self, user_id):
        """
        사용자별 모델을 반환. 캐싱된 모델이 없으면 로드.
        """
        if user_id not in self.models:
            self.models[user_id] = self._load_model(user_id)
        return self.models[user_id]

    def _load_model(self, user_id):
        """
        모델 상태를 파일에서 로드하거나 초기화.
        """
        model = MenuRecommendationNet(input_size=self.input_size, num_menus=self.num_menus)
        weights_path = get_weights_path(user_id)

        if os.path.exists(weights_path):
            checkpoint = torch.load(weights_path)
            model.load_state_dict(checkpoint["model_state_dict"])
            print(f"Loaded model for user {user_id} from {weights_path}")
        else:
            print(f"No saved model for user {user_id}. Using initialized model.")

        return model

    def save_model(self, user_id, model, optimizer=None, epoch=0):
        """
        사용자별 모델 및 옵티마이저 상태를 저장.
        """
        weights_path = get_weights_path(user_id)
        checkpoint = {
            "model_state_dict": model.state_dict(),
            "epoch": epoch,
        }
        if optimizer is not None:
            checkpoint["optimizer_state_dict"] = optimizer.state_dict()
        os.makedirs(os.path.dirname(weights_path), exist_ok=True)
        torch.save(checkpoint, weights_path)
        print(f"Saved model for user {user_id} at {weights_path}")

    def get_optimizer(self, user_id):
        """
        사용자별 옵티마이저를 반환. 캐싱된 옵티마이저가 없으면 생성.
        """
        if user_id not in self.optimizers:
            self.optimizers[user_id] = self._create_optimizer(user_id)
        return self.optimizers[user_id]

    def _create_optimizer(self, user_id):
        """
        옵티마이저 생성 (Adam 옵티마이저 사용)
        """
        model = self.get_model(user_id)
        optimizer = optim.Adam(model.parameters(), lr=0.01)  # 기본 학습률 0.01
        print(f"Created new optimizer for user {user_id}")
        return optimizer

    def get_lock(self, user_id):
        """
        사용자별 파일 락 반환.
        """
        if user_id not in self.locks:
            self.locks[user_id] = Lock()
        return self.locks[user_id]
    def has_saved_model(self, user_id):
        """
        사용자의 저장된 모델 상태가 있는지 확인.
        """
        weights_path = get_weights_path(user_id)
        return os.path.exists(weights_path)
    def get_epoch(self, user_id):
        """
        사용자별 저장된 epoch 값을 반환. 저장된 모델이 없으면 0 반환.
        """
        weights_path = get_weights_path(user_id)
        if os.path.exists(weights_path):
            checkpoint = torch.load(weights_path)
            return checkpoint.get("epoch", 0)  # 저장된 epoch 값 반환 (기본값: 0)
        return 0  # 저장된 모델이 없으면 0 반환
