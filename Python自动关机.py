#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter, os, time, webbrowser
from tkinter import ttk
import tkinter.messagebox as message_box

#window 窗口居中
def center_window(width, height):
    screen_width, screen_height = win.maxsize()
    size = '{}x{}+{}+{}' .format( width, height, int((screen_width - width)/2), int((screen_height - height)/2) )
    win.geometry(size)

#建立window窗口 并限制大小
win = tkinter.Tk()           
win.title("Python定时关机小助手")  #标题
win.update()
center_window(320,240)
win.resizable(0,0)            #限制调整
# win.maxsize(600, 480)       #最大尺寸
# win.minsize(320, 240)       #最小尺寸


#提醒文本
txt1 = tkinter.Label(win, text='设置关机时间:')
txt1.place(x=20, y=25)

txt2 = tkinter.Label(win, text='选择单位:')
txt2.place(x=150, y=25)

txt3 = tkinter.Label(win, text='快捷选项:')
txt3.place(x=20, y=100)



# 存储输入的值
save_time = tkinter.StringVar()
save_unit = tkinter.StringVar()

#输入框
entry_time = tkinter.Entry(win, width=10, textvariable=save_time)
entry_time.place(x=20, y=55)



#下拉菜单选项
menu = ttk.Combobox(win, width=8, textvariable=save_unit)
menu.place(x=150, y=55)
menu['value'] = ('hour', 'minute', 'second') # 设置下拉菜单中的值
menu.current(1)      # 设置默认值




#start按钮参数
def start():
    if save_time.get() and save_unit.get():
        message_box.showwarning("Warning", "你的电脑将在 {} {} 后关机。" .format(save_time.get(), save_unit.get()))
        # shutdown 的秒数
        count_down_second = int(save_time.get())
        if save_unit.get() == 'hour':
            count_down_second *= 3600
        elif save_unit.get() == 'minute':
            count_down_second *= 60
        # execute
        os.system("shutdown -s -t {}" .format(count_down_second))
        win.quit()

#start按钮
start_button = tkinter.Button(win, text='完成', width=6, height=1, command=start)
start_button.place(x=250, y=50)

def change_edit(to_time):
    entry_time.delete(0, 10)
    entry_time.insert(0, to_time)
    menu.current(1)

'''   
#常用的时间按钮
#该按钮需要点击
def shortcut():
    if save_time.get() and save_unit.get():
        message_box.showwarning("Warning", "你的电脑将在 {} {} 后关机。" .format(save_time.get(), save_unit.get()))
        # shutdown 的秒数
        count_down_second = int(save_time.get())
        if save_unit.get() == 'hour':
            count_down_second *= 3600
        elif save_unit.get() == 'minute':
            count_down_second *= 60
        # execute
        os.system("shutdown -s -t {}" .format(count_down_second))
        win.quit()

for i in range(2, 7):
    button = tkinter.Button(win, text=str(i * 15) + "min", command=shortcut)
    button.place(x=60*i-100, y=140)
'''



#快捷按钮       暂时，未用for
def shortcut(num):
    message_box.showwarning("Warning", "你的电脑将在 {} minute 后关机。" .format(num))
    os.system("shutdown -s -t {}" .format(60*num))
    win.quit()

def switch1():         #switch
    shortcut(num = 30)
button = tkinter.Button(win, text='30' + "min", command=switch1)
button.place(x=20, y=140)

def switch2():         
    shortcut(num = 45)
button = tkinter.Button(win, text='45' + "min", command=switch2)
button.place(x=80, y=140)

def switch3():         
    shortcut(num = 60)
button = tkinter.Button(win, text='60' + "min", command=switch3)
button.place(x=140, y=140)

def switch4():         
    shortcut(num = 75)
button = tkinter.Button(win, text='75' + "min", command=switch4)
button.place(x=200, y=140)

def switch5():         
    shortcut(num = 90)
button = tkinter.Button(win, text='90' + "min", command=switch5)
button.place(x=260, y=140)



#取消按钮参数
def cancel():
    os.system("shutdown -a")
    win.quit()

#取消按钮
cancel_button = tkinter.Button(win, text='取消关机', width=8, height=1, command=cancel)
cancel_button.place(x=240, y=85)


# author
link = tkinter.Label(win, text='进入小磊哥的Github')
link.pack(side='bottom')

def open_url(event):
    webbrowser.open("https://github.com/superleige/shutdown", new=0)
 
# 绑定label单击时间
link.bind("<Button-1>", open_url)




#获取系统当前时间
screen_time=tkinter.Label(text=time.strftime('%Y年%m月%d日 %H:%M:%S',time.localtime(time.time())))
screen_time.pack()
def trickit():
    currentTime=time.strftime('%Y年%m月%d日 %H:%M:%S',time.localtime(time.time()))
    screen_time.config(text=currentTime)
    screen_time.after(1000, trickit)
screen_time.after(1000, trickit)


win.mainloop()