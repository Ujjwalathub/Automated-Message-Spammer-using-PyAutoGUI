# Pet Spammer Bot 🐾

This is a simple Python script that simulates keyboard input to repeatedly send randomized pet-related messages like "You are a dog", "You are a cat", etc. It uses the `pyautogui` library to simulate keystrokes.

## 📋 Features

- Randomly selects from a list of pets (`parrot`, `dog`, `cat`, `rabbit`)
- Types "You are a `<pet>`" and presses Enter
- Repeats this process 5000 times
- Waits 8 seconds before starting (to allow switching to the target input field)

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- `pyautogui` installed

You can install `pyautogui` with:

```bash
pip install pyautogui
