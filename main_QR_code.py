from art import * 
from colorama import Fore , Back , Style
import os
import qrcode
from datetime import datetime
from PIL import Image
import cv2


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
               generate_qr(data,filename)

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

"""  Call the function with the user-input data ,file name,img  """
while True:
#User Interface 
    print(Fore.RED + "📌 Automatic QR Code Generator")
    print(Fore.BLUE +"1️⃣  Generate a QR Code from manual input")
    print(Fore.BLUE +"2️⃣  Generate multiple QR Codes from a text file (one per line)")
    print(Fore.BLUE +"3️⃣  Generate QR Codes from img ")

    choice = input("🔸 Select an option (1 or 2 or 3): ").strip() # strip() to remove the space

    if choice == "1":
      generate_from_input()
    elif choice == "2":
      file_path = input("📂 Enter the text file path: ").strip()
      generate_from_file(file_path)
    elif choice == "3":
      QR_img = input("Enter the name of the QR image (with extension): ")
      read_from_QR_img(QR_img)
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