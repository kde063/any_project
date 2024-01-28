from tkinter import *

expression = "" #변수 선언

def press(num):  #버튼 명령어

    global expression
 
    expression = expression + str(num) #변수값 수정
 
    equation.set(expression)  #변수 입력란에 출력

 
def equalpress():  #결과버튼 명령어

    try:  #사칙연산 가능할경우(정상작동)
 
        global expression

        total = str(eval(expression))  #변수값 사칙연산후 문자열 변환후 출력
 
        equation.set(total)  #입력란에 출력

        expression = ""  #변수 설정
 

    except: #아닐 경우(에러날경우)
 
        equation.set(" error ") #error 출력
        expression = "" #변수 설정


def clear(): #clear 버튼 명령어
    global expression 
    expression = ""  #변수 값 설정
    equation.set("") # 입력창에 ""출력(아무것도 없음)

 

if __name__ == "__main__":

    gui = Tk()  #창 생성
 
    gui.configure(background="pink",bd=2)  #창 색깔
 
    gui.title("Simple Calculator")  #창 이름
 
    gui.geometry("270x150")  #창 크기
 
    equation = StringVar()
 
    expression_field = Entry(gui, textvariable=equation) #입력창
 
    expression_field.grid(columnspan=4, ipadx=70)  #입력창 배치
 
    button1 = Button(gui, text=' 1 ', fg='black', bg='white',
                    command=lambda: press(1), height=1, width=7)  #숫자1버튼
    button1.grid(row=2, column=0)                                 #버튼 배치
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='white',
                    command=lambda: press(2), height=1, width=7)   #숫자2버튼
    button2.grid(row=2, column=1)                                  #버튼 배치
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='white',
                    command=lambda: press(3), height=1, width=7)   #숫자3버튼
    button3.grid(row=2, column=2)                                  #버튼 배치
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='white',
                    command=lambda: press(4), height=1, width=7)   #숫자4버튼
    button4.grid(row=3, column=0)                                  #버튼 배치
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='white',
                    command=lambda: press(5), height=1, width=7)   #숫자5버튼
    button5.grid(row=3, column=1)                                  #버튼 배치
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='white',
                    command=lambda: press(6), height=1, width=7)   #숫자6버튼
    button6.grid(row=3, column=2)                                  #버튼 배치
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='white',
                    command=lambda: press(7), height=1, width=7)   #숫자7버튼
    button7.grid(row=4, column=0)                                  #버튼 배치
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='white',
                    command=lambda: press(8), height=1, width=7)   #숫자8버튼
    button8.grid(row=4, column=1)                                  #버튼 배치
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='white',
                    command=lambda: press(9), height=1, width=7)   #숫자9버튼
    button9.grid(row=4, column=2)                                  #버튼 배치
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='white',
                    command=lambda: press(0), height=1, width=7)   #숫자0버튼
    button0.grid(row=5, column=0)                                  #버튼 배치
 
    plus = Button(gui, text=' + ', fg='black', bg='white',
                command=lambda: press("+"), height=1, width=7)   #더하기 버튼
    plus.grid(row=2, column=3)                                   #버튼 배치
 
    minus = Button(gui, text=' - ', fg='black', bg='white',
                command=lambda: press("-"), height=1, width=7)   #뺘기 버튼
    minus.grid(row=3, column=3)                                  #버튼 배치
 
    multiply = Button(gui, text=' * ', fg='black', bg='white',
                    command=lambda: press("*"), height=1, width=7)   #곱하기버튼
    multiply.grid(row=4, column=3)                                   #버튼 배치
 
    divide = Button(gui, text=' / ', fg='black', bg='white',
                    command=lambda: press("/"), height=1, width=7)   #나누기 버튼
    divide.grid(row=5, column=3)                                     #버튼 배치
 
    equal = Button(gui, text=' = ', fg='black', bg='white',
                command=equalpress, height=1, width=7)   #결과 버튼
    equal.grid(row=5, column=2)                          #버튼 배치
 
    clear = Button(gui, text='Clear', fg='black', bg='white',
                command=clear, height=1, width=7)   #clear 버튼
    clear.grid(row=5, column='1')                    #버튼 배치
 
    Decimal= Button(gui, text='.', fg='black', bg='white',
                    command=lambda: press('.'), height=1, width=7)   #.버튼
    Decimal.grid(row=6, column=0)                                    #버튼 배치

    gui.mainloop() #창시작