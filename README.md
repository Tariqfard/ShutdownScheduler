# Shutdown Scheduler

A Python application to schedule your computer to shut down or enter sleep mode after a specified time. This application works on **Windows**, **Linux**, and **macOS** and features a modern dark-themed UI.

## Features
- Input time in minutes for shutdown or sleep mode.
- Choose between **Shutdown** or **Sleep** when the timer ends.
- Cancel ongoing timers with a single click.
- Cross-platform support:
  - **Windows**: Uses `shutdown` and `rundll32`.
  - **Linux**: Uses `shutdown` and `systemctl`.
  - **macOS**: Uses `shutdown` and `pmset`.
- Modern dark-themed UI for a sleek and professional look.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Tariqfard/ShutdownScheduler.git
   cd ShutdownScheduler

2. Install dependencies:
 ```bash
    pip install -r requirements.txt
```
3. Run the app

4. Requirements

    Python 3.7 or later
    customtkinter library (install via pip)
