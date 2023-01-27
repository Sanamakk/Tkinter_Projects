from tkinter import *
from tkinter import ttk
from datetime import date
from tkinter.messagebox import showerror

main = Tk()

def age_Calculating():
    try:
        today_date = date.today()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = (year,month,day)
        age = today_date.year-birth_date.year-((today_date.month,today_date.day)<(birth_date.month, birth_date.day))
        age_result.configure(f'You are {str(age)} Years old')
    except:
        showerror(title='Error',message='We face a issue while calculating your age')

main.title("Age Calculator")
main.geometry("500x260+430+300")
main.resizable(False,False)

canvas = Canvas(main, width=500,height=400)
canvas.pack()
Label_style = ttk.Style()
Label_style.configure('TLabel',foreground ='#000000',font=('Dontumche',16))

button_style = ttk.Style()
button_style.configure('TButton',foreground='#0000000',font=('Dontumche',14))

entry_style = ttk.Style()
entry_style.configure('TEntry',font='Dontum,15')

main_label = Label(main,text='Age Calculator',font=('OCR A EXTEND',25))

canvas.create_window(245,40,window=main_label)

day_label = ttk.Label(main,text='Day',style='TLabel')
day_entry = ttk.Entry(main,width=15,style='TEntry')

month_label = ttk.Label(main,text='Month',style='TLabel')
month_entry = ttk.Entry(main,width=15,style='TEntry')

year_label = ttk.Label(main,text='Year',style='TLabel')
year_entry = ttk.Entry(main,width=15,style='TEntry')

calculate_button = ttk.Button(main,text='Cauculate age',style='TButton',command= age_Calculating)

age_result = ttk.Label(main, text= '', style='TLabel')

canvas.create_window(114,100,window=day_label)
canvas.create_window(130,130,window=day_entry)

canvas.create_window(250,100,window=month_label)
canvas.create_window(245,130,window=month_entry)

canvas.create_window(350,100,window=year_label)
canvas.create_window(360,130,window=year_entry)

canvas.create_window(245,220,window=calculate_button)


calculate_button = ttk.Button(main,text='Cauculate age',style='TButton',command= age_Calculating)
main.mainloop()




































