import time
import pyautogui

pyautogui.PAUSE = 0.2

pyautogui.hotkey("win", "d")
time.sleep(1)

# 修改为网易云音乐图标的实际坐标
pyautogui.doubleClick(1238, 1420, interval=0.15)

time.sleep(5)