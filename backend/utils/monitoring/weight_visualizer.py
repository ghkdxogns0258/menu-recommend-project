import os
import json
import matplotlib.pyplot as plt

def visualize_weights(log_dir: str = "logs/weights"):
    """각 층의 첫 번째 가중치만 시각화하는 함수.

    Args:
        log_dir (str): 가중치가 저장된 디렉토리 경로
    """
    weight_files = sorted([f for f in os.listdir(log_dir) if f.endswith(".json")])

    weight_history = {}
    layer_colors = {
        'fc1': 'blue',
        'fc2': 'green',
        'fc3': 'red',
    }

    # 모든 파일을 순차적으로 로드하여 각 층의 첫 번째 가중치만 기록
    for file_name in weight_files:
        epoch = int(file_name.split('_')[-1].split('.')[0])
        with open(os.path.join(log_dir, file_name), "r") as f:
            weights = json.load(f)

        # 각 레이어에서 첫 번째 가중치 하나만 기록
        for layer_name in ['fc1', 'fc2', 'fc3']:
            weight_key = f"{layer_name}.weight"
            if weight_key in weights:
                # 첫 번째 값만 선택
                first_weight_value = weights[weight_key][0] if isinstance(weights[weight_key], list) else weights[weight_key]
                label_name = f"{layer_name}.weight_first"

                if label_name not in weight_history:
                    weight_history[label_name] = []
                weight_history[label_name].append((epoch, first_weight_value))

    # 각 층의 첫 번째 가중치만 시각화
    for name, values in weight_history.items():
        epochs, weight_values = zip(*values)
        color = layer_colors.get(name.split('.')[0], 'black')
        plt.plot(epochs, weight_values, label=name, color=color, linewidth=1.5)

    plt.xlabel("Epoch")
    plt.ylabel("Weight Value (First Weights)")
    plt.title("Weight Changes of Selected Weights During Training")
    plt.legend(loc="upper right")
    plt.show()