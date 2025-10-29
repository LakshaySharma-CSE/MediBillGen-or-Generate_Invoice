
---

# 💊 MediBillGen — Smart Medicine Invoice Generator  

A lightweight and interactive **Python-based pharmacy invoice generator** built with **ReportLab** and **QRCode**.  
It helps shop owners instantly create professional PDF invoices with **discount, GST, and QR-based UPI payment support** — all in one click.  

---

## ⚙️ Features  

✅ Dynamic input for medicines and receiver details  
✅ Automatic subtotal, 10% discount, and 18% GST calculation  
✅ QR code generation for UPI payments  
✅ Editable medicine list before generating invoice  
✅ Clean, print-ready PDF design  
✅ One-click setup and run for non-tech users  

---

## 🧠 Tech Stack  

- **Python 3**  
- **ReportLab** — PDF generation  
- **QRCode** — QR payment creation  
- **datetime**, **os**, **textwrap** — built-in modules  

---

## 🧰 Installation (for Everyone)  

You can now install and run MediBillGen **without typing any commands**.  

### 🪄 Step 1: One-Time Setup  
Run `setup.bat`  
This will:  
- Create a Python virtual environment  
- Install all necessary libraries (`reportlab`, `qrcode`)  
- Prepare everything automatically  

You only need to do this **once**.  

### ▶️ Step 2: Run the Program  
After setup, just double-click `run.bat`  
It will automatically start your **invoice generator** each time you use it.  

---

### ⚠️ Important — Setting Up Your QR Code  

Before using the program for payments, you must **add your own UPI payment details** so the QR code links to your business account.  

In your file **`generate_invoice.py`**, find this line:  

```python
qr_data = f"upi://pay?pa=<UPI_ID>&pn=<Payee Name>&am={grand_total:.2f}&cu=INR"

Now, replace <UPI_ID> and <Payee Name> with your actual UPI details.

💡 How to Find Your UPI Details:

1. Open your existing business UPI QR code (for example, the one you display at your shop).


2. Scan it with Google Lens or any QR code scanner app.


3. It will show details like:

upi://pay?pa=yourupi@upi&pn=Your Business Name&cu=INR


4. Copy your UPI ID (after pa=) and Payee Name (after pn=).


5. Paste them into the code, like this:



qr_data = f"upi://pay?pa=yourupi@upi&pn=YourBusinessName&am={grand_total:.2f}&cu=INR"

✅ That’s it!
Now, your generated invoice will include a fully functional UPI QR code linked to your payment account.


---

🧩 Story Behind the Project

This project began with a simple problem — and a spark of curiosity.

I was working on a startup for a medical shop and helping with my family’s pharmacy business. While setting up the billing process, I realized that most invoice generator apps cost ₹500–₹1000 per month.
For a small business or a new startup, that felt like an unnecessary expense — especially for something that could be automated with a bit of code.

So I decided to build my own invoice generator — one that was simple, free, and efficient.

I explored libraries like ReportLab for PDFs and QRCode for payments, and gradually built this tool from scratch. It wasn’t just about saving money — it was about learning, building, and creating something useful for others like me.

What started as a small personal project soon became a tool that any pharmacy or small business could use to make professional invoices without monthly costs.

After refining and testing it, I added features like editable medicine lists, GST and discount calculations, and UPI QR support — turning it into something truly practical.

Now, I’m working to improve it further, so that every startup, stockist, or local pharmacist can use it effortlessly.


---

💡 Future Enhancements

GUI version using Tkinter or PyQt

Database storage for recurring customers

Export to CSV/Excel for analytics

Multi-page invoice support



---

👋 About Me — Lakshay Sharma

> “The people who are crazy enough to think they can change the world are the ones who do.”
— Steve Jobs



Hi, I’m Lakshay Sharma — a 19-year-old developer, dreamer, and builder on a mission to turn ideas into reality through code.

Whether it’s a web interface, an app prototype, or an automation script — I believe every line of code brings me closer to shaping the future I imagine.


---

💡 Why I Code

Technology isn't just syntax or semicolons — it’s:

🎨 A canvas for creativity

🌍 A tool for impact

⚙️ A path to innovation


If you're looking for someone who is:

💡 Endlessly curious and always learning

🧠 Obsessed with solving real problems

🤝 Eager to collaborate on bold, meaningful projects


You’re in the right place.


---

🛠 What I'm Building

This space is more than a portfolio — it's a living lab of my journey:

🔗 Projects: Real-world experiments in progress (more coming soon!)

📓 Dev Logs: Notes, breakthroughs, and the messy magic of learning

🌱 Growth: From my first Hello World to a future in Robotics, AI & Automation



---

📬 Let’s Connect

Have an idea, a project, or just want to talk code?
DM me anytime — I'm always up for building something awesome together.

📷 Instagram: @Lakshay_7_Sharma


---

⭐ If you like this project, consider giving it a star! ⭐

---
