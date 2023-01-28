import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sistema de Login")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)



#Trabalhando com a imagem da tela
# img = PhotoImage(file='images.png')
# label_img = customtkinter.CTkLabel(master=janela, image=img)
# label_img.place(x=5, y=65)

labell_tt = customtkinter.CTkLabel(master=janela,text='Entre na sua conta e acesse \na plataforma', font=('Roboto', 18), text_color='#00B0F0').place(x=10,y=10)

#Frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side= RIGHT)

#Frame widgets
label = customtkinter.CTkLabel(master= frame, text='Sistema de Login', font=('Roboto',20), text_color='white')
label.place(x=25,y=5)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text="Nome do Usuário", width=300,font=("Roboto",14)).place(x=25,y=105)
label1= customtkinter.CTkLabel(master=frame,text="*O campo nome de usuário é de carater obrigatório.",text_color="green",font=("Roboto",10)).place(x=25,y=135)
entry2 = customtkinter.CTkEntry(master = frame, placeholder_text="Senha", width=300,font=("Roboto",14)).place(x=25,y=175)
label2= customtkinter.CTkLabel(master=frame,text="*O campo senha do usuário é de carater obrigatório.",text_color="green",font=("Roboto",10)).place(x=25,y=205)

check_box = customtkinter.CTkCheckBox(master=frame,text="Lembrar").place(x=25, y=235)
button = customtkinter.CTkButton(master=frame, text="Login",width=300).place(x=25, y=285)




janela.mainloop()










