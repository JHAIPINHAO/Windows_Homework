import tkinter as tk
from tkinter import Button , Frame

class Windows(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        frame_top = Frame(self,bg="red")

        but_1 = Button(frame_top,text="按鈕1",font=("Helvetica","24"))
        but_1.bind('<Button-1>',self.click)
        but_1.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        
        but_2 = Button(frame_top,text="按鈕2",font=("Helvetica","24"))
        but_2.bind('<Button-1>',self.click)
        but_2.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        but_3 = Button(frame_top,text="按鈕3",font=("Helvetica","24"))
        but_3.bind('<Button-1>',self.click)
        but_3.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        frame_top.pack(expand=True,fill=tk.BOTH)
        
        frame_mid = Frame(self,bg="green")
        but_4 = Button(frame_mid,text="按鈕4",font=("Helvetica","24"))
        but_4.bind('<Button-1>',self.click)
        but_4.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        but_5 = Button(frame_mid,text="按鈕5",font=("Helvetica","24"))
        but_5.bind('<Button-1>',self.click)
        but_5.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        but_6 = Button(frame_mid,text="按鈕6",font=("Helvetica","24"))
        but_6.bind('<Button-1>',self.click)
        but_6.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        frame_mid.pack(expand=True,fill=tk.BOTH)

        frame_bot = Frame(self,bg="blue")
        but_7=Button(frame_bot,text="按鈕7",font=("Helvetica","24"))
        but_7.bind('<Button-1>',self.click)
        but_7.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        but_8=Button(frame_bot,text="按鈕8",font=("Helvetica","24"))
        but_8.bind('<Button-1>',self.click)
        but_8.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        but_9=Button(frame_bot,text="按鈕9",font=("Helvetica","24"))
        but_9.bind('<Button-1>',self.click)
        but_9.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        frame_bot.pack(expand=True,fill=tk.BOTH)

    def click(self,event):
        print(event.widget['text'])


def main():
    windows = Windows()    
    windows.title("HomeWork")
    windows.geometry("400x400")
    windows.mainloop()

if __name__=="__main__":
    main()