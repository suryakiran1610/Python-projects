from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


def convert(text="type", src="english", dest="hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def get_data():
    s = combobox1.get()
    d = combobox2.get()
    msg = source_text.get(1.0, END)
    text_get = convert(text=msg, src=s, dest=d)
    destination_text.delete(1.0, END)
    destination_text.insert(END, text_get)



root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="Red")

labe1=Label(root,text="Translator",font=("times New Roman",40,"bold"))
labe1.place(x=100,y=30,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

label2 = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="black", bg="red")
label2.place(x=100, y=100, height=20, width=300)


source_text=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
source_text.place(x=10,y=150,height=150,width=480)

list_language=list(LANGUAGES.values())

combobox1=ttk.Combobox(frame,value=list_language)
combobox1.place(x=10,y=320,height=40,width=150)
combobox1.set("english")

button1=Button(frame,text="Translate",relief=RAISED,command = get_data)
button1.place(x=170,y=320,height=40,width=150)

combobox2=ttk.Combobox(frame,value=list_language)
combobox2.place(x=330,y=320,height=40,width=150)
combobox2.set("english")

label3= Label(root, text="Destination text", font=("Times New Roman", 20, "bold"), fg="black", bg="red")
label3.place(x=120, y=400, height=20, width=300)

destination_text=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
destination_text.place(x=10,y=460,height=180,width=480)




root.mainloop()

