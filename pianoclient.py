from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(350, 400)[0] == 0:
        click(350, 400)
    if pyautogui.pixel(436, 400)[0] == 0:
        click(436, 400)
    if pyautogui.pixel(530, 400)[0] == 0:
        click(530, 400)
    if pyautogui.pixel(560, 400)[0] == 0:
        click(560, 400)
