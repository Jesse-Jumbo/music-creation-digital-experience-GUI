import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


os.environ['TK_SILENCE_DEPRECATION'] = "1"


def select_files():
    # 讓用戶選擇音檔
    file_paths = filedialog.askopenfilenames()
    # 將選擇的音檔顯示在列表中
    listbox_files.delete(0, tk.END)
    for path in file_paths:
        listbox_files.insert(tk.END, path)


def merge_files():
    # 從列表中獲取音檔路徑
    files = listbox_files.get(0, tk.END)
    if files:
        # 在這裡調用您的音檔合成函數
        # merge_audio(files)
        messagebox.showinfo("成功", "音檔合成成功！")
    else:
        messagebox.showwarning("警告", "請先選擇音檔！")


if __name__ == '__main__':
    # 創建窗口
    window = tk.Tk()
    window.title("音檔合成工具")

    # 選擇文件按鈕
    btn_select = tk.Button(window, text="選擇音檔", command=select_files)
    btn_select.pack()

    # 顯示選擇的文件
    listbox_files = tk.Listbox(window)
    listbox_files.pack()

    # 合成按鈕
    btn_merge = tk.Button(window, text="合成音檔", command=merge_files)
    btn_merge.pack()

    # 運行GUI程序
    window.mainloop()
