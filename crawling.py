from bs4 import BeautifulSoup
import urllib.request as req
from urllib.parse import quote
from tkinter import *
from time import sleep

def date_where():
    global where
    where = quote(Entry_where.get())
    where_input = Entry_where.get()
    try:
        weather = quote("날씨")
        url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="+ where+weather
        res = req.urlopen(url)
        soup = BeautifulSoup(res,"html.parser")
        lowest = soup.find('span',{'class':'lowest'}).get_text()
        highest = soup.find('span',{'class':'highest'}).get_text()
        date= soup.find('span',{'class':'date'}).get_text()
        where_input = soup.find('h2',{'class':'title'}).get_text()
        now = soup.find('span',{'class':'blind'})[2].text()


        label_where.config(text="지역:"+where_input)
        label_date.config(text="날짜:"+date)
        label_highest.config(text=highest)
        label_lowest.config(text=lowest)
        label_now.config(text=now)
    except:
        error = StringVar()
        Entry_where.config(textvariable=error)
        error.set("error")

    
if __name__ == "__main__":
    where =" "    

    wid = Tk()  #creat window

    wid.title("weather")  #window name

    wid.geometry("500x300")  #window size
    #explain what to do at Entry_where
    label_explain = Label(text="지역을 입력하세요")
    label_explain.grid(row=0,column=0)
    
    Entry_where = Entry(wid) #입력창
    Entry_where.grid(row=0,column=1)
    
    #print date_where
    label_where = Label(wid,text="지역:",width=15) ;label_where.grid(row=2,column=0)
    label_date = Label(wid,text="날짜:",width=15) ;label_date.grid(row=3,column=0)
    label_now = Label(wid,text="현재기온:",width=15) ;label_now.grid(row=4,column=0)
    label_highest = Label(wid,text="최고기온:",width=15) ;label_highest.grid(row=5,column=0)
    label_lowest = Label(wid,text="최저기온:",width=15) ;label_lowest.grid(row=6,column=0)
    #change label_where`s text
    button = Button(wid,command=date_where,width=2,text="확인")
    button.grid(row=0,column=2)
    
    wid.mainloop()
