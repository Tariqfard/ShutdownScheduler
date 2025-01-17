import os
import threading
import time
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# Initialize customtkinter
ctk.set_appearance_mode("dark")  # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("dark-blue")


class ShutdownScheduler(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App Settings
        self.title("Shutdown Scheduler")
        self.geometry("500x400")
        self.resizable(False, False)

        # Timer State
        self.timer_seconds = 0
        self.timer_running = False
        self.timer_thread = None

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Shutdown Scheduler", font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Time Input
        self.time_label = ctk.CTkLabel(self, text="Enter time in minutes:")
        self.time_label.pack(pady=5)

        self.time_entry = ctk.CTkEntry(self, width=200, justify="center", placeholder_text="Minutes")
        self.time_entry.pack(pady=10)

        # Dropdown Menu for Action
        self.action_label = ctk.CTkLabel(self, text="When the timer stops:")
        self.action_label.pack(pady=5)

        self.action_option = ctk.CTkOptionMenu(self, values=["Shutdown", "Sleep"])
        self.action_option.pack(pady=10)

        # Buttons
        self.start_button = ctk.CTkButton(self, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.cancel_timer)
        self.cancel_button.pack(pady=10)

        # Timer Display
        self.timer_label = ctk.CTkLabel(self, text="No task scheduled.", font=("Arial", 18))
        self.timer_label.pack(pady=20)

    def start_timer(self):
        # Get user input
        try:
            minutes = int(self.time_entry.get())
            self.timer_seconds = minutes * 60
            action = self.action_option.get()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for minutes.")
            return

        if self.timer_seconds <= 0:
            messagebox.showerror("Invalid Input", "Time must be greater than zero.")
            return

        # Start Timer
        if not self.timer_running:
            self.timer_running = True
            self.timer_label.configure(text=f"Time Remaining: {minutes} minutes")
            self.timer_thread = threading.Thread(target=self.run_timer, args=(action,))
            self.timer_thread.start()
        else:
            messagebox.showwarning("Timer Running", "A timer is already running. Cancel it first.")

    def run_timer(self, action):
        while self.timer_seconds > 0 and self.timer_running:
            minutes, seconds = divmod(self.timer_seconds, 60)
            self.timer_label.configure(text=f"Time Remaining: {minutes} min {seconds} sec")
            time.sleep(1)
            self.timer_seconds -= 1

        if self.timer_running:
            self.timer_running = False
            self.execute_action(action)

    def execute_action(self, action):
        if action == "Shutdown":
            os.system("shutdown /s /t 0")
        elif action == "Sleep":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        self.timer_label.configure(text="Task completed!")

    def cancel_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.timer_label.configure(text="Task canceled.")
        else:
            messagebox.showinfo("No Task", "No timer is currently running.")


if __name__ == "__main__":
    app = ShutdownScheduler()
    app.mainloop()
