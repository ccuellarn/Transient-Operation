import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import base64
from io import BytesIO

class AstronomicalPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Planner for Astronomical Observations")
        self.root.geometry("1200x900")
        
        # Estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background='white')
        self.style.configure('TLabel', background='white', font=('Tahoma', 10))
        self.style.configure('Header.TLabel', font=('Tahoma', 16, 'bold'), foreground='#242949')
        self.style.configure('TButton', font=('Tahoma', 10), background='#242949', foreground='white')
        self.style.configure('TEntry', font=('Tahoma', 10))
        self.style.configure('TCombobox', font=('Tahoma', 10))
        
        # Contenedor principal
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Logo (placeholder)
        self.logo_label = ttk.Label(self.header_frame, text="LOGO", width=20)
        self.logo_label.pack(side=tk.LEFT, padx=10)
        
        self.title_label = ttk.Label(self.header_frame, text="Planner for Astronomical Observations", style='Header.TLabel')
        self.title_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Formulario
        self.form_frame = ttk.LabelFrame(self.main_frame, text="Observation Parameters", padding=20)
        self.form_frame.pack(fill=tk.X, pady=10)
        
        # Primera fila (Latitud/Longitud)
        self.row1_frame = ttk.Frame(self.form_frame)
        self.row1_frame.pack(fill=tk.X, pady=5)
        
        self.latitud_label = ttk.Label(self.row1_frame, text="Observer Latitude (degree):")
        self.latitud_label.pack(side=tk.LEFT, padx=5)
        self.latitud_entry = ttk.Entry(self.row1_frame, width=15)
        self.latitud_entry.pack(side=tk.LEFT, padx=5)
        self.latitud_entry.insert(0, "4.609")
        
        self.longitud_label = ttk.Label(self.row1_frame, text="Observer Longitude (degree):")
        self.longitud_label.pack(side=tk.LEFT, padx=5)
        self.longitud_entry = ttk.Entry(self.row1_frame, width=15)
        self.longitud_entry.pack(side=tk.LEFT, padx=5)
        self.longitud_entry.insert(0, "-74.081")
        
        # Segunda fila (Fechas)
        self.row2_frame = ttk.Frame(self.form_frame)
        self.row2_frame.pack(fill=tk.X, pady=5)
        
        self.fecha_inicio_label = ttk.Label(self.row2_frame, text="Start Date and Time:")
        self.fecha_inicio_label.pack(side=tk.LEFT, padx=5)
        self.fecha_inicio_entry = ttk.Entry(self.row2_frame, width=20)
        self.fecha_inicio_entry.pack(side=tk.LEFT, padx=5)
        self.fecha_inicio_entry.insert(0, "2025-03-13 19:00")
        
        self.fecha_fin_label = ttk.Label(self.row2_frame, text="End Date and Time:")
        self.fecha_fin_label.pack(side=tk.LEFT, padx=5)
        self.fecha_fin_entry = ttk.Entry(self.row2_frame, width=20)
        self.fecha_fin_entry.pack(side=tk.LEFT, padx=5)
        self.fecha_fin_entry.insert(0, "2025-03-14 07:00")
        
        # Tercera fila (Escala de tiempo)
        self.row3_frame = ttk.Frame(self.form_frame)
        self.row3_frame.pack(fill=tk.X, pady=5)
        
        self.escala_tiempo_label = ttk.Label(self.row3_frame, text="Time Scale:")
        self.escala_tiempo_label.pack(side=tk.LEFT, padx=5)
        self.escala_tiempo_combo = ttk.Combobox(self.row3_frame, values=["Seconds", "Minutes", "Hours"], width=10)
        self.escala_tiempo_combo.pack(side=tk.LEFT, padx=5)
        self.escala_tiempo_combo.current(1)
        
        self.escala_valor_label = ttk.Label(self.row3_frame, text="Value of Time Scale:")
        self.escala_valor_label.pack(side=tk.LEFT, padx=5)
        self.escala_valor_entry = ttk.Entry(self.row3_frame, width=5)
        self.escala_valor_entry.pack(side=tk.LEFT, padx=5)
        self.escala_valor_entry.insert(0, "30")
        
        # Cuarta fila (Límites)
        self.row4_frame = ttk.Frame(self.form_frame)
        self.row4_frame.pack(fill=tk.X, pady=5)
        
        self.altitud_label = ttk.Label(self.row4_frame, text="Altitude Limit (degrees):")
        self.altitud_label.pack(side=tk.LEFT, padx=5)
        self.altitud_entry = ttk.Entry(self.row4_frame, width=5)
        self.altitud_entry.pack(side=tk.LEFT, padx=5)
        self.altitud_entry.insert(0, "33")
        
        self.magnitud_label = ttk.Label(self.row4_frame, text="Minimum Magnitude:")
        self.magnitud_label.pack(side=tk.LEFT, padx=5)
        self.magnitud_entry = ttk.Entry(self.row4_frame, width=5)
        self.magnitud_entry.pack(side=tk.LEFT, padx=5)
        self.magnitud_entry.insert(0, "30")
        
        # Quinta fila (Parámetro K)
        self.row5_frame = ttk.Frame(self.form_frame)
        self.row5_frame.pack(fill=tk.X, pady=5)
        
        self.parametro_k_label = ttk.Label(self.row5_frame, text="Parameter K (seconds):")
        self.parametro_k_label.pack(side=tk.LEFT, padx=5)
        self.parametro_k_entry = ttk.Entry(self.row5_frame, width=5)
        self.parametro_k_entry.pack(side=tk.LEFT, padx=5)
        self.parametro_k_entry.insert(0, "10")
        
        # Sección de objetivos
        self.targets_frame = ttk.LabelFrame(self.main_frame, text="Targets of Astronomical Observations", padding=20)
        self.targets_frame.pack(fill=tk.X, pady=10)
        
        # Modo de ingreso
        self.modo_frame = ttk.Frame(self.targets_frame)
        self.modo_frame.pack(fill=tk.X, pady=5)
        
        self.modo_label = ttk.Label(self.modo_frame, text="Entry Mode:")
        self.modo_label.pack(side=tk.LEFT, padx=5)
        self.modo_combo = ttk.Combobox(self.modo_frame, values=["Manual Entry", "Upload CSV"], width=15)
        self.modo_combo.pack(side=tk.LEFT, padx=5)
        self.modo_combo.current(0)
        self.modo_combo.bind("<<ComboboxSelected>>", self.toggle_input_mode)
        
        # Contenedor para entrada manual
        self.manual_frame = ttk.Frame(self.targets_frame)
        self.manual_frame.pack(fill=tk.X, pady=5)
        
        # Primer objetivo
        self.target_container = ttk.Frame(self.manual_frame)
        self.target_container.pack(fill=tk.X)
        
        self.add_target_row(initial=True)
        
        self.add_button = ttk.Button(self.manual_frame, text="Add Another Target", command=self.add_target_row)
        self.add_button.pack(pady=10)
        
        # Contenedor para CSV (inicialmente oculto)
        self.csv_frame = ttk.Frame(self.targets_frame)
        
        self.csv_label = ttk.Label(self.csv_frame, text="Upload CSV file:")
        self.csv_label.pack(side=tk.LEFT, padx=5)
        self.csv_button = ttk.Button(self.csv_frame, text="Browse...", command=self.browse_csv)
        self.csv_button.pack(side=tk.LEFT, padx=5)
        self.csv_file_label = ttk.Label(self.csv_frame, text="No file selected")
        self.csv_file_label.pack(side=tk.LEFT, padx=5)
        
        # Botón de generar plan
        self.generate_button = ttk.Button(self.main_frame, text="Generate Observation Plan", command=self.generate_plan)
        self.generate_button.pack(pady=20)
        
        # Resultados (inicialmente ocultos)
        self.results_frame = ttk.LabelFrame(self.main_frame, text="Observation Plan Generated", padding=20)
        
        # Tabla de resultados
        self.tree = ttk.Treeview(self.results_frame, columns=("Hour", "Label", "Target", "RA", "DEC", "Magnitude", "Exposition Time"), show="headings")
        self.tree.heading("Hour", text="Hour")
        self.tree.heading("Label", text="Label")
        self.tree.heading("Target", text="Target")
        self.tree.heading("RA", text="RA")
        self.tree.heading("DEC", text="DEC")
        self.tree.heading("Magnitude", text="Magnitude")
        self.tree.heading("Exposition Time", text="Exposition Time")
        
        scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Gráfica (inicialmente oculta)
        self.plot_frame = ttk.LabelFrame(self.main_frame, text="Celestial Positions", padding=20)
        self.plot_canvas = None
        
        # Footer
        self.footer_frame = ttk.Frame(self.main_frame)
        self.footer_frame.pack(fill=tk.X, pady=20)
        
        current_year = datetime.now().year
        self.footer_label = ttk.Label(self.footer_frame, text=f"Rights Reserved © {current_year}", font=('Tahoma', 8))
        self.footer_label.pack()
        
    def toggle_input_mode(self, event=None):
        mode = self.modo_combo.get()
        if mode == "Manual Entry":
            self.manual_frame.pack(fill=tk.X, pady=5)
            self.csv_frame.pack_forget()
        else:
            self.manual_frame.pack_forget()
            self.csv_frame.pack(fill=tk.X, pady=5)
    
    def browse_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.csv_file_label.config(text=file_path.split("/")[-1])
    
    def add_target_row(self, initial=False):
        row_frame = ttk.Frame(self.target_container)
        row_frame.pack(fill=tk.X, pady=5)
        
        # Nombre
        nombre_label = ttk.Label(row_frame, text="Name of the target:")
        nombre_label.pack(side=tk.LEFT, padx=5)
        nombre_entry = ttk.Entry(row_frame, width=15)
        nombre_entry.pack(side=tk.LEFT, padx=5)
        if initial:
            nombre_entry.insert(0, "ATKFRLD")
        
        # RA
        ra_label = ttk.Label(row_frame, text="Right Ascention (RA):")
        ra_label.pack(side=tk.LEFT, padx=5)
        ra_entry = ttk.Entry(row_frame, width=15)
        ra_entry.pack(side=tk.LEFT, padx=5)
        if initial:
            ra_entry.insert(0, "09h21m58.31s")
        
        # DEC
        dec_label = ttk.Label(row_frame, text="Declination (DEC):")
        dec_label.pack(side=tk.LEFT, padx=5)
        dec_entry = ttk.Entry(row_frame, width=15)
        dec_entry.pack(side=tk.LEFT, padx=5)
        if initial:
            dec_entry.insert(0, "+24d39m47.46s")
        
        # Magnitud
        mag_label = ttk.Label(row_frame, text="Magnitude:")
        mag_label.pack(side=tk.LEFT, padx=5)
        mag_entry = ttk.Entry(row_frame, width=8)
        mag_entry.pack(side=tk.LEFT, padx=5)
        if initial:
            mag_entry.insert(0, "-7.59")
        
        # Botón eliminar (excepto para la fila inicial)
        if not initial:
            delete_button = ttk.Button(row_frame, text="Delete", command=lambda: row_frame.destroy())
            delete_button.pack(side=tk.LEFT, padx=5)
    
    def generate_plan(self):
        # Validar entrada
        if self.modo_combo.get() == "Upload CSV" and self.csv_file_label.cget("text") == "No file selected":
            messagebox.showerror("Error", "Please select a CSV file")
            return
        
        # Aquí iría la lógica para generar el plan de observación
        # Por ahora simulamos datos de ejemplo
        
        # Mostrar resultados
        self.show_results()
    
    def show_results(self):
        # Limpiar resultados anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Añadir datos de ejemplo
        sample_data = [
            ("19:00", "Start", "ATKFRLD", "09h21m58.31s", "+24d39m47.46s", "-7.59", "30s"),
            ("19:30", "Obs", "ATKFRLD", "09h21m58.31s", "+24d39m47.46s", "-7.59", "30s"),
            ("20:00", "Obs", "ATKFRLD", "09h21m58.31s", "+24d39m47.46s", "-7.59", "30s"),
            # ... más datos simulados
        ]
        
        for data in sample_data:
            self.tree.insert("", tk.END, values=data)
        
        # Mostrar frames de resultados
        self.results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Crear y mostrar gráfica de ejemplo
        self.show_sample_plot()
    
    def show_sample_plot(self):
        # Crear una figura de ejemplo
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Datos de ejemplo
        hours = range(19, 24) + list(range(0, 8))
        altitudes = [30 + x % 10 for x in range(len(hours))]
        
        ax.plot(hours, altitudes, '-o')
        ax.set_xlabel("Hour")
        ax.set_ylabel("Altitude (degrees)")
        ax.set_title("Target Altitude Over Time")
        ax.grid(True)
        
        # Limpiar frame anterior si existe
        if self.plot_canvas:
            self.plot_canvas.get_tk_widget().destroy()
        
        # Mostrar en Tkinter
        self.plot_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.plot_canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = AstronomicalPlannerApp(root)
    root.mainloop()