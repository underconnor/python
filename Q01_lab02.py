# Q01_lab01.py

import tkinter as tk
from typing import Text

# 창 생성
win = tk.Tk()

#창 설정
win.geometry('300x200+100+100')
win.title('***** TKINTER')

win.resizable(False,False)  # 창 크기 조절 불가

#레이블 설정
lbl_name = tk.Label(win, text='**')
lbl_age = tk.Label(win, text='**')
lbl_school = tk.Label(win, text='**')
lbl_hobby = tk.Label(win, text='**')

# 레이블 출력
lbl_name.pack()
lbl_age.pack()
lbl_school.pack()
lbl_hobby.pack()

#화면 보이기
win.mainloop()


