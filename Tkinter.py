from tkinter import *
from PIL import ImageTk,Image




root = Tk()
root.title("BUcksers")
root.iconbitmap("pixel2.ico")

root.geometry('500x500+0+0')
root.configure(background='#00704A')

# image
img = Image.open('star.png')
resize_img = img.resize((100,70))
img = "C:\Users\ommah\Downloads\starbucks__exorcist_logo_by_dougsq_danxadq-414w-2x - Copy.jpg"(resize_img)

img_label = Label(root,image = img)
img_label.pack(pady=10,padx=20)

# text label
text_label = Label(root,text="Giet Bucks",font=('Arial', 18,'bold'),bg='#00704A',fg='white')
text_label.pack(pady=10,padx=20)

email_label = Label(root,text="Email",font=('Arial', 18,'bold'),bg='#00704A',fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='grey')
email_entry.pack(pady=(5,10))

password_label = Label(root,text="Password",font=('Arial', 18,'bold'),bg='#00704A',fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='grey')
password_entry.pack(pady=(5,10))

login_btn = Button(root,text="Login",font=('Arial', 18,'bold'),bg='#00704A',fg='white')
login_btn.pack(pady=(5,10))

 













root.mainloop()