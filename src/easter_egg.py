import keyboard
import ctypes
import threading


class EasterEgg:
# 경고 창을 띄우는 함수
    def show_warning(self):
        ctypes.windll.user32.MessageBoxW(0, "이스터에그", "경고", 0x00000030)

# 키 입력을 감지하는 함수
    def key_listener(self):
        while True:
            if keyboard.is_pressed('0'):
                self.show_warning()
                break

# 키 입력을 감지하고 경고창을 띄우는 함수
    def track_keys(self):
        while True:
            self.key_listener()  # 키 입력 감지
            # 경고창을 띄우고 빠져나온 후, 다음 입력을 위해 반복