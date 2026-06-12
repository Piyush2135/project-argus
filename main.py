import time
import pyautogui
import win32gui
import os

SAVE_FILE = "capture.png"
TEMP_FILE = "capture_tmp.png"

# 0.08 = ~12.5 FPS (good balance)
INTERVAL = 0.08

# Search priority (QUIZ first!)
WINDOW_KEYWORDS = [
    "QUIZ",
    "scrcpy",
    "Xiaomi",
    "POCO",
    "Android"
]


def find_window():
    result = []

    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)

            for key in WINDOW_KEYWORDS:
                if key.lower() in title.lower():
                    result.append((hwnd, title))
                    break

        return True

    win32gui.EnumWindows(callback, None)

    # Return the first valid match
    if result:
        return result[0][0], result[0][1]

    return None, None


print("Searching for QUIZ/scrcpy window...")

hwnd = None
title = None
last_find = 0

while True:
    try:
        now = time.time()

        # Re-find window every 3 seconds only
        if hwnd is None or (now - last_find > 3):
            hwnd, title = find_window()
            last_find = now

            if hwnd:
                print(f"Connected to: {title}")
            else:
                print("Window not found...")
                time.sleep(0.5)
                continue

        # Get current coordinates
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)

        width = right - left
        height = bottom - top

        # Skip invalid dimensions
        if width <= 20 or height <= 20:
            hwnd = None
            continue

        # Capture screenshot
        img = pyautogui.screenshot(
            region=(left, top, width, height)
        )

        # Save atomically (prevents OCR reading half-written file)
        img.save(TEMP_FILE)
        os.replace(TEMP_FILE, SAVE_FILE)

        # DO NOT print every frame
        time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\nStopped.")
        break

    except Exception:
        # If window disappears, try to find it again
        hwnd = None
        time.sleep(0.2)