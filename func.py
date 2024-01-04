from datetime import datetime
import json

chat_message = "mock_data.json"

def format_message(username, message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    return (f"{timestamp} username:{username} message:{message}")

def load_messages():
    try:
        with open(chat_message, 'r') as file:
            messages = json.load(file)
        return messages
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_messages(messages):
    with open(chat_message, 'w') as file:
        json.dump(messages, file, indent=2)