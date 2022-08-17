# Checkbutton控件
import tkinter
from tkinter import *
# from tkinter.ttk import *
from tkinter.messagebox import *
import cust_generate
import user_generate
import tkinter as tk


def cut(editor, event=None):
    editor.event_generate("<<Cut>>")


def copy(editor, event=None):
    editor.event_generate("<<Copy>>")


def paste(editor, event=None):
    editor.event_generate('<<Paste>>')


def rightKey(event, editor):
    menubar.delete(0, END)
    menubar.add_command(label='剪切', command=lambda: cut(editor))
    menubar.add_command(label='复制', command=lambda: copy(editor))
    menubar.add_command(label='粘贴', command=lambda: paste(editor))
    menubar.post(event.x_root, event.y_root)


def clearTextInput():
    text_message.delete("1.0", "end")


def btn_cust():
    new_cust_name = cust_generate.TmCust().cust_name_init()
    new_social_credit = cust_generate.TmCust().create_social_credit()
    # print(new_cust_name)
    # print(new_social_credit)
    text_message.insert("insert", "企业名称：" + new_cust_name)
    text_message.insert(tk.INSERT, '\n')
    text_message.insert("insert", "统一社会信用代码：" + new_social_credit)
    text_message.insert(tk.INSERT, '\n')


def btn_user():
    new_name = user_generate.TmUser().user_name()
    new_bank = user_generate.TmUser().user_bank_card()
    new_id_no = user_generate.TmUser().user_id_no()
    new_mobile_phone = user_generate.TmUser().user_mobile_phone()
    # print(new_name)
    # print(new_bank[0], new_bank[1])
    # print(new_id_no)
    # print(new_mobile_phone)
    text_message.insert("insert", "用户姓名：" + new_name)
    text_message.insert(tk.INSERT, '\n')
    text_message.insert("insert", "身份证号码：" + new_id_no)
    text_message.insert(tk.INSERT, '\n')
    text_message.insert("insert", "手机号码：" + new_mobile_phone)
    text_message.insert(tk.INSERT, '\n')
    text_message.insert("insert", "开户银行：" + new_bank[0])
    text_message.insert(tk.INSERT, '\n')
    text_message.insert("insert", "银行卡号：" + new_bank[1])
    text_message.insert(tk.INSERT, '\n')


# 新建一个窗体名称:root
window = tk.Tk()
# 为窗体添加一个标题
window.title("用户信息生成")
var = tkinter.StringVar()
text_message = tkinter.Text(window)
text_message.pack()
button_cust = tkinter.Button(window, text='生成客户', command=btn_cust)
button_cust.pack()
button_user = tkinter.Button(window, text='生成用户', command=btn_user)
button_user.pack()
button_user = tkinter.Button(window, text='清空', command=clearTextInput)
button_user.pack()
menubar = Menu(window, tearoff=False)  # 创建一个菜单
# 复制粘贴剪切绑定右键菜单事件。
text_message.bind("<Button-3>", lambda x: rightKey(x, text_message))

# 显示
window.mainloop()
