import tkinter as tk
import time

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        self.master.configure(background='black')
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        
        self.time_label = tk.Label(master, font=("ds-digital", 80), background="black", foreground="cyan")
        self.time_label.pack(anchor='center', pady=50)
        
        button_frame = tk.Frame(master, background='black')
        button_frame.pack()
        
        self.start_button = tk.Button(button_frame, text="Start", font=("ds-digital", 18), background="black", foreground="cyan", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(button_frame, text="Stop", font=("ds-digital", 18), background="black", foreground="cyan", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(button_frame, text="Reset", font=("ds-digital", 18), background="black", foreground="cyan", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        tk.Button(master, text="Quit", font=("ds-digital", 18), background="black", foreground="cyan", command=self.master.destroy).pack(pady=20)
        
        self.update_clock()
    
    def update_clock(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        elapsed_time_str = self.format_time(self.elapsed_time)
        self.time_label.config(text=elapsed_time_str)
        self.time_label.after(100, self.update_clock)
    
    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return f"{int(hours):02}:{int(mins):02}:{int(secs):02}"
    
    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
    
    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
    
    def reset(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

def main():
    root = tk.Tk()
    root.geometry("600x400")
    stopwatch = Stopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
