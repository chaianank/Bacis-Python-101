from tkinter import *
from tkinter import ttk
#from tkinter import font as tkFont
from tkinter import messagebox
import tkinter as tkGUI

GUI = tkGUI.Tk()
GUI.title('Basic Calculator')
##GUI.geometry('350x400')
GUI.rowconfigure([0,1,2,3,4,5],minsize=60)
GUI.columnconfigure([0,1,2,3,4],minsize=30)

mark = ['']
num = [0,0]
memory=['']

ent_result = ttk.Entry(GUI,font=('Time',60,'bold'),justify=RIGHT,width='9')
ent_result.insert(0,'0')
ent_result.grid(row=0,column=0,columnspan=5)

def on_btn_clear_click():
    ent_result.delete(0,tkGUI.END)
    ent_result.insert(0,'0')

def on_btn_del_click():
        ent_result.delete(len(str(ent_result.get()))-1)
        check_zero()
    
def check_zero():
    symbol = ent_result.get()
    if symbol == '0'  :
        ent_result.delete(0,tkGUI.END)
    elif symbol == ''  :
        ent_result.insert(0,'0')
    elif symbol == '+' or symbol == '-' or symbol=='*' or symbol=='/' :
        ent_result.delete(0,tkGUI.END)

def plus(x,y):
    sum = float(x) + float(y)
    return(sum)
def minus(x,y):
    sum = float(x) - float(y)
    return(sum)
def multply(x,y):
    sum = float(x) * float(y)
    return(sum)
def devide(x,y):
    sum = float(x) / float(y)
    return(sum)

def on_btn_plus_click():
    mark[0] = '+'
    num[0] = ent_result.get()
    ent_result.delete(0,tkGUI.END)
    ent_result.insert(0,"+")
def on_btn_minus_click():
    mark[0] = '-'
    num[0] = ent_result.get()
    ent_result.delete(0,tkGUI.END)
    ent_result.insert(0,"-")
def on_btn_multiply_click():
    mark[0] = '*'
    num[0] = ent_result.get()
    ent_result.delete(0,tkGUI.END)
    ent_result.insert(0,"*")
def on_btn_devide_click():
    mark[0] = '/'
    num[0] = ent_result.get()
    ent_result.delete(0,tkGUI.END)
    ent_result.insert(0,"/")
def on_btn_power_click():
    sum = float(ent_result.get()) ** 2
    ent_result.delete(0,tkGUI.END)
    ent_result.insert(0,str(sum))



def on_btn_sum_click():
    num[1] = ent_result.get()
    if mark[0] == '+':
        ent_result.delete(0,tkGUI.END)
        ent_result.insert(0,plus(num[0],num[1]))
    elif mark[0] == '-':
        ent_result.delete(0,tkGUI.END)
        ent_result.insert(0,str(minus(num[0],num[1])))
    elif mark[0] == '*':
        ent_result.delete(0,tkGUI.END)
        ent_result.insert(0,str(multply(num[0],num[1])))
    elif mark[0] == '/':
        ent_result.delete(0,tkGUI.END)
        ent_result.insert(0,str(devide(num[0],num[1])))    


def on_btn_1_click():
    check_zero()
    ent_result.insert(tkGUI.END,'1')
def on_btn_2_click():
    check_zero()
    ent_result.insert(tkGUI.END,'2')
def on_btn_3_click():
    check_zero()
    ent_result.insert(tkGUI.END,'3')
def on_btn_4_click():
    check_zero()
    ent_result.insert(tkGUI.END,'4')
def on_btn_5_click():
    check_zero()
    ent_result.insert(tkGUI.END,'5')
def on_btn_6_click():
    check_zero()
    ent_result.insert(tkGUI.END,'6')
def on_btn_7_click():
    check_zero()
    ent_result.insert(tkGUI.END,'7')
def on_btn_8_click():
    check_zero()
    ent_result.insert(tkGUI.END,'8')
def on_btn_9_click():
    check_zero()
    ent_result.insert(tkGUI.END,'9')  
def on_btn_0_click():
    check_zero()
    ent_result.insert(tkGUI.END,'0')   
def on_btn_dot_click():
    ent_result.insert(tkGUI.END,'.') 
    

btn_1 = ttk.Button(master=GUI,text='1',command=on_btn_1_click)
btn_1.grid(row=2,column=0,sticky='nsew')
btn_2 = ttk.Button(master=GUI,text='2',command=on_btn_2_click)
btn_2.grid(row=2,column=1,sticky='nsew')
btn_3 = ttk.Button(master=GUI,text='3',command=on_btn_3_click)
btn_3.grid(row=2,column=2,sticky='nsew')
btn_4 = ttk.Button(master=GUI,text='4',command=on_btn_4_click)
btn_4.grid(row=3,column=0,sticky='nsew')
btn_5 = ttk.Button(master=GUI,text='5',command=on_btn_5_click)
btn_5.grid(row=3,column=1,sticky='nsew')
btn_6 = ttk.Button(master=GUI,text='6',command=on_btn_6_click)
btn_6.grid(row=3,column=2,sticky='nsew')
btn_7 = ttk.Button(master=GUI,text='7',command=on_btn_7_click)
btn_7.grid(row=4,column=0,sticky='nsew')
btn_8 = ttk.Button(master=GUI,text='8',command=on_btn_8_click)
btn_8.grid(row=4,column=1,sticky='nsew')
btn_9 = ttk.Button(master=GUI,text='9',command=on_btn_9_click)
btn_9.grid(row=4,column=2,sticky='nsew')
btn_0 = ttk.Button(master=GUI,text='0',command=on_btn_0_click)
btn_0.grid(row=5,column=1,sticky='nsew')
btn_dot = ttk.Button(master=GUI,text='.',command=on_btn_dot_click)
btn_dot.grid(row=5,column=2,sticky='nsew')
btn_clear = ttk.Button(GUI,text="C",command=on_btn_clear_click)
btn_clear.grid(row=1,column=0,sticky='nwes')
btn_del = ttk.Button(GUI,text="<---",command=on_btn_del_click)
btn_del.grid(row=1,column=1,columnspan=2,sticky='nswe')
btn_sumary = ttk.Button(GUI,text="=",command=on_btn_sum_click)
btn_sumary.grid(row=4,column=3,columnspan=2,rowspan=2,sticky='nswe')
btn_plus = ttk.Button(GUI,text="+",command=on_btn_plus_click)
btn_plus.grid(row=2,column=4,rowspan=2,sticky='nsew')
btn_minus = ttk.Button(GUI,text="-",command=on_btn_minus_click)
btn_minus.grid(row=1,column=4,sticky='nsew')
btn_multiply = ttk.Button(GUI,text="x",command=on_btn_multiply_click)
btn_multiply.grid(row=3,column=3,sticky='nsew')
btn_divid = ttk.Button(GUI,text='/',command=on_btn_devide_click)
btn_divid.grid(row=2,column=3,sticky='nsew')
btn_power2 = ttk.Button(GUI,text='^2',command=on_btn_power_click)
btn_power2.grid(row=1,column=3,sticky='nswe')


GUI.mainloop()
