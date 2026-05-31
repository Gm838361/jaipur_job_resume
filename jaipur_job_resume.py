import tkinter as tk
from tkinter import ttk
import random

class JaipurCareerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 SEON GRVSTUDENT CAREER HUB & RESUME BUILDER")
        self.root.geometry("750x650+300+80")
        self.root.configure(bg="#0A0915")
        
        # एनीमेशन का डेटा
        self.balloons = []
        self.colors = ["#FF4B4B", "#27AE60", "#2980B9", "#F1C40F", "#9B59B6", "#E67E22"]
        self.animating = False

        # --- 👑 टॉप हेडर ---
        header = tk.Label(root, text="🎓 SEON GRV STUDENT CAREER HUB", bg="#0A0915", fg="#FF4B4B", font=("Arial", 20, "bold"))

        header.pack(pady=10)
        
        subheader = tk.Label(root, text="Jobs, Placement Alerts & Instant Resume Builder", bg="#0A0915", fg="#BDC3C7", font=("Arial", 11, "italic"))
        subheader.pack(pady=2)

        # --- 📝 रिज्यूमे फॉर्म फ़्रेम ---
        form_frame = tk.Frame(root, bg="#1E222B", bd=2, relief="groove", padx=15, pady=15)
        form_frame.pack(pady=15, fill="x", padx=20)

        # फॉर्म के इनपुट बॉक्स
        tk.Label(form_frame, text="Full Name:", bg="#1E222B", fg="#FFFFFF", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(form_frame, width=25, font=("Arial", 10), bg="#2C3E50", fg="white", insertbackground="white")
        self.name_entry.insert(0, "SEON")
        self.name_entry.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="Mobile Number:", bg="#1E222B", fg="#FFFFFF", font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w", pady=5)
        self.phone_entry = tk.Entry(form_frame, width=20, font=("Arial", 10), bg="#2C3E50", fg="white", insertbackground="white")
        self.phone_entry.insert(0, "98XXX")
        self.phone_entry.grid(row=0, column=3, pady=5, padx=10)

        tk.Label(form_frame, text="College Name:", bg="#1E222B", fg="#FFFFFF", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        self.college_entry = tk.Entry(form_frame, width=25, font=("Arial", 10), bg="#2C3E50", fg="white", insertbackground="white")
        self.college_entry.insert(0, "QW")
        self.college_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="Key Skills:", bg="#1E222B", fg="#FFFFFF", font=("Arial", 10, "bold")).grid(row=1, column=2, sticky="w", pady=5)
        self.skills_entry = tk.Entry(form_frame, width=20, font=("Arial", 10), bg="#2C3E50", fg="white", insertbackground="white")
        self.skills_entry.insert(0, "Python, Streamlit")
        self.skills_entry.grid(row=1, column=3, pady=5, padx=10)

        # 🔥 जादुई बटन - रिज्यूमे भी बनाएगा और गुब्बारे भी उड़ाएगा!
        btn = tk.Button(root, text="🚀 GENERATE RESUME & CELEBRATE! 🎈", bg="#FF4B4B", fg="white", 
                        font=("Arial", 12, "bold"), bd=0, cursor="hand2", padx=20, pady=8, command=self.generate_and_celebrate)
        btn.pack(pady=5)

        # --- 🖼️ कैनवास (जहाँ गुब्बारे उड़ेंगे और रिज्यूमे दिखेगा) ---
        self.canvas = tk.Canvas(root, width=700, height=350, bg="#0E1117", highlightthickness=0)
        self.canvas.pack(pady=10, fill="both", expand=True, padx=20)
        
        # शुरुआत में कैनवास पर खाली गाइड टेक्स्ट
        self.resume_text_id = self.canvas.create_text(350, 150, text="ऊपर फॉर्म भरकर बटन दबाओ भाई, रिज्यूमे यहाँ प्रकट होगा! ✨", 
                                                      fill="#7F8C8D", font=("Arial", 12, "bold"), justify="center")

    def generate_and_celebrate(self):
        # इनपुट से डेटा निकालना
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        college = self.college_entry.get()
        skills = self.skills_entry.get()

        if not name or not phone or not college:
            self.canvas.itemconfig(self.resume_text_id, text="❌ गलती! नाम, मोबाइल और कॉलेज भरना ज़रूरी है भाई।", fill="#FF4B4B")
            return

        # 📄 रिज्यूमे का पक्का डिज़ाइन टेक्स्ट
        resume_template = f"""
============================================================
                  📄 PROFESSIONAL RESUME
============================================================
👤 FULL NAME:   {name}
📞 MOBILE:      +91 {phone}
📍 LOCATION:    Jaipur, Rajasthan

------------------------------------------------------------
🎓 EDUCATION:
------------------------------------------------------------
College:        {college}
Course:         B.Com (Commerce & Accountancy)

------------------------------------------------------------
🛠️ TECHNICAL SKILLS:
------------------------------------------------------------
Skills:         {skills}
Projects:       Built 'Gaurav Digital Store' Web Application

============================================================
        """
        # कैनवास साफ़ करके पुराना टेक्स्ट हटाना और नया रिज्यूमे छापना
        self.canvas.delete("all")
        
        # रिज्यूमे टेक्स्ट को कैनवास पर फिक्स करना
        self.canvas.create_text(350, 160, text=resume_template, fill="#FFFFFF", font=("Courier", 10, "bold"), justify="left")
        
        # 🎉 अब गुब्बारे उड़ाने की बारी!
        if not self.animating:
            self.animating = True
            for _ in range(12):
                self.create_balloon()
            self.animate()

    def create_balloon(self):
        r = random.randint(12, 22)
        x = random.randint(50, 650)
        y = random.randint(350, 550)
        speed = random.uniform(2, 4)
        color = random.choice(self.colors)
        
        oval = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline="")
        line = self.canvas.create_line(x, y+r, x, y+r+15, fill="#BDC3C7", width=1)
        
        # इन्हें नीचे (Lower) ले जाना ताकि ये रिज्यूमे टेक्स्ट के पीछे उड़ें, टेक्स्ट के ऊपर न आएँ!
        self.canvas.tag_lower(oval)
        self.canvas.tag_lower(line)
        
        self.balloons.append({"oval": oval, "line": line, "speed": speed, "x": x, "r": r})

    def animate(self):
        if not self.animating: return
        
        for b in self.balloons:
            self.canvas.move(b["oval"], 0, -b["speed"])
            self.canvas.move(b["line"], 0, -b["speed"])
            
            pos = self.canvas.coords(b["oval"])
            if pos and pos[3] < 0:
                # स्क्रीन से बाहर जाने पर वापस नीचे भेजना
                r = b["r"]
                new_x = random.randint(50, 650)
                self.canvas.moveto(b["oval"], new_x - r, 360)
                self.canvas.moveto(b["line"], new_x, 360 + r)
                b["speed"] = random.uniform(2, 4)
        
        self.root.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = JaipurCareerApp(root)
    root.mainloop()
