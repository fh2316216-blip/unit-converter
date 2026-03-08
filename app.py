import customtkinter as ctk
from PIL import Image, ImageDraw
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Fares Converter")
app.geometry("500x450")

# عمل الصورة دائرية
def make_circle(path):
    img = Image.open(path).resize((90,90))
    
    mask = Image.new("L",(90,90),0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0,90,90),fill=255)
    
    img.putalpha(mask)
    return img

# تحميل الصورة
profile_img = None

if os.path.exists("profile.png"):
    img = make_circle("profile.png")
    profile_img = ctk.CTkImage(img,size=(90,90))

# إطار علوي
top = ctk.CTkFrame(app,fg_color="transparent")
top.pack(pady=20)

avatar = ctk.CTkLabel(top,image=profile_img,text="")
avatar.pack()

title = ctk.CTkLabel(app,text="Unit Converter",font=("Arial",32,"bold"))
title.pack(pady=10)

def convert():
    try:
        value=float(entry.get())
        
        if option.get()=="Feet → Meters":
            result=value*0.3048
            result_label.configure(text=f"{result:.2f} meters")
            
        else:
            result=value/0.3048
            result_label.configure(text=f"{result:.2f} feet")
            
    except:
        result_label.configure(text="Enter number")

entry = ctk.CTkEntry(app,width=260,height=45,placeholder_text="Enter value")
entry.pack(pady=25)

option = ctk.CTkOptionMenu(app,values=["Feet → Meters","Meters → Feet"],width=200)
option.pack()

button = ctk.CTkButton(app,text="Convert",command=convert,width=220,height=45)
button.pack(pady=25)

result_label = ctk.CTkLabel(app,text="",font=("Arial",26,"bold"))
result_label.pack()

footer = ctk.CTkLabel(app,text="Created by Fares Hamed")
footer.pack(side="bottom",pady=10)

app.mainloop()
