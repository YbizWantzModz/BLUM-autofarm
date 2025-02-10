import requests

CLOUD_ACCOUNTS_URL = "https://example.com/blum_accounts.json"  # Замените на реальный URL

def get_accounts():
    try:
        response = requests.get(CLOUD_ACCOUNTS_URL)
        if response.status_code == 200:
            return response.json().get("accounts", [])
        else:
            print(f"[ERROR] Failed to load accounts. HTTP {response.status_code}")
            return []
    except Exception as e:
        print(f"[ERROR] Could not retrieve accounts: {e}")
        return []
