import time

import pyautogui

INTERVAL_IN_SECONDS = 60 * 1

while True:
    time.sleep(INTERVAL_IN_SECONDS)
    pyautogui.move(0, -1)   # move up one pixel
    pyautogui.move(0, 1)    # cowardly move back
