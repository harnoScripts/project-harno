import tkinter as tk
from tkinter import scrolledtext

# ========================================
# PROJECT HARNO - TKINTER EDITION
# ========================================
# Visual idêntico ao Project Ligma Remake
# ========================================

# ========================================
# JANELA PRINCIPAL
# ========================================
root = tk.Tk()
root.title("Project Harno")
root.geometry("500x320")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# ========================================
# TITLE BAR
# ========================================
title_bar = tk.Frame(root, bg="#c8c8c8", height=25)
title_bar.pack(fill=tk.X)
title_bar.pack_propagate(False)

title = tk.Label(title_bar, text="Project Harno", bg="#c8c8c8", fg="black", font=("Arial", 10, "bold"), anchor="w")
title.pack(side=tk.LEFT, padx=5)

close_btn = tk.Button(title_bar, text="X", bg="#dcdcdc", fg="black", font=("Arial", 8, "bold"), command=root.destroy, bd=1, relief="raised")
close_btn.pack(side=tk.RIGHT, padx=2, pady=2)

# ========================================
# FRAME PRINCIPAL
# ========================================
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# ========================================
# SCRIPT EDITOR
# ========================================
script_box = scrolledtext.ScrolledText(main_frame, width=50, height=12, bg="white", fg="black", font=("Consolas", 10), bd=1, relief="solid")
script_box.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")
script_box.insert(tk.END, "-- type your script here")

# ========================================
# OUTPUT BOX
# ========================================
output_box = scrolledtext.ScrolledText(main_frame, width=50, height=4, bg="white", fg="black", font=("Consolas", 8), bd=1, relief="solid")
output_box.grid(row=1, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")
output_box.insert(tk.END, "click here to enable output (just for looks m)")

# ========================================
# BOTÕES (EXE, CLEAR, INJECT)
# ========================================
btn_frame = tk.Frame(main_frame, bg="#f0f0f0")
btn_frame.grid(row=0, column=2, rowspan=2, padx=5, sticky="n")

def exe():
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, script_box.get("1.0", tk.END))

def clear():
    script_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Cleared!")

def inject():
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Injected! G00byd0lan in corner.")
    # Simula o g00by rodando e indo pro canto
    import time
    for i in range(5):
        output_box.insert(tk.END, f"\nSpinning... {i*20}°")
        root.update()
        time.sleep(0.2)
    output_box.insert(tk.END, "\nG00byd0lan went to the corner!")

tk.Button(btn_frame, text="EXE", width=8, command=exe, bg="#e6e6e6", bd=1, relief="raised").pack(pady=2)
tk.Button(btn_frame, text="CLEAR", width=8, command=clear, bg="#e6e6e6", bd=1, relief="raised").pack(pady=2)
tk.Button(btn_frame, text="INJECT", width=8, command=inject, bg="#e6e6e6", bd=1, relief="raised").pack(pady=2)

# ========================================
# SIDEBAR (OPTIONS)
# ========================================
sidebar = tk.Frame(main_frame, bg="#e6e6e6", bd=1, relief="solid")
sidebar.grid(row=0, column=3, rowspan=2, padx=5, sticky="n")

tk.Label(sidebar, text="Options", bg="#c8c8c8", font=("Arial", 9, "bold")).pack(fill=tk.X)

def decal():
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Decal (G00byd0lan) applied!")

def skybox():
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Skybox (G00byd0lan) applied!")

def reset():
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Reset!")

tk.Button(sidebar, text="Decal (G00by)", width=12, command=decal, bg="#f5f5f5", bd=1, relief="raised").pack(pady=2, padx=2)
tk.Button(sidebar, text="Skybox (G00by)", width=12, command=skybox, bg="#f5f5f5", bd=1, relief="raised").pack(pady=2, padx=2)
tk.Button(sidebar, text="Reset", width=12, command=reset, bg="#f5f5f5", bd=1, relief="raised").pack(pady=2, padx=2)

# ========================================
# FOOTER
# ========================================
footer = tk.Label(root, text="Project Harno Remake By g00byd0lan", bg="#f0f0f0", fg="black", font=("Arial", 7), anchor="e")
footer.pack(side=tk.BOTTOM, fill=tk.X)

# ========================================
# RODAR
# ========================================
root.mainloop()