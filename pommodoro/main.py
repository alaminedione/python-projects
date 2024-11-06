import time
import tkinter as tk

from notifications import play_sound, show_notification
from settings import load_settings, save_settings


class PomodoroApp:
    def __init__(self, root):
        self.settings = load_settings()
        self.pomodoro_duration = self.settings["pomodoro_duration"] * 60
        self.short_break_duration = self.settings["short_break_duration"] * 60
        self.long_break_duration = self.settings["long_break_duration"] * 60
        self.sessions_before_long_break = self.settings["sessions_before_long_break"]

        self.time_left = self.pomodoro_duration
        self.session_count = 0
        self.running = False
        self.on_break = False

        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x400")
        self.root.configure(bg="#1e1e2f")

        self.title_label = tk.Label(
            root,
            text="Focus Time",
            font=("JetBrains Mono", 18, "bold"),
            bg="#1e1e2f",
            fg="#FF6E6E",
        )
        self.title_label.pack(pady=20)

        self.timer_label = tk.Label(
            root,
            text="Work Session",
            font=("JetBrains Mono", 14),
            bg="#1e1e2f",
            fg="#FF9F45",
        )
        self.timer_label.pack()

        self.session_tracker = tk.Label(
            root,
            text=f"Session: {self.session_count}/{self.sessions_before_long_break}",
            font=("JetBrains Mono", 10),
            bg="#1e1e2f",
            fg="white",
        )
        self.session_tracker.pack(pady=10)

        self.time_display = tk.Label(
            root,
            text=self.format_time(self.time_left),
            font=("JetBrains Mono", 36),
            bg="#1e1e2f",
            fg="white",
        )
        self.time_display.pack(pady=20)

        button_frame = tk.Frame(root, bg="#1e1e2f")
        button_frame.pack(pady=10)

        self.start_button = tk.Button(
            button_frame,
            text="Start",
            command=self.start_timer,
            font=("JetBrains Mono", 12),
            bg="#FF6E6E",
            fg="white",
            width=8,
        )
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(
            button_frame,
            text="Pause",
            command=self.pause_timer,
            font=("JetBrains Mono", 12),
            bg="#FF6E6E",
            fg="white",
            width=8,
        )
        self.pause_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_timer,
            font=("JetBrains Mono", 12),
            bg="#FF6E6E",
            fg="white",
            width=8,
        )
        self.reset_button.grid(row=0, column=2, padx=5)

        self.settings_button = tk.Button(
            root,
            text="Settings",
            command=self.open_settings,
            font=("JetBrains Mono", 12),
            bg="#FF9F45",
            fg="white",
            width=12,
        )
        self.settings_button.pack(pady=20)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def start_timer(self):
        if not self.running:
            self.running = True
            self.countdown()
            self.title_label.config(text="Focus Time", fg="#FF6E6E")
            show_notification("Focus Time", "Time to focus!")
            play_sound("start")

    def pause_timer(self):
        self.running = False
        self.title_label.config(text="Paused", fg="#FF6E6E")
        show_notification("Paused", "Timer paused")

    def reset_timer(self):
        self.running = False
        self.time_left = (
            self.pomodoro_duration if not self.on_break else self.short_break_duration
        )
        self.time_display.config(text=self.format_time(self.time_left))
        self.session_tracker.config(
            text=f"Session: {self.session_count}/{self.sessions_before_long_break}"
        )

    def countdown(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.time_display.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.countdown)
        elif self.time_left == 0:
            self.switch_session()

    def switch_session(self):
        if not self.on_break:
            self.session_count += 1
            if self.session_count >= self.sessions_before_long_break:
                self.time_left = self.long_break_duration
                self.session_count = 0
                show_notification("Break", "Time for a long break!")
                play_sound("long_break")
            else:
                self.time_left = self.short_break_duration
                show_notification("Break", "Time for a short break!")
                play_sound("short_break")
            self.on_break = True
            self.title_label.config(text="Break Time", fg="#4ECCA3")
            self.timer_label.config(text="Break Session", fg="#4ECCA3")
        else:
            self.time_left = self.pomodoro_duration
            self.on_break = False
            self.title_label.config(text="Focus Time", fg="#FF6E6E")
            self.timer_label.config(text="Work Session", fg="#FF9F45")
            show_notification("Work", "Time to focus!")
            play_sound("start")
        self.session_tracker.config(
            text=f"Session: {self.session_count}/{self.sessions_before_long_break}"
        )
        self.time_display.config(text=self.format_time(self.time_left))
        self.start_timer()

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("250x200")
        settings_window.configure(bg="#2d2d44")

        labels = [
            "Pomodoro Duration (min):",
            "Short Break (min):",
            "Long Break (min):",
            "Sessions Before Long Break:",
        ]
        keys = [
            "pomodoro_duration",
            "short_break_duration",
            "long_break_duration",
            "sessions_before_long_break",
        ]
        entries = {}

        for i, label_text in enumerate(labels):
            tk.Label(
                settings_window,
                text=label_text,
                font=("JetBrains Mono", 10),
                bg="#2d2d44",
                fg="white",
            ).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(settings_window, font=("JetBrains Mono", 10), width=5)
            entry.insert(0, str(self.settings[keys[i]]))
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[keys[i]] = entry

        def save_new_settings():
            for key in keys:
                self.settings[key] = int(entries[key].get())
            save_settings(self.settings)
            settings_window.destroy()
            self.reset_timer()  # Reset timer to apply new settings

        save_button = tk.Button(
            settings_window,
            text="Save",
            command=save_new_settings,
            font=("JetBrains Mono", 10),
            bg="#FF6E6E",
            fg="white",
        )
        save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)


# Run the application
root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()
