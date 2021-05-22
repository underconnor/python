#Q03_lab01.py

import tkinter as tk

def quit():
    win.quit()
    
    

#창 생성
win = tk.Tk()
win.geometry('300x200')
win.title('버튼 위젯 소개')

# 레이블 생성
lbl_button = tk.Label(win, text='종료 버튼을 누르면 창을 종료합니다.', fg='yellow', bg='black')

#버튼 생성
btn_quit = tk.Button(win, text='종료', command=quit, width=10, height=3)

#pack
lbl_button.pack()
btn_quit.pack()

#보이기
win.mainloop()