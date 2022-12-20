import tkinter as tk

window = tk.Tk()
window.title("STOPWATCH")
window.geometry("280x480")
window.resizable(False, False)
window.configure(bg="white")

run = False
sec = 0
mnt = 0
hou = 0

def start():
    global run

    if not run:
        main()
        run = True
        
def stop():
    global run
    if run:
        time_label.after_cancel(main_time)
        run = False

def reset():
    global run
    if run:
        time_label.after_cancel(main_time)
        run =  False

    global sec, mnt, hou
    sec = 0
    mnt = 0
    hou = 0

    time_label.config(text="00 : 00 : 00")

def main():
    global sec, mnt, hou
    sec += 1
    if sec == 60:
        mnt += 1
        sec = 0
    if mnt == 60:
        hou += 1
        mnt = 0
    
    hou_str = f"{hou}" if hou > 9 else f"0{hou}"
    mnt_str = f"{mnt}" if mnt > 9 else f"0{mnt}"
    sec_str = f"{sec}" if sec > 9 else f"0{sec}"

    time_label.config(text = f"{hou_str} : {mnt_str} : {sec_str}")

    global main_time
    main_time = time_label.after(1000, main)

time_label = tk.Label(text="00 : 00 : 00", font=("Helvetica", 32), bg="white")
time_label.pack(pady= 80)

quit_button = tk.Button(text="Quit", height = 2, width= 10, font=("Arial", 10), command = window.quit)
quit_button.pack(side=tk.BOTTOM, pady = 10)

reset_button = tk.Button(text="Reset", height = 2, width= 10, font=("Arial", 10), command = reset)
reset_button.pack(side=tk.BOTTOM, pady = 10)

stop_button = tk.Button(text="Stop", height = 2, width = 10, font=("Arial", 10), command = stop)
stop_button.pack(side=tk.BOTTOM, pady = 10)

start_button = tk.Button(text="Start", height = 2, width = 10, font=('Arial', 10), command = start)
start_button.pack(side=tk.BOTTOM, pady = 10)


window.mainloop()
