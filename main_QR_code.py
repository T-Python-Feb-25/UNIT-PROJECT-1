from art import * 
from colorama import Fore , Back , Style
import os
import qrcode
from datetime import datetime
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
from PIL import Image, ImageTk


print(text2art("QR ",font="fancy5",decoration="barcode1")) # decoration parameter is added in Version 4.6


""" Create a folder for saving QR Codes (if it doesn’t exist)"""

output_folder = "QR_Codes"
os.makedirs(output_folder, exist_ok=True)

def generate_qr(data, filename):

    """Generate a QR Code and save it as an image"""

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image
    file_path = os.path.join(output_folder, filename)
    img.save(file_path)
    print(f"{Fore.BLUE}✅ QR Code saved: {file_path}")

def generate_from_input():
    """Create a QR Code from user input"""

    data = input("🔹 Enter data for the QR Code: ").strip()
    if data:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"
        generate_qr(data, filename)
    else:
        print("⚠️ No data entered!")

def generate_from_file(file_path):
    """Generate multiple QR Codes from a file"""

    try:
        with open(file_path, "r", encoding="utf-8") as file: # when use with open() we dont need to close() file 
            lines = file.read() 
        
        if not lines:
            print("⚠️ The file is empty!")
            return
        
        #for index, line in enumerate(lines):
           # data = line.strip()
           # if data:
        filename = f"qr_{5}.png"
        generate_qr(lines,filename)

    except FileNotFoundError:
        print("❌ File not found!")

def read_from_QR_img(image_path):
    """Read the QR Code image and display the content on the screen"""
    
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"❌ Error: Could not load the image. Check the file name and path: {image_path}")
        return

    # Initialize OpenCV QR Code Detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR Code
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

    # Check if a QR Code was detected
    if vertices_array is not None:
        print("✅ QR Code Data:")
        print(data)
    else:
        print("❌ No QR Code detected in the image.")

#//////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////////////////creat QR CODES with diffrent window /////////////////////////////////////////////////




def create_qr_code_gui():

    """ This function creates a QR for a contact by entering the contact information in the GUI screen"""

    # Create the main window
    qr_image= None
    tk_img= None
    
    root = tk.Tk()       
    root.title("QR Code Generator")
    root.geometry("450x650")

    # Create a frame with a scrollbar
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Default colors
    qr_foreground = "black"
    qr_background = "white"

    # Functions for color selection
    def choose_foreground():
        nonlocal qr_foreground
        qr_foreground = colorchooser.askcolor()[1]

    def choose_background():
        nonlocal qr_background
        qr_background = colorchooser.askcolor()[1]

    # Function to generate the QR Code
    def generate_qr():
        name = entry_name.get()
        company = entry_company.get()
        phone = entry_phone.get()
        email = entry_email.get()
        website = entry_website.get()
        address = entry_address.get()
        box_size = int(size_var.get())  # QR box size

        if not name or not phone:
            messagebox.showwarning("Warning", "Please enter at least a name and phone number!")
            return

        # vCard data format
        vcard_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
