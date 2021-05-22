# Q01_lab01.py

import tkinter as tk

# 창 생성하기
win = tk.Tk()

# 창 설정
win.geometry('500x200')
win.title('Python GUI')

# 메시지 만들기
lbl_msg = tk.Label(win, text='tkinter 패키지는 tkGUI 툴킷에 대한 표준 파이썬 인터페이스이다.')

#메시지 출력하기
lbl_msg.pack()

# 창 보이기
tk.mainloop()