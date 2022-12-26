from tkinter import ttk, Tk
from PIL import Image, ImageTk
import random

def first_label_func(num):
    num += 1
    root = Tk()
    #root.geometry("500x500")
    if num == 1:
        root.title("初めてのtkinter")
    else:
        root.title(str(num)+"回目のwindow")
    entry = ttk.Entry(root)
    img_ttk = ImageTk.PhotoImage(img, master=root)
    button_list = []
    for i in range(10):
        button_list.append(ttk.Button(root,image=img_ttk,text = 'OK', command=lambda:judge_chinrou(object_or_chinrou(num))))
        #utton_list[i].grid(row=0, column=i)

    label_1 = ttk.Label(root,
        text ='ちん狼ジャッジメント',
        foreground = '#1155ee',
        padding = (5,10),
        font = ('Times New Roman',20),
        wraplength = 400,
        image = img_ttk,
        compound = 'right')
    entry = ttk.Entry(root)

    label_1.pack()
    entry.pack()
    for i in range(10):
        button_list[i].pack(side = 'left')
    root.mainloop()

def object_or_chinrou(num):
    ns = []
    judge_tmp = random.randint(1, 10)
    if not judge_tmp in ns:
        ns.append(judge_tmp)
    object_flag = True
    #今回の数字が1か2であれば、object_flagはFalseになる。(= ちん狼になる。)
    if ns[num - 1] < 3:
        object_flag = False
    return object_flag

def judge_chinrou(object_flag):
    root = Tk()
    root.title("Judgement")
    if object_flag:
        string = "ちん狼ではありません"
    else:
        string = "ちん狼です"
    label = ttk.Label(root,
        text = string,
        foreground = '#1155ee',
        padding = (5,10),
        font = ('Times New Roman',20))
    label.pack()
    root.mainloop()

num = 0
filename = 'bocchi-chan-square.jpg'
img = Image.open(filename)
img = img.resize((100, 100))

first_label_func(num)
