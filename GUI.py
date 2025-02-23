import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os 

def launch_main_script():
    venv_python = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")  
    script_path = os.path.abspath("main.py")

    print(f"Trying to run: {script_path}")
    subprocess.Popen(["python", script_path], shell=True)

def show_foundation_day_gui():
    """
    Foundation Day window display with background image and rich text.
    """
    root = tk.Tk()
    root.title(" يوم التأسيس السعودي ")
    root.geometry("800x500")

    image = Image.open("Bakgrond.png")
    image = image.resize((800, 500), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(root, width=800, height=500, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    text_x, text_y = 800 // 2, 150

    foundation_day_text = """ يوم التأسيس - ٢٢ فبراير 
"فبراير 𝟏𝟕𝟐𝟕م .. يـوم بدينـا، للعز انـتـميـنا" 
تاريخ يُجسد جذورنا الراسخة ومسيرة مجدٍ 
امتدّت عبر القرون. فخرُ بماضينا، واعتزازُ 
بحاضرنا، وانطلاقةُ لمستقبلٍ مشرق."""

    canvas.create_text(
        text_x,
        text_y,
        text=foundation_day_text,
        fill="#5B4221",
        font=("Traditional Arabic", 20, "bold"),
        justify="center",
        anchor="center",
        width=500,
    )

    open_button = tk.Button(
        root,
        text="بمناسبة يوم التأسيس، أدخل إلى تطبيق سعراتك... علشان ما تقول آخر الليل، وين راحت السعرات؟",
        command=root.destroy,
        bg="#F5F0E1",
        fg="#5B4221",
        font=("Arial", 15, "bold"),
        activebackground="#F5F0E1",
        padx=10,
        pady=5,
        borderwidth=2,
        relief="raised",
    )
    open_button.place(relx=0.5, rely=0.85, anchor="center")
    root.after(5000, launch_main_script)

    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\n❌ Program interrupted by user. Exiting safely...")
        root.destroy()  



show_foundation_day_gui()
