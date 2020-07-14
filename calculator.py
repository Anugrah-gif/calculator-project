from tkinter import *
from tkinter .messagebox import  *

window=Tk()
window.title("My calc")
def all_clear():
    text_input.delete(0, END)

def back():
    ex = text_input.get()
    ex = ex[0:len(ex)-1]
    text_input.delete(0, END)
    text_input.insert(0, ex)


def click_btn(event):
    print("button clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text=='x':
        text_input.insert(END,"*")
        return



    if(text=='='):
     try:
        ex=text_input.get()
        answer=eval(ex)
        text_input.delete(0,END)
        text_input.insert(0,answer)
     except Exception as e:
        print("Error..", e)
        showerror("Error", e)
     return

    text_input.insert(END,text)


window.geometry("400x500")
font=("aerial",20)
window.config(bg="#cce0ff")
text_input=Entry(window,font=("aerial",30),justify=RIGHT,relief="sunken")
text_input.pack(fill=X,padx=10,pady=10)
buttonFrame=Frame(window,pady=10,bg="#cce0ff")
buttonFrame.pack(side=TOP)
btnC=Button(buttonFrame,text='C',font=font,justify=RIGHT,width=3,height=1,activebackground="grey",command=all_clear)
btnC.grid(row=0,column=0,padx=10,pady=10)
btnba=Button(buttonFrame,text='<-',font=font,justify=RIGHT,width=3,height=1,activebackground="grey",command=back)
btnba.grid(row=0,column=1,padx=10,pady=10)
btn7=Button(buttonFrame,text='7',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn7.grid(row=1,column=0,padx=10,pady=10)
btn8=Button(buttonFrame,text='8',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn8.grid(row=1,column=1,padx=10,pady=10)
btn9=Button(buttonFrame,text='9',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn9.grid(row=1,column=2,padx=10,pady=10)
btnplus=Button(buttonFrame,text='+',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btnplus.grid(row=1,column=3,padx=10,pady=10)
btn4=Button(buttonFrame,text='4',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn4.grid(row=2,column=0,padx=10,pady=10)
btn5=Button(buttonFrame,text='5',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn5.grid(row=2,column=1,padx=10,pady=10)
btn6=Button(buttonFrame,text='6',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn6.grid(row=2,column=2,padx=10,pady=10)
btnmul=Button(buttonFrame,text='x',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btnmul.grid(row=2,column=3,padx=10,pady=10)
btn1=Button(buttonFrame,text='1',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn1.grid(row=3,column=0,padx=10,pady=10)
btn2=Button(buttonFrame,text='2',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn2.grid(row=3,column=1,padx=10,pady=10)
btn3=Button(buttonFrame,text='3',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btn3.grid(row=3,column=2,padx=10,pady=10)
btnsub=Button(buttonFrame,text='-',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btnsub.grid(row=3,column=3,padx=10,pady=10)
zerobtn=Button(buttonFrame,text='0',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
zerobtn.grid(row=4,column=0,padx=10,pady=10)
dotbtn=Button(buttonFrame,text='.',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
dotbtn.grid(row=4,column=1,padx=10,pady=10)
equalbtn=Button(buttonFrame,text='=',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
equalbtn.grid(row=4,column=2,padx=10,pady=10)
btndivide=Button(buttonFrame,text='/',font=font,justify=RIGHT,width=3,height=1,activebackground="orange")
btndivide.grid(row=4,column=3,padx=10,pady=10)



btn7.bind('<Button-1>',click_btn)
btn8.bind('<Button-1>',click_btn)
btn9.bind('<Button-1>',click_btn)
btn4.bind('<Button-1>',click_btn)
btn5.bind('<Button-1>',click_btn)
btn6.bind('<Button-1>',click_btn)
btn1.bind('<Button-1>',click_btn)
btn2.bind('<Button-1>',click_btn)
btn3.bind('<Button-1>',click_btn)
zerobtn.bind('<Button-1>',click_btn)
equalbtn.bind('<Button-1>',click_btn)
dotbtn.bind('<Button-1>',click_btn)
btndivide.bind('<Button-1>',click_btn)
btnsub.bind('<Button-1>',click_btn)
btnmul.bind('<Button-1>',click_btn)
btnplus.bind('<Button-1>',click_btn)
window.mainloop()