# Checkbutton控件
from tkinter import *
# from tkinter.ttk import *
from tkinter.messagebox import *

# 新建一个窗体还是需要tkinter
root = Tk()
root.geometry("450x100")
root.title("CheckButton控件")


#Label标签
Label01 = Label(root,text = "请选择你去过的城市")
Label01.grid(row = 0,column = 0,padx = 0,pady = 20)

city_list = ["北京","上海","广州","深圳","南京"]
# 用一组值存储选中哪些
is_check_list = []

# 通过循环展示
for city in city_list:
    is_check_list.append(IntVar())
    CheckButton01 = Checkbutton(root,text=city,variable = is_check_list[-1])    # 为啥是-1
    CheckButton01.grid(row = 0,column = len(is_check_list),padx = 5,pady = 5)

# sel函数
def sel():
    all_select = ""
    for i in range(0,len(is_check_list)):
        if is_check_list[i].get() == 1:
            all_select += city_list[i] + " "
    Label_select["text"] = "所选城市为:"+all_select

# 添加一个Button
Button01 = Button(root,text = "确认选择",command = sel)
Button01.grid(row = 1,column = 0,padx = 5,pady = 5)

# 添加一个Label标签，用于展示显示后的结果
Label_select = Label(root,text = "")
Label_select.grid(row = 1,column = 1,columnspan = 5)


# 加载
root.mainloop()