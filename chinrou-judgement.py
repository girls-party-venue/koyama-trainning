from tkinter import ttk, Tk
import tkinter
from PIL import Image, ImageTk
import random

#Global変数として定義
num = 0
chinrou_num = 2
object_num = 2
pic_num = chinrou_num + object_num

# 昼のアクション1
def confirm_answer(event):
    # print(number)
    print(int(event.widget.cget("text")))
    root = Tk()
    root.title("confirm answer")
    #======================================================================
    filename = 'fig_list\\template\\ちん狼でよろしいですか.png'
    confirm_img = Image.open(filename)
    confirm_chinrou_img = ImageTk.PhotoImage(confirm_img, master=root)
    confirm_label = ttk.Label(root, image = confirm_chinrou_img)
    #======================================================================
    input_filename = img_list[int(event.widget.cget("text"))]
    question_img = Image.open(input_filename)
    question_chinrou_img = ImageTk.PhotoImage(question_img, master=root)
    question_label = ttk.Label(root, image = question_chinrou_img)
    #======================================================================
    conf_button_ok = ttk.Button(root, text='OK', command=lambda:[voting_chinrou(),root.destroy()])
    conf_button_no = ttk.Button(root, text='NO', command=lambda:root.destroy())
    confirm_label.pack()
    question_label.pack()
    conf_button_ok.pack(side = 'left', anchor='center')
    conf_button_no.pack(side = 'left', anchor='center')
    
    root.mainloop()

def voting_chinrou():
    print("aaa")

# 自作サンプル関数==================
def test_func2():
    root = Tk()
    root.title("Judgement")
    object_flag = True
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

    string = "ちん狼です"
    judge_label = ttk.Label(window,
        text = string,
        foreground = '#008080',
        padding = (5,10),
        font = ('游ゴシック',20))
    judge_label.pack()
# =================================

# 昼のアクション2

# 夜のアクション1

# 夜のアクション2

# 朝のアクション

# 自作lib, 画像ファイルのパスを入力すると tkinterで使用できる形で画像を返してくれる。
#TODO エラー出力。原因はおそらく、ImageTk.PhotoImageの第2引数にどのwindowで使うか指定していないから。
def making_img(input_filename):
    width=100
    height=100
    img = Image.open(input_filename)
    img = title_img.resize((width, height))
    img_ttk2 = ImageTk.PhotoImage(img)
    return img_ttk2

# メインウィンドウ
window = tkinter.Tk()
window.geometry("1100x600")
window.title("ちん狼ジャッジメント")

#===============
# img取得場
filename = 'bocchi-chan-icon.png'
title_img = Image.open(filename)
title_img = title_img.resize((100, 100))
title_img_ttk = ImageTk.PhotoImage(title_img)

# ファイルのパスをまとめたリスト
img_list = []
chinrou_dir = 'fig_list\\chinrou_fig\\'
object_dir = 'fig_list\\object_fig\\'
# 画像ファイル名とindex番号を紐づけた辞書も作成しておく。
# 本当は無いほうが処理が早そう。
input_img = {}
for i in range(chinrou_num):
    input_img_string = chinrou_dir + "chinrou_" + str(i) + ".jpg"
    img_list.append(input_img_string)
    input_img[input_img_string] = i
for i in range(object_num):
    input_img_string = object_dir + "object_" + str(i) + ".jpg"
    img_list.append(input_img_string)
    input_img[input_img_string] = i + chinrou_num
#===============

title = ttk.Label(window,
    text = 'ちん狼ジャッジメント',
    foreground = '#1155ee',
    font=("游ゴシック", "20", "bold"),
    wraplength = 400,
    image = title_img_ttk,
    compound = 'right')
title.pack()

#あるボタンが持つ設定値をまとめたものが格納される。
button_list = []
#あるボタンで使用するように変換した画像が格納される。
btn_img = []
#表示する画像の順番をランダムにする配列
img_rand = []
while len(img_rand) < pic_num:
    n = random.randint(0,pic_num-1)
    if not n in img_rand:
        img_rand.append(n)
for i in range(4):
    print(img_rand[i])

# tkinter用の画像を並べて配列に格納。
for i in range(pic_num):
    button_img = (Image.open(img_list[i])).resize((100, 100))
    btn_img.append(ImageTk.PhotoImage(button_img))

# tkinter用の画像を乱数配列を基に並び変え。
tmp_btn_img = []
for i in img_rand:
    tmp_btn_img.append(btn_img[i])

for i in range(pic_num):
    btn_id = img_rand[i] #ボタンにidを振る。
    button_list.append(ttk.Button(window, image=tmp_btn_img[i], text=btn_id))
    button_list[i].pack(side = 'left')
    button_list[i].bind("<ButtonPress>", confirm_answer)

window.mainloop()