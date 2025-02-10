import time
import random
import keyboard
import pyautogui
from cloud import get_accounts
from stats import FarmStats

# Настройки
CLICK_INTERVAL = 3  # Интервал между кликами (в секундах)

# Инициализация статистики
stats = FarmStats()

def random_offset():
    return random.randint(-5, 5), random.randint(-5, 5)

def auto_farm():
    print("[INFO] Blum AutoFarm started. Press 'q' to stop.")
    
    accounts = get_accounts()
    if not accounts:
        print("[ERROR] No accounts loaded from the cloud.")
        return
    
    while not keyboard.is_pressed('q'):
        x, y = pyautogui.position()
        x_offset, y_offset = random_offset()
        pyautogui.moveTo(x + x_offset, y + y_offset, duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        stats.increment_clicks()
        print(f"[INFO] Clicked at ({x + x_offset}, {y + y_offset}) - Total clicks: {stats.get_clicks()}")
        time.sleep(CLICK_INTERVAL + random.uniform(-0.5, 0.5))
    
    print("[INFO] Blum AutoFarm stopped.")

if __name__ == "__main__":
    auto_farm()
