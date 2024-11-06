import json

DEFAULT_SETTINGS = {
    "pomodoro_duration": 25,
    "short_break_duration": 5,
    "long_break_duration": 15,
    "sessions_before_long_break": 4,
}


def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Create a default settings file if it doesn't exist
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS


def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)
