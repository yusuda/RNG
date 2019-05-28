#! /usr/bin/env python
# coding: utf-8

import sys
import random
import tkinter as tk
from tkinter import messagebox

loop_count = 0

# python3系では動かない?
# reload(sys)
# sys.setdefaultencoding('utf-8')


# def get_num():
#     try:
#         num_of_st = int(sys.argv[1])
#     except ValueError:
#         return get_num()
#     else:
#         return num_of_st


def gen_next():
    # label_rand = tk.Label(frame, text=random.randint(1, 29), font=48)
    # label_rand.grid(row=0, column=1)
    # たぶんスコープの問題でダメ
    # -> そういうわけではないっぽい　呼び出し方の問題
    # このやり方だと，実行するたびにどんどんラベルが増える（中身を更新するのではなく）
    # -> StringVar()を設定し，それに新しい値をsetする
    if roop_count == 0:
        var.set('未入力')
    else:
        try:
            max_rand = int(entry_max.get())
            var.set(random.randint(1, max_rand))
        except ValueError:
            messagebox.showerror( u'エラー', u'無効な値です．整数で最大値を指定してください．')
    # label_rand.pack(fill='x', side='left')


def quit_widget():
    # return 'cancel'
    # ウィジェットを終了するコマンド
    root.quit()


# status = ''
# while status != 'e':
#     print random.randint(1, get_num())
#     status = raw_input('next: ')

# ルート
root = tk.Tk()
root.title('random number generator 1.0')
root.geometry('320x300')

# エントリ用のフレーム
frame_entry = tk.Frame(root)
frame_entry.pack()

# テキスト用のフレーム（ウィジェットを縦に並べる）
frame_text = tk.Frame(root)
frame_text.pack()

# ボタン用のフレーム（横に並べる）
frame_button = tk.Frame(root)
frame_button.pack()

# エントリ（乱数の最大値を入力）
label_entry = tk.Label(frame_entry, text=u'乱数の最大値を入力')
label_entry.pack()
entry_max = tk.Entry(frame_entry, width=20)
# 前回の値を入れっぱなしにするのはどうやらこれでいいらしい
entry_max.insert(tk.END, entry_max.get())
entry_max.pack()

# テキスト
label_before = tk.Label(frame_text, text=u'次は')
label_after = tk.Label(frame_text, text=u'です．')

# ボタン
# 関数を実行するように指定するのではなく，関数オブジェクトの状態でコマンドに指定する
button_next = tk.Button(frame_button, text='next', command=gen_next)
button_ok = tk.Button(frame_button, text='OK', command=quit_widget)

# ラベル（乱数部分の前）
# label_before.grid(row=0, column=0)
# label_after.grid(row=0, column=2)
# button_OK.grid(row=2, column=0)
# button_canc.grid(row=2, column=1)
label_before.pack(fill='x', side='top')

# 乱数部分の表示
# 起動時にも乱数生成・表示関数を実行
var = tk.StringVar()
# ボタンを押しても値を更新しているだけだが，ラベルは表示しなおさなくても更新されるらしい
gen_next()
label_rand = tk.Label(frame_text, textvariable=var, font=("Helvetica", 100, "bold"))
label_rand.pack(fill='x', side='top')
# 状態把握のためのカウンター
loop_count = loop_count + 1

# ラベル（乱数部分の後）
label_after.pack(fill='x', side='top')
button_next.pack(fill='x', side='left')
button_ok.pack(fill='x', side='left')

# ウィジェット実行のため？の処理？
root.mainloop()
