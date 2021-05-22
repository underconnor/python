#Q02_lab01.py

import tkinter as tk

#창 생성하기
win = tk.Tk()
win.geometry('300x200')
win.title('회사소개')

#레이블 만들기
lbl_name = tk.Label(win, text='회사명 : *****',fg='black',bg ='yellow',padx=3, pady=3)
lbl_location = tk.Label(win, text='회사주소 : ****** *****',fg='black',bg ='yellow',padx=3, pady=3)
lbl_mail = tk.Label(win, text='회사메일: *********@gmail.com',fg='red',bg ='orange',padx=3, pady=3)
lbl_phone = tk.Label(win, text='연락처: **********',fg='red',bg ='orange',padx=3, pady=3)

#레이블 출력하기
lbl_name.pack()
lbl_location.pack()
lbl_mail.pack()
lbl_phone.pack()

#창 보이기
win.mainloop()