

from tkinter import Tk,Button,Label,DoubleVar,Entry

window = Tk()
window.title("feet to meter convertor")
window.configure(background="light blue")
window.geometry("320x220")
window.resizable(width=False,height=False)

def convert():
	value=float(ft_entry.get())
	meter= value * 0.3048
	mt_value.set(" %.4f" % meter)
def clear():
	ft_value.set("")
	mt_value.set("")


conv_btn=Button(window,text="Convert",bg="orange",fg="white",width=15,command=convert)
conv_btn.grid(column=0,row=2,pady=30)

clr_btn=Button(window,text="Clear",bg="black",fg="white",width=15,command=clear)
clr_btn.grid(column=1,row=2,pady=30)
	
ft_lbl=Label(window,text="Feet",bg="blue",fg="white",width=14)
ft_lbl.grid(column=0,row=0,padx=15,pady=15)

mt_lbl=Label(window,text="Meter",bg="green",fg="white",width=14)
mt_lbl.grid(column=0,row=1,padx=15,pady=15)

ft_value=DoubleVar()
ft_entry=Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0,pady=15)
ft_entry.delete(0,'end')

mt_value=DoubleVar()
mt_entry=Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,pady=15)
mt_entry.delete(0,'end')


window.mainloop() 