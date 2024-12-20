# -*- coding: utf-8 -*-
"""Py_pyautogui_이용가이드.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TsHSWYJTdCZi5RnkEETlT308-8SUdP4m

# Pyautogui

참고 : https://jdh5202.tistory.com/905

# Sample1
참고:
"""

from PIL import ImageGrab
from functools import partial
import pyautogui
import time

#화면 저장
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# 이미지 영역의 중앙 부분을 찾아 마우스 이동
char_obj = pyautogui.locateCenterOnScreen('objects/charbar.png',confidence=0.9) // confidence - 이미지 정확도
pyautogui.moveTo(char_obj)
#pyautogui.moveTo(char_obj,1) # 이미지로 이동하는데 1초 걸림

# 키보드 타이핑(0.1초만에)
pyautogui.typewrite('abcd1234!', interval=0.1)

# 마우스 휠 내림
pyautogui.scroll(-1)

# 이미지 찾아서 클릭
pyautogui.click(hero,duration=1)

# 모니터 화면 가운데로 마우스 커서 이동 후 더블클릭
screenCenter = pyautogui.size()
screenCenter = (int(screenCenter[0] / 2), int(screenCenter[1] / 2))
pyautogui.moveTo(screenCenter[0],screenCenter[1] ,1)
pyautogui.doubleClick()
