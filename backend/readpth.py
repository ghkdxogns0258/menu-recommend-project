import torch

# 가중치 파일 로드
weights_path = "logs/weights/user_1_weights.pth"
checkpoint = torch.load(weights_path)

# 저장된 모델의 가중치와 편향 출력
print("Model weights and biases:")
for name, param in checkpoint['model_state_dict'].items():
    print(f"{name}: {param}")

# 옵티마이저 상태 확인 (optional)
if 'optimizer_state_dict' in checkpoint:
    print("\nOptimizer state:")
    for key, value in checkpoint['optimizer_state_dict'].items():
        print(f"{key}: {value}")

# 에폭 정보 출력
if 'epoch' in checkpoint:
    print(f"\nSaved epoch: {checkpoint['epoch']}")