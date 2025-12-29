import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time
from algoritmalar import KonveksZarfCozucu

class ConvexHullApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kapali Cevrim Uygulamasi")
        self.root.geometry("900x700")
        
        self.points = []
        
        # Üst Panel - Kontroller
        control_frame = tk.Frame(root, pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)
        
        tk.Label(control_frame, text="Nokta Sayısı:").pack(side=tk.LEFT, padx=5)
        self.n_entry = tk.Entry(control_frame, width=10)
        self.n_entry.insert(0, "50")
        self.n_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Button(control_frame, text="Nokta Üret", command=self.generate_points, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Kaba Kuvvet", command=self.run_brute_force, bg="#FF9800", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Graham Scan", command=self.run_graham_scan, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
        
        self.time_label = tk.Label(control_frame, text="Süre: 0.00s", font=("Arial", 10, "bold"))
        self.time_label.pack(side=tk.LEFT, padx=20)

        # Grafik Alanı
        self.figure, self.ax = plt.subplots(figsize=(6, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.generate_points()

    def generate_points(self):
        try:
            n = int(self.n_entry.get())
            self.points = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(n)]
            self.plot_result([], "")
        except ValueError:
            pass

    def run_brute_force(self):
        if not self.points: return
        
        # UI güncellemesi için
        self.root.config(cursor="wait")
        self.root.update()
        
        start = time.time()
        hull = KonveksZarfCozucu.kaba_kuvvet_konveks_zarf(self.points)
        duration = time.time() - start
        
        self.root.config(cursor="")
        self.plot_result(hull, f"Kaba Kuvvet: {duration:.4f}s")

    def run_graham_scan(self):
        if not self.points: return
        
        start = time.time()
        hull = KonveksZarfCozucu.graham_tarama_konveks_zarf(self.points)
        duration = time.time() - start
        
        self.plot_result(hull, f"Graham Scan: {duration:.4f}s")

    def plot_result(self, hull, title_text):
        self.ax.clear()
        # Noktaları çiz
        if self.points:
            px, py = zip(*self.points)
            self.ax.scatter(px, py, c='blue', s=20, alpha=0.6, label='Noktalar')
        
        # Zarfı çiz
        if hull:
            hx = [p[0] for p in hull] + [hull[0][0]]
            hy = [p[1] for p in hull] + [hull[0][1]]
            self.ax.plot(hx, hy, 'r-', linewidth=2, label='Konveks Zarf')
            self.ax.scatter(hx, hy, c='red', s=30)
            
        self.ax.set_title(title_text)
        self.ax.grid(True, linestyle='--', alpha=0.5)
        if title_text:
            self.time_label.config(text=title_text)
        else:
            self.time_label.config(text="Süre: 0.00s")
            
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConvexHullApp(root)
    root.mainloop()
