import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ShiftReport v0.1")
root.geometry("1100x700")


# WIDGETS SECTION
production_frame = ttk.Frame(root, padding=10)
production_frame_label = ttk.Label(production_frame, text="Produkcja")
production_order_entry_label = ttk.Label(production_frame, text="Numer zlecenia")
production_order_entry = ttk.Entry(production_frame, width=30)
production_int_label = ttk.Label(production_frame, text="Ilość wyprodukowana")
production_int_entry = ttk.Entry(production_frame, width=30)
production_add_button = ttk.Button(production_frame, text="Dodaj")

downtime_frame = ttk.Frame(root, padding=10)
downtime_frame_label = ttk.Label(downtime_frame, text="Postoje")
downtime_reason_entry_label = ttk.Label(downtime_frame, text="Powód postoju")
downtime_reason_entry = ttk.Entry(downtime_frame, width=30)
downtime_duration_label = ttk.Label(downtime_frame, text="Czas trwania (minuty)")
downtime_duration_entry = ttk.Entry(downtime_frame, width=30)
downtime_add_button = ttk.Button(downtime_frame, text="Dodaj")


teams_frame = ttk.Frame(root, padding=10)
teams_frame_label = ttk.Label(teams_frame, text="Raport Teams")
teams_text_box = tk.Text(teams_frame, width=40, height=10)

outlook_frame = ttk.Frame(root, padding=10)
outlook_frame_label = ttk.Label(outlook_frame, text="Raport Outlook")
outlook_text_box = tk.Text(outlook_frame, width=40, height=10)


# MANAGE WIDGETS
production_frame.grid(row=0, column=0, padx=5, pady=5)
downtime_frame.grid(row=0, column=1, padx=5, pady=5)
teams_frame.grid(row=1, column=0, padx=5, pady=5)
outlook_frame.grid(row=1, column=1, padx=5, pady=5)

production_frame_label.grid(row=0, column=0, padx=5, pady=5)
production_order_entry_label.grid(row=1, column=0, padx=5, pady=5)
production_order_entry.grid(row=2, column=0, padx=5, pady=5)
production_int_label.grid(row=1, column=1, padx=5, pady=5)
production_int_entry.grid(row=2, column=1, padx=5, pady=5)
production_add_button.grid(row=2, column=2, columnspan=2, padx=5, pady=5)


downtime_frame_label.grid(row=0, column=0, padx=5, pady=5)
downtime_reason_entry_label.grid(row=1, column=0, padx=5, pady=5)
downtime_reason_entry.grid(row=2, column=0, padx=5, pady=5)
downtime_duration_label.grid(row=1, column=1, padx=5, pady=5)
downtime_duration_entry.grid(row=2, column=1, padx=5, pady=5)
downtime_add_button.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

teams_frame_label.grid(row=0, column=0, padx=5, pady=5)
teams_text_box.grid(row=1, column=0, padx=5, pady=5)

outlook_frame_label.grid(row=0, column=0, padx=5, pady=5)
outlook_text_box.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
