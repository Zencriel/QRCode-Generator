import customtkinter as ctk
import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def mistermaker():
    myurl = ururl.get().strip()
    if not myurl:
        yetanothersticker.configure(text="check your url")
        return
    var1 = qrcode.QRCode()
    var1.add_data(myurl)
    to_return = var1.make_image()
    filepath = "urqrbro.png"  # u can replace this with ur desired absolute path for ur own use
    try:
        to_return.save(filepath)
    except Exception as e:
        yetanothersticker.configure(text=f"Error saving QR: {e}")
        return

    img = Image.open(filepath)
    annoyingpopup = ctk.CTkToplevel(plslookhere)
    annoyingpopup.title("Qr code")

    popup_img = ctk.CTkImage(light_image=img,dark_image=img,size=(200, 200))
    qr_label = ctk.CTkLabel(annoyingpopup,image=popup_img, text="")
    qr_label.image = popup_img
    qr_label.pack(padx=20, pady=20)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

plslookhere = ctk.CTk()
plslookhere.title("QR Code Generator")
plslookhere.geometry("600x400")
plslookhere.resizable(True, True)

bg_canvas = tk.Canvas(plslookhere,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
retreive = Image.open("Aqualicious.png")
bakgroudn = ImageTk.PhotoImage(retreive)
bg_canvas.create_image(0, 0, image=bakgroudn, anchor="nw")

lookatthis = ctk.CTkFrame(bg_canvas,bg_color="#559CAD",width=400,height=200)
lookatthis.place(relx=0.5,rely=0.5,anchor="center")
sticker = ctk.CTkLabel(lookatthis,text="Enter a URL",font=("Bahnschrift",25,"bold"))
sticker.pack(pady=(20, 10))

ururl = ctk.CTkEntry(lookatthis,placeholder_text="https://example.com",width=290,height=35,font=("Bahnschrift", 18))
ururl.pack(pady=10)
only_button = ctk.CTkButton(lookatthis,fg_color="#C99DA3",text="Generate",font=("Bahnschrift", 14),width=180,height=45,hover_color="#305252",command=mistermaker)
only_button.pack(pady=20)

yetanothersticker = ctk.CTkLabel(lookatthis,text="",font=("Bahnschrift", 12))
yetanothersticker.pack(pady=(0, 10))

plslookhere.mainloop()
