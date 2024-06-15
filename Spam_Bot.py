import pyautogui as pg
import time

time.sleep(5)

message = """
    
"""

for i in range(10):
    pg.write(message)
    pg.press("Enter")
