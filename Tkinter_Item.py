import customtkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

app=customtkinter.CTk()
app.title('Products')
app.geometry('400x200')
app.config(bg='#24344f')

font1=('Arial',15,"bold")

db=sqlite3.connect('items.db')
db.execute("CREATE TABLE IF NOT EXISTS PRODUCTS (Product_ID integer, Operating_System TEXT)")
cursor = db.cursor()

def insert():
    row=[int(product_entry.get()),os_entry.get()]
    cursor.execute('INSERT into PRODUCTS values (?,?)',row)
    db.commit()
    messagebox.showinfo(title='Saved',message='Item is saved')
    
def delete():
    cursor.execute('DELETE from PRODUCTS WHERE Product_ID=?',[product_entry.get()])
    db.commit()
    messagebox.showinfo(title='Deleted',massage='Item is deleted')

product_label = customtkinter.CTkLabel(app,text="Product_ID",font=font1,text_color="#FFFFFF")
product_label.place(x=5 ,y=10)

product_entry = customtkinter.CTkEntry(app,border_width=1,font=font1,text_color='#000000',border_color='#FFFFFF',fg_color='#FFFFFF',width=150)
product_entry.place(x=190,y=10)

os_label = customtkinter.CTkLabel(app, text='Operating System:',font=font1,text_color='#FFFFFF')
os_label.place(x=5,y=70)


os_entry = customtkinter.CTkEntry(app,border_width=1,text_color='#000000',font=font1,border_color='#FFFFFF',fg_color='#FFFFFF',width=150)
os_entry.place(x=190,y=70)

save_button = customtkinter.CTkButton(app, command=insert,text='Save',fg_color='#189614',font=font1,hover_color='#189614')
save_button.place(x=30,y=150)

delete_button = customtkinter.CTkButton(app, command=delete,text='Delete',fg_color='#c7580e',font=font1,hover_color='#c7580e')
delete_button.place(x=180,y=150)
 
app.mainloop()

