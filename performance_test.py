import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time
from algoritmalar import KonveksZarfCozucu

class ConvexHullPerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritma Performans Analizi")
        self.root.geometry("800x750")

        # Başlık
        self.label = tk.Label(root, text="Kaba Kuvvet vs Graham Scan Performans Testi", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)

        # Kontrol Butonu
        self.start_button = tk.Button(root, text="Testi Başlat ve Grafiği Çiz", command=self.run_performance_test, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.start_button.pack(pady=5)

        # Grafik Alanı
        self.figure, self.ax = plt.subplots(figsize=(15, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Sonuç Tablosu
        self.result_label = tk.Label(root, text="Detaylı Performans Sonuçları:", font=("Arial", 10, "bold"), anchor="w")
        self.result_label.pack(fill=tk.X, padx=10, pady=(5, 0))
        
        self.result_text = tk.Text(root, height=10, font=("Courier New", 9))
        self.result_text.pack(fill=tk.X, padx=10, pady=5)

    def generate_points(self, n):
        """Rastgele N adet (x, y) noktası üretir."""
        return [(random.randint(0, 10000), random.randint(0, 10000)) for _ in range(n)]

    def run_performance_test(self):
        self.start_button.config(state="disabled", text="Test Çalışıyor...")
        self.result_text.delete(1.0, tk.END)
        self.root.update()

        n_values = [100, 500, 1000, 2000, 5000] 
        
        bf_times = []
        gs_times = []

        for n in n_values:
            points = self.generate_points(n)

            # Brute Force Süre Ölçümü
            start_time = time.time()
            KonveksZarfCozucu.kaba_kuvvet_konveks_zarf(points)
            bf_times.append(time.time() - start_time)

            # Graham Scan Süre Ölçümü
            start_time = time.time()
            KonveksZarfCozucu.graham_tarama_konveks_zarf(points)
            gs_times.append(time.time() - start_time)
            
            # Arayüzün donmaması için güncelleme
            print(f"N={n} tamamlandı.")
            self.root.update()

        self.draw_graph(n_values, bf_times, gs_times)
        self.display_results(n_values, bf_times, gs_times)
        self.start_button.config(state="normal", text="Testi Tekrar Başlat")

    def display_results(self, n_values, bf_times, gs_times):
        header = f"{'N (Nokta)':<12} | {'Kaba Kuvvet (sn)':<20} | {'Graham Scan (sn)':<20} | {'Hızlanma (Kat)'}\n"
        sep = "-" * 80 + "\n"
        self.result_text.insert(tk.END, header + sep)
        
        for n, bf, gs in zip(n_values, bf_times, gs_times):
            ratio = bf / gs if gs > 0 else 0
            line = f"{n:<12} | {bf:<20.6f} | {gs:<20.6f} | {ratio:.2f}x\n"
            self.result_text.insert(tk.END, line)

    def draw_graph(self, n_values, bf_times, gs_times):
        self.ax.clear()
        
        # Verileri Çizdir
        self.ax.plot(n_values, bf_times, label="Kaba Kuvvet (Brute Force)", marker='o', color='tab:blue')
        self.ax.plot(n_values, gs_times, label="Graham Scan", marker='x', color='tab:orange')

        # Grafik Başlık ve Etiketleri
        self.ax.set_title("BİLGİSAYARINIZDA HER İKİ YÖNTEMİN ÇALIŞMA\nSÜRELERİNİN KARŞILAŞTIRILMASI")
        self.ax.set_xlabel("N ADET NOKTALAR KÜMESİ")
        self.ax.set_ylabel("SÜRE (SANİYE)")
        
        self.ax.legend()
        self.ax.grid(True, linestyle='--', alpha=0.6)

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConvexHullPerformanceApp(root)
    root.mainloop()