ORG:{company}
TEL:{phone}
EMAIL:{email}
URL:{website}
ADR:;;{address}
END:VCARD"""

        # Generate QR Code
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=4
        )
        qr.add_data(vcard_data)
        qr.make(fit=True)

        # Create QR image
       
        qr_image = qr.make_image(fill_color=qr_foreground, back_color=qr_background)

        # Save temporarily and display
        qr_image.save("qr_temp.png")
        img = Image.open("qr_temp.png")
        tk_img = ImageTk.PhotoImage(img)
        qr_label.config(image=tk_img)
        qr_label.image = tk_img

    # Function to save QR as an image
    def save_qr():
        if qr_image:
            filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
            if filepath:
                qr_image.save(filepath)
                messagebox.showinfo("Saved", f"QR Code saved at: {filepath}")

    # Function to clear all fields
    def clear_fields():
        entry_name.delete(0, tk.END)
        entry_company.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_website.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        qr_label.config(image="")

    # Input fields
    tk.Label(scrollable_frame, text="Name:", font=("Arial", 12)).pack()
    entry_name = tk.Entry(scrollable_frame, width=40, font=("Arial", 12))
    entry_name.pack(pady=5)

    tk.Label(scrollable_frame, text="Company:", font=("Arial", 12)).pack()
    entry_company = tk.Entry(scrollable_frame, width=40, font=("Arial", 12))
    entry_company.pack(pady=5)

    tk.Label(scrollable_frame, text="Phone:", font=("Arial", 12)).pack()
    entry_phone = tk.Entry(scrollable_frame, width=40, font=("Arial", 12))
    entry_phone.pack(pady=5)

    tk.Label(scrollable_frame, text="Email:", font=("Arial", 12)).pack()
    entry_email = tk.Entry(scrollable_frame, width=40, font=("Arial", 12))
    entry_email.pack(pady=5)

    tk.Label(scrollable_frame, text="Website:", font=("Arial", 12)).pack()
    entry_website = tk.Entry(scrollable_frame, width=40, font=("Arial", 12))
    entry_website.pack(pady=5)

    tk.Label(scrollable_frame, text="Address:", font=("Arial", 12)).pack()
    entry_address = tk.Entry(scrollable_frame, width=40, font=("Arial", 12))
    entry_address.pack(pady=5)

    # QR color selection buttons
    tk.Button(scrollable_frame, text="Choose Foreground Color", command=choose_foreground, font=("Arial", 12)).pack(pady=5)
    tk.Button(scrollable_frame, text="Choose Background Color", command=choose_background, font=("Arial", 12)).pack(pady=5)

    # QR size selection
    tk.Label(scrollable_frame, text="QR Code Size:", font=("Arial", 12)).pack()
    size_var = tk.StringVar(value="10")
    size_dropdown = ttk.Combobox(scrollable_frame, textvariable=size_var, values=[5, 10, 15, 20], state="readonly")
    size_dropdown.pack(pady=5)

    # Generate QR button
    generate_btn = tk.Button(scrollable_frame, text="Generate QR", command=generate_qr, font=("Arial", 12), bg="blue", fg="white")
    generate_btn.pack(pady=10)

    # Display QR
    qr_label = tk.Label(scrollable_frame)
    qr_label.pack(pady=10)

    # Save QR buttons
    save_btn = tk.Button(scrollable_frame, text="Save as Image", command=save_qr, font=("Arial", 12), bg="green", fg="white")
    save_btn.pack(pady=5)

    # Clear fields button
    clear_btn = tk.Button(scrollable_frame, text="Clear Fields", command=clear_fields, font=("Arial", 12), bg="red", fg="white")
    clear_btn.pack(pady=5)

    # Run the interface
    root.mainloop()

# Call the function to start the GUI
create_qr_code_gui()


#/////////////////////////////////////////////////end creation QR with GUI ////////////////////////////////////////////////


"""  Call the function with the user-input data ,file name,img  """
while True:
#User Interface 
    print(Fore.RED + "📌 Automatic QR Code Generator")
    print(Fore.BLUE +"1️⃣  Generate a QR Code from manual input")
    print(Fore.BLUE +"2️⃣  Generate multiple QR Codes from a text file ")
    print(Fore.BLUE +"3️⃣  Read QR Codes from img ")
    print(Fore.BLUE +"4️⃣  Generate QR Codes with diffrent window  ")


    choice = input("🔸 Select an option (1 or 2 or 3 or 4): ").strip() # strip() to remove the space
    

    if choice == "1":
      generate_from_input()
    elif choice == "2":
      file_path = input("📂 Enter the text file path: ").strip()
      generate_from_file(file_path)
    elif choice == "3":
      QR_img = input("Enter the name of the QR image (with extension): ")
      read_from_QR_img(QR_img)
    elif choice == "4":
      
    # Ask the user if he wants to open the data entry window

      QR_win = input("Type 'start' to creat contact qr with diffrent window : ").strip().lower()
      if QR_win == "start":
       create_qr_code_gui( )  # Open QR generation window only if user types "start"
      else:
       print("you are dont write 'start' please write 'start' .")

    else:
      print(Fore.YELLOW +"⚠️ Invalid choice!")
    answer= input("Do you want to continue press 'y' or 'n'  :  ")
   

    if answer=='y':
      continue
    elif answer=='n':
      break

    else :
      while True : # while to choose y to return to menue or n to exit from program
        answer2= input("please must enter 'y'to continue or  to exit 'n'  : " )
        if answer2=='y':
           break
        if answer2=='n':
           exit(print("🚶GOOD BYE 🖐️ "))
      
print( "🎉 Execution completed!")
art_2=art("woman  ",number=2) # return multiple art as str
print(art_2)