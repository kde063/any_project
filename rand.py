from tkinter import *
from time import sleep
from random import randint
wid = Tk()
wid.geometry("500x200")
wid.resizable(False, False)
global num
num = 0
a = list()

#cammond
def start():
    pass

def get():
    global num_first
    global num_last
    num_first = start_text.get()   
    num_last = end_text.get()
    
def rand():    
    try:
        if type(int(num_first)) == int:
            if type(int(num_last)) == int:
                if int(num_first)<int(num_last):   
                    num_label.config(text = randint(int(num_first),int(num_last)))
                else:
                    num_label.config(text = "마지막 수가 더 작습니다",font=("돋음", 10))
    except:
        num_label.config(text = "숫자를 입력하세요",font=("돋음", 10))


#button
start_button = Button(wid,width =5,height=2,text="start",command=rand)
button = Button(wid,width = 5,height=2,text="확인",command=get)

#Entry
start_text = Entry(wid, width=30)
end_text = Entry(wid, width=30)

#label
num_label = Label(wid,text=0,font=("돋음", 10),width=30,height=5)
start_label = Label(wid,text="처음숫자",bg="white")
end_label = Label(wid,text="마지막숫자")


#Entrt(grid)
start_text.grid(column=0, row=1)
end_text.grid(column=0,row=4)


#button(grid)
start_button.grid(column=5, row=3)
button.grid(column=4, row=3)

#label(grid)
num_label.grid(column=0, row=5)
start_label.grid(column=0, row=0)
end_label.grid(column=0, row=3)

wid.mainloop()
