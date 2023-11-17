import tkinter as tk
import webbrowser

# 倒计时秒数
count = 5

# 目标URL
target_url = ""

# 广告图片(.gif)
ad_pic = ""

# 跳过广告
def skip():
    root.destroy()

# 打开浏览器
def mouse_move(event):
    webbrowser.open(target_url)
    root.destroy()

# 童叟无欺倒计时
def update_timer():
    global count
    count -= 1
    timer_label.config(text="Advertisement time: " + str(count) + "s")

    if count > 0:
        root.after(2000, update_timer)
    else:
        root.destroy()

root = tk.Tk()

# 全屏
root.attributes('-fullscreen', True)

# 显示倒计时
timer_label = tk.Label(root, text="Advertisement time: " + str(count) + "s")
timer_label.pack()

# 显示跳过按钮
tk.Button(root, text="Skip", command=skip).pack()

# 显示“广告”
pyad_img = tk.PhotoImage(file=ad_pic)
tk.Label(root, image=pyad_img).pack()

# 监听鼠标移动
root.bind("<Motion>", mouse_move)

root.after(2000, update_timer)
root.mainloop()
