import tkinter,sys
from tkinter import *
from tkinter.ttk import *

while True:
        root = Tk()
        root.title('ASCII码转换')  # 程序的标题名称
        root.geometry("500x500+512+288")  # 窗口的大小及页面的显示位置
        root.resizable(False, False)  # 固定页面不可放大缩小
        root.iconbitmap("picture.ico")  # 程序的图标

        canvas = tkinter.Canvas(root, bg="#ebebeb", height=500, width=500, borderwidth=-3)  # 创建画布
        canvas.pack(side='top')  # 放置画布
        try:
                image_file1 = tkinter.PhotoImage(file="./ASCII1.png")  # 加载图片文件
                canvas.create_image(0, 0, anchor='nw', image=image_file1)  # 将图片置于画布上
                image_file2 = tkinter.PhotoImage(file="./ASCII2.png")  # 加载图片文件
                canvas.create_image(250, 0, anchor='nw', image=image_file2)  # 将图片置于画布上
        except:
                exit()
                pass

        #输入信息
        var_Input_information = tkinter.StringVar()
        tkinter.Entry(root, width=20, borderwidth=1, bg='#ebebeb', textvariable=var_Input_information).place(x=29, y=300)

        #输入信息
        var_pick_up_information = tkinter.StringVar()
        tkinter.Entry(root, width=20, borderwidth=1, bg='#ebebeb', textvariable=var_pick_up_information).place(x=306, y=300)

 
        #获取信息
        var_Input_information_2 = tkinter.StringVar()
        tkinter.Entry(root, width=20, borderwidth=1, bg='#ebebeb', textvariable=var_Input_information_2).place(x=29, y=350)

        #获取信息
        var_pick_up_information_2 = tkinter.StringVar()
        tkinter.Entry(root, width=20, borderwidth=1, bg='#ebebeb', textvariable=var_pick_up_information_2).place(x=306, y=350)

        tkinter.Label(canvas, bg="#ebebeb", text='↓↓↓↓').place(x=364, y=324)
        tkinter.Label(canvas, bg="#ebebeb", text='↓↓↓↓').place(x=84, y=324)

 
        def ASCII_ord():
                try:
                        ord_ = ord(var_Input_information.get())
                        var_Input_information_2.set(ord_)
                except:
                        var_Input_information_2.set('错误字符或多输入字符！！！')

        def ASCII_chr():
                try:
                        chr_ = chr(int(var_pick_up_information.get()))
                        var_pick_up_information_2.set(chr_)
                except:
                        var_pick_up_information_2.set('错误字符或多输入字符！！！')
        Button(root, text='字符转ASCII码', command=ASCII_ord).place(x=55, y=240)
        Button(root, text='ASCII码转字符', command=ASCII_chr).place(x=336, y=240)
        root.mainloop()
        sys.exit(0)
