import platform
import subprocess


def show_notification(title, message):
    if platform.system() == "Linux":
        subprocess.run(["notify-send", title, message])
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(
            [
                "osascript",
                "-e",
                f'display notification "{message}" with title "{title}"',
            ]
        )
    # Windows notifications can be added here if needed


def play_sound(sound_type="start"):
    sound_files = {
        "start": "sounds/start.wav",
        "short_break": "sounds/short_break.wav",
        "long_break": "sounds/long_break.wav",
    }
    sound_file = sound_files.get(sound_type, sound_files["start"])

    if platform.system() == "Linux":
        subprocess.run(["aplay", sound_file])
