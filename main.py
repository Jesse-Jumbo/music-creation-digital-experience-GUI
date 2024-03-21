import os
import tkinter as tk
from tkinter import filedialog, messagebox
import sounddevice as sd
import wavio
import threading

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


def record_audio():
    # 設置錄音的參數
    fs = 44100  # 採樣頻率
    seconds = 5  # 錄音時間
    messagebox.showinfo("錄音", "錄音開始，將持續 {} 秒".format(seconds))
    try:
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)  # 改為單聲道
        sd.wait()  # 等待錄音結束
        # 錄音保存
        file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if file_path:
            wavio.write(file_path, recording, fs, sampwidth=2)
            listbox_files.insert(tk.END, file_path)
            messagebox.showinfo("錄音", "錄音保存於: " + file_path)
    except Exception as e:
        messagebox.showerror("錄音錯誤", str(e))


if __name__ == '__main__':
    window = tk.Tk()
    window.title("音檔合成工具")

    btn_select = tk.Button(window, text="選擇音檔", command=select_files)
    btn_select.pack()

    listbox_files = tk.Listbox(window)
    listbox_files.pack()

    btn_merge = tk.Button(window, text="合成音檔", command=merge_files)
    btn_merge.pack()

    btn_record = tk.Button(window, text="錄製音檔", command=lambda: threading.Thread(target=record_audio).start())
    btn_record.pack()

    window.mainloop()
