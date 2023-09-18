from  tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s  /t 1")        

st =Tk()
st.title("shutdown API")
st.geometry("500x500")
st.config(bg="Yellow")

restart_button = Button(st,text="RESTART",font=("ADLaM Display",30,"bold"),
            relief=RAISED,cursor="plus",command=restart)
restart_button.place(x=150,y=60,height=50,width=200)

logout_button = Button(st,text="LOGOUT",font=("ADLaM Display",30,"bold"),
            relief=RAISED,cursor="plus",command=logout)
logout_button.place(x=150,y=170,height=50,width=200)

shutdown_button = Button(st,text="SHUTDOWN",font=("ADLaM Display",30,"bold"),
            relief=RAISED,cursor="plus",command=shutdown)
shutdown_button.place(x=150,y=270,height=60,width=250)





st.mainloop()