import os
from utils.logging.logger import logger

def clear_weight_logs(log_dir="logs/weights"):
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                logger.info(f"Deleted weight log file: {filename}")
        except Exception as e:
            logger.error(f"Failed to delete {filename}. Reason: {e}")
