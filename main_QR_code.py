from art import * 
from colorama import Fore , Back , Style
import os
import qrcode
from datetime import datetime

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
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        if not lines:
            print("⚠️ The file is empty!")
            return
        
        for index, line in enumerate(lines):
            data = line.strip()
            if data:
                filename = f"qr_{index+1}.png"
                generate_qr(data, filename)

    except FileNotFoundError:
        print("❌ File not found!")
while True:
# User Interface
    print(Fore.RED + "📌 Automatic QR Code Generator")
    print(Fore.BLUE +"1️⃣ Generate a QR Code from manual input")
    print(Fore.BLUE +"2️⃣ Generate multiple QR Codes from a text file (one per line)")
    choice = input("🔸 Select an option (1 or 2): ").strip()

    if choice == "1":
      generate_from_input()
    elif choice == "2":
      file_path = input("📂 Enter the text file path: ").strip()
      generate_from_file(file_path)
    else:
      print(Fore.YELLOW +"⚠️ Invalid choice!")
    answer= input("Do you want to continue press 'y' or 'n'  :  ")
    if answer=='y':
      continue
    else:
      break
print( "🎉 Execution completed!")
art_2=art("woman  " ,number=2) # return multiple art as str
print(art_2)