from tkinter import ttk
from tkinter import *

root = Tk()  # 初始框的声明
columns = ("姓名", "IP地址")
treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

treeview.column("姓名", width=100, anchor='center')  # 表示列,不显示
treeview.column("IP地址", width=300, anchor='center')

treeview.heading("姓名", text="姓名")  # 显示表头
treeview.heading("IP地址", text="IP地址")

treeview.pack(side=LEFT, fill=BOTH)

name = ['电脑1', '服务器', '笔记本']
ipcode = ['10.13.71.223', '10.25.61.186', '10.25.11.163']
for i in range(min(len(name), len(ipcode))):  # 写入数据
    treeview.insert('', i, values=(name[i], ipcode[i]))


def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题


def set_cell_value(event):  # 双击进入编辑状态
    for item in treeview.selection():
        # item = I001
        item_text = treeview.item(item, "values")
        # print(item_text[0:2])  # 输出所选行的值
    column = treeview.identify_column(event.x)  # 列
    row = treeview.identify_row(event.y)  # 行
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))
    entryedit = Text(root, width=10 + (cn - 1) * 16, height=1)
    entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)

    def saveedit():
        treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()

    okb = ttk.Button(root, text='OK', width=4, command=saveedit)
    okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)


def newrow():
    name.append('待命名')
    ipcode.append('IP')
    treeview.insert('', len(name) - 1, values=(name[len(name) - 1], ipcode[len(name) - 1]))
    treeview.update()
    newb.place(x=120, y=(len(name) - 1) * 20 + 45)
    newb.update()


treeview.bind('<Double-1>', set_cell_value)  # 双击左键进入编辑
newb = ttk.Button(root, text='新建联系人', width=20, command=newrow)
newb.place(x=120, y=(len(name) - 1) * 20 + 45)

for col in columns:  # 绑定函数，使表头可排序
    treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeview, _col, False))
'''
1.遍历表格
t = treeview.get_children()
for i in t:
    print(treeview.item(i,'values'))
2.绑定单击离开事件
def treeviewClick(event):  # 单击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text[0:2])  # 输出所选行的第一列的值
tree.bind('<ButtonRelease-1>', treeviewClick)  
------------------------------
鼠标左键单击按下1/Button-1/ButtonPress-1 
鼠标左键单击松开ButtonRelease-1 
鼠标右键单击3 
鼠标左键双击Double-1/Double-Button-1 
鼠标右键双击Double-3 
鼠标滚轮单击2 
鼠标滚轮双击Double-2 
鼠标移动B1-Motion 
鼠标移动到区域Enter 
鼠标离开区域Leave 
获得键盘焦点FocusIn 
失去键盘焦点FocusOut 
键盘事件Key 
回车键Return 
控件尺寸变Configure
------------------------------
'''

root.mainloop()  # 进入消息循环



