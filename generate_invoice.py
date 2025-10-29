from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import datetime
import textwrap
import qrcode
import sys
import os

def create_invoice(filename, medicines):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    #add logo here
     
    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 50, "Shop Invoice maker by LakshaySharma") 

    # Shop Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 100, "Shop Name: xxxxxxxxxxxxxxxxxx")

    c.drawString(50, height - 125, "Address: xxxxxxxxxxxxxxxxxxxxxxxxxxx")
    c.drawString(50, height - 140, "                XXXXXXXXXXXXXXXXXXXX")
   
    # add the contact number and gstin number were
    c.drawString(50, height - 170, "Contact: +91 ______________")
    c.drawString(50, height - 190, "GSTIN: -_____________________")
    
    #Receive Details Input code
    Receiver_name=input("Enter Receiver Name: ")
    Delivery_address1=input("Enter 50% Delivrery Address: ")
    Delivery_address2=input("Enter 50% Delivrery Address: ")
    contact = input("Enter Contact Number: ")
    while len(contact) != 10 or not contact.isdigit():
     print("Error! Invalid Phone Number. Please enter a 10-digit number.")
     contact = input("Enter Contact Number: ")

    # Receiver Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(325, height - 100, f"Receiver Name:{Receiver_name}")
    c.drawString(325, height - 125, f"Delivery Address: {Delivery_address1}")
    c.drawString(330, height - 140, f"{Delivery_address2}")
    c.drawString(325, height - 160, f"Contact: +91{contact}")

    # Table Headers
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 250, "Medicine Name")
    c.drawString(200, height - 250, "Quantity")
    c.drawString(300, height - 250, "Price")
    c.drawString(400, height - 250, "Total")

    # Table Data
    y = height - 270
    for medicine, qty, price in medicines:
        c.setFont("Helvetica", 12)
        c.drawString(60, y, medicine)
        c.drawString(220, y, str(qty))
        c.drawString(320, y, f"Rs.{price:.2f}")
        c.drawString(420, y, f"Rs.{qty * price:.2f}")
        y -= 20

    # Total Calculation
    subtotal = sum(qty * price for _, qty, price in medicines)
    discount = subtotal * 0.1
    gst = (subtotal - discount) * 0.18
    grand_total = subtotal - discount + gst

    # Totals and Discounts
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Subtotal: Rs.{subtotal:.2f}")
    c.drawString(50, y - 40, f"Discount (10%): -Rs.{discount:.2f}")
    c.drawString(50, y - 60, f"GST (18%): +Rs.{gst:.2f}")
    c.drawString(50, y - 80, f"Grand Total: Rs.{grand_total:.2f}")

    # QR Code
    #Example of a UPI QR code:
    # pa= → Payee VPA/UPI ID
    # pn= → Payee Name (Your business name)
    # am= → Amount to be Paid
    # cu= → Currency Code (INR for Indian Rupee)
    # upi://pay?pa=<UPI_ID>&pn=<Payee Name>&am=<Amount>&cu=INR
    qr_data = f"upi://pay?pa=<UPI_ID>&pn=<Payee Name>&am={grand_total:.2f}&cu=INR"
    qr = qrcode.make(qr_data)
    qr.save("qrcode.png")

    try:
        qr_img = ImageReader("qrcode.png")
        c.drawImage(qr_img, 400, y - 100, width=80, height=80)
    except Exception:
        c.drawString(400, y - 100, "QR Code Missing")
     
    x = datetime.datetime.now()
    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 30, "Thank you for choosing Jai Maa Medicos!")
    c.drawString(400, 30, f"Date & Time: {x}")

    # Save the PDF
    c.save()



    # Clean up QR Code Image
if os.path.exists("qrcode.png"):
        os.remove("qrcode.png")

# Collect Medicines Data Dynamically
medicines = []
n = int(input("Enter the number of medicines: "))

for i in range(n):
    name = input(f"Enter medicine {i + 1} name: ")
    qty = int(input(f"Enter quantity for {name}: "))
    price = float(input(f"Enter price for {name}: "))
    medicines.append((name, qty, price))
# Display Medicine List
print("\nMedicine List:")
for item in medicines:
    print(item)
  
ans=input("Do you want to edit the list ? (yes/no): ")
if ans.lower() == "yes":
    print("\nMedicine List:")
    for i in range(n):
        print(f"{i+1}. {medicines[i]}")
    index = int(input("Enter the index of the medicine you want to edit: "))
    name = input("Enter new medicine name: ")
    qty = int(input("Enter new quantity: "))
    price = float(input("Enter new price: "))
    medicines[index-1] = (name, qty, price)
    print("\nUpdated Medicine List:")
    for item in medicines:
        print(item)
elif ans.lower() == "no":
    pass
   # Generate the invoice
invoice_name = input("Enter the invoice name: ")
create_invoice(f"{invoice_name}-invoice of in .pdf", medicines)
print("PDF created successfully!")