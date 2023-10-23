import tkinter as tk
from tkinter import ttk

def countdownTimer():
    confirmButton.config(state=tk.DISABLED)
    countdown = int(countdown_time_entry.get())
    restTime = int(rest_time_entry.get())
    Laps = int(laps_entry.get())
    countdown_time_label.config(text="", foreground="#ffcc4a")
    laps_contdown_label.config(text="")
    
    for i in range(Laps,0,-1):
        laps_contdown_label.config(text=f"เหลือจำนวนรอบอีก {i} รอบ", foreground="#ffcc4a")
            
        for n in range(countdown, -1, -1):
            countdown_time_label.config(text=f"เหลือเวลาอีก {n} วินาที", foreground="red")
            window.update()
            window.after(1000)

        for u in range(restTime, -1, -1):
            countdown_time_label.config(text=f"เหลือเวลาพักอีก {u} วินาที", foreground="green")
            window.update()
            window.after(1000)

    window.after(1000)
    countdown_time_label.config(text="")
    laps_contdown_label.config(text="หมดเวลาแล้ว!", foreground="green")
    confirmButton.config(state=tk.NORMAL)

            
window = tk.Tk()
window.title("Cycle Timer")

title_label = ttk.Label(text="นี่คือโปรแกรมจับเวลาออกกำลังกาย", font=("JasmineUPC", 20), foreground="#14b4d9")
title_label.grid(padx=40)

frame = ttk.Frame(window)
frame.grid(row=1,column=0)

ttk.Label(frame, text="เวลาออกกำลังที่ต้องการ :", font=("JasmineUPC", 16)).grid(row=1,column=0)
countdown_time_entry = ttk.Entry(frame)
countdown_time_entry.grid(row=1,column=1)

ttk.Label(frame, text="เวลาพักที่ต้องการ :", font=("JasmineUPC", 16)).grid(row=2,column=0)
rest_time_entry = ttk.Entry(frame)
rest_time_entry.grid(row=2,column=1)

ttk.Label(frame, text="จำนวนรอบที่ต้องการ :", font=("JasmineUPC", 16)).grid(row=3,column=0)
laps_entry = ttk.Entry(frame)
laps_entry.grid(row=3,column=1)

confirmButton = ttk.Button(text="ยืนยันข้อมูล", command=countdownTimer)
confirmButton.grid()

laps_contdown_label = ttk.Label(text="", font=("JasmineUPC", 20), foreground="#ffcc4a")
laps_contdown_label.grid()
countdown_time_label = ttk.Label(text="", font=("JasmineUPC", 20))
countdown_time_label.grid()

window.mainloop()