from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("System")
root.geometry("900x650")
root.configure(bg="#0B1120")
root.resizable(False,False)

# ================= LOGIN =================

def login():

    email=email_entry.get()
    password=password_entry.get()

    if email=="" or password=="":
        messagebox.showerror("Error","All fields required")
        return

    if "@" not in email:
        messagebox.showerror("Error","Invalid Email")
        return

    messagebox.showinfo("Success","Login Successful")

    open_dashboard()


def toggle():

    if password_entry.cget('show')=="*":
        password_entry.config(show="")
        show_btn.config(text="Hide")

    else:
        password_entry.config(show="*")
        show_btn.config(text="Show")


# ================= DASHBOARD =================

def open_dashboard():

    dash=Toplevel(root)
    dash.geometry("900x650")
    dash.title("Student Details")
    dash.configure(bg="#0B1120")

    border=Frame(dash,
                 bg="#3B82F6",
                 width=720,
                 height=520,
                 relief="groove",
                 bd=4)

    border.place(relx=0.5,rely=0.5,anchor="center")

    card=Frame(border,
               bg="#0E2642",
               width=700,
               height=500)

    card.place(relx=0.5,rely=0.5,anchor="center")

    Label(card,
          text="Student Details Form",
          font=('Arial',22,'bold'),
          bg="white",
          fg="#0B1120").pack(pady=20)

    form=Frame(card,bg="white")
    form.pack(pady=10)

    Label(form,text="Full Name",
          font=('Arial',13,'bold'),
          bg="white",
          width=12,
          anchor="w").grid(row=0,column=0,padx=20,pady=10)

    name=Entry(form,
               font=('Arial',13),
               width=28,
               relief="sunken",
               bd=3)

    name.grid(row=0,column=1,pady=10)

    Label(form,text="Age",
          font=('Arial',13,'bold'),
          bg="white",
          width=12,
          anchor="w").grid(row=1,column=0,padx=20,pady=10)

    age=Entry(form,
              font=('Arial',13),
              width=28,
              relief="sunken",
              bd=3)

    age.grid(row=1,column=1,pady=10)

    Label(form,text="Course",
          font=('Arial',13,'bold'),
          bg="white",
          width=12,
          anchor="w").grid(row=2,column=0,padx=20,pady=10)

    course=ttk.Combobox(form,
                        values=["B.Tech","BCA","MCA","MBA"],
                        width=26)

    course.grid(row=2,column=1,pady=10)

    Label(form,text="Skills",
          font=('Arial',13,'bold'),
          bg="white",
          width=12,
          anchor="w").grid(row=3,column=0,padx=20,pady=10)

    skill_frame=Frame(form,bg="white")
    skill_frame.grid(row=3,column=1,pady=10,sticky="w")

    py=IntVar()
    java=IntVar()

    Checkbutton(skill_frame,
                text="Python",
                variable=py,
                bg="white").pack(side=LEFT,padx=10)

    Checkbutton(skill_frame,
                text="Java",
                variable=java,
                bg="white").pack(side=LEFT,padx=10)

    Label(form,text="Address",
          font=('Arial',13,'bold'),
          bg="white",
          width=12,
          anchor="nw").grid(row=4,column=0,padx=20,pady=10)

    address=Text(form,
                 width=30,
                 height=4,
                 relief="sunken",
                 bd=3)

    address.grid(row=4,column=1,pady=10)

    Button(card,
           text="Submit",
           bg="#04264D",
           fg="white",
           font=('Arial',13,'bold'),
           width=20,
           relief="raised",
           bd=3).pack(pady=30)


# ================= LOGIN UI =================

border=Frame(root,
             bg="#3B82F6",
             width=420,
             height=500,
             relief="groove",
             bd=4)

# PERFECT CENTER
border.place(relx=0.5,
             rely=0.5,
             anchor="center")

login_card=Frame(border,
                 bg="#9EBEF1",
                 width=480,
                 height=500)

login_card.place(relx=0.5,
                 rely=0.5,
                 anchor="center")

top=Frame(login_card,bg="white")
top.pack(pady=20)

try:
    img = Image.open(r"C:\Users\ommah\Downloads\911.jpg")
    img = img.resize((100,90))
    logo = ImageTk.PhotoImage(img)

    Label(top,
          image=logo,
          bg="white").pack()

except:
    Label(top,
          text="⭐",
          font=('Arial',40),
          bg="#2269BA",
          fg="gold").pack()

Label(top,
      text="911 planning",
      font=('Arial',22,'bold'),
      bg="white").pack()

Label(login_card,
      text="Email",
      font=('Arial',13,'bold'),
      bg="white").pack()

email_entry=Entry(login_card,
                  font=('Arial',13),
                  width=28,
                  relief="sunken",
                  bd=3)

email_entry.pack(pady=10,ipady=4)

Label(login_card,
      text="Password",
      font=('Arial',13,'bold'),
      bg="white").pack()

pass_frame=Frame(login_card,bg="white")
pass_frame.pack()

password_entry=Entry(pass_frame,
                     font=('Arial',13),
                     width=22,
                     show="*",
                     relief="sunken",
                     bd=3)

password_entry.pack(side=LEFT,ipady=4)

show_btn=Button(pass_frame,
                text="Show",
                command=toggle,
                relief="raised",
                bd=2)

show_btn.pack(side=LEFT,padx=5)

Checkbutton(login_card,
            text="Remember me",
            bg="white").pack(pady=10)

Button(login_card,
       text="Login",
       bg="#3B82F6",
       fg="white",
       font=('Arial',15,'bold'),
       width=18,
       relief="raised",
       bd=3,
       command=login).pack(pady=25)

root.mainloop()
