import tkinter,requests
from tkinter import messagebox
import json
from PIL import Image,ImageTk


SYMBOLS = ['EUR','JPY','CAD','MXN','CNY','GBP','AUD','BRL','NZD','RUB','ZAR','INR','HKD','CZK','RON','SGD','CHF','SGD','KRW','ILS','USD']
SYMBOLS_STRING = ','.join(SYMBOLS)
def convert():
    
    try:
        dollars = float(starting_currency_entry.get())
    except ValueError:
        messagebox.showerror(title='Oops',message='Please enter a NUMBER!')
        starting_currency_entry.delete(0,tkinter.END)
    else:
        base = from_variable.get()
        to = to_variable.get()
        if dollars < 0:
            messagebox.showerror(title='Oops',message='Please enter a POSITIVE NUMBER!')
            starting_currency_entry.delete(0,tkinter.END)
        else:
            url = f'https://api.exchangeratesapi.io/latest'
            d = {'base': base,'symbols': SYMBOLS_STRING}
            response = requests.get(url,params=d)
            exchange_rates = json.loads(response.text)
            
            if to == base:
                exchange_rate = 1
            else:
                exchange_rate =euros_per_dollar = exchange_rates['rates'][to]

            result = dollars * exchange_rate
            ending_currency_result['text'] = f"{result:.2f}"

     
    








window = tkinter.Tk()
window.title("Currency Converter")
window.config(padx=20,pady=20)


font = ('Courier',40,"bold")

canvas = tkinter.Canvas(width=320,height=320,highlightthickness=0)
image = Image.open('currency.png')
photo = ImageTk.PhotoImage(image)
canvas.create_image(160,160,image=photo)
canvas.grid(row=0,column=0,columnspan=2)



starting_currency_label = tkinter.Label(text="USD:",font=font)
starting_currency_label.grid(row=1,column=0,sticky=tkinter.E)


starting_currency_entry = tkinter.Entry(font=font)
starting_currency_entry.insert(0,"0.00")
starting_currency_entry.focus()
starting_currency_entry.grid(row=1,column=1,sticky=tkinter.W,padx=5)



ending_currency_label = tkinter.Label(text="EUROS:",font=font)
ending_currency_label.grid(row=2,column=0,sticky=tkinter.E)


ending_currency_result = tkinter.Label(text='0.00',font=font)
ending_currency_result.grid(row=2,column=1,sticky=tkinter.W,padx=5)


frame = tkinter.Frame()
frame.grid(row=3,column=0)

def radio_used():
    value = radio_state.get()
    print('used')
    if value == 1:
        ending_currency_label['text'] = 'EUROS:'
        starting_currency_label['text'] = 'USD:'
    else:
        ending_currency_label['text'] = 'USD:'
        starting_currency_label['text'] = 'EUROS:'


    ending_currency_result['text']= '0.00'


def from_changed(*args):
    starting_currency_label['text'] = f"{from_variable.get()}:"
    ending_currency_result['text'] = '0.00'

    




def to_changed(*args):
    ending_currency_label['text'] = f"{to_variable.get()}:"
    ending_currency_result['text'] = '0.00'

from_variable = tkinter.StringVar()
from_variable.set('USD')

from_variable.trace('w',from_changed)

option_menu_1_label = tkinter.Label(text='FROM:',font=font)
option_menu_1_label.grid(row=3,column=0)
option_menu_1 = tkinter.OptionMenu(window,from_variable,*SYMBOLS)
option_menu_1.config(font=font)
option_menu_1.grid(row=3,column=1,sticky=tkinter.W)


to_variable = tkinter.StringVar()
to_variable.trace('w',to_changed)


to_variable.set('EUR')
option_menu_2_label = tkinter.Label(text='TO:',font=font)
option_menu_2_label.grid(row=4,column=0)
option_menu_2 = tkinter.OptionMenu(window,to_variable,*SYMBOLS)

option_menu_2.config(font=font)
option_menu_2.grid(row=4,column=1,sticky=tkinter.W)


'''
radio_state = tkinter.IntVar()
radio_state.set(1)
radiobutton1 = tkinter.Radiobutton(frame,text='USD to EURO',value=1,variable=radio_state,command=radio_used,font=font)
radiobutton1.grid(row=0,column=0)
radiobutton2 = tkinter.Radiobutton(frame,text='EURO to USD',value=2,variable=radio_state,command=radio_used,font=font)
radiobutton2.grid(row=1,column=0)
'''
convert_button = tkinter.Button(text='CONVERT',font=font,command=convert)
convert_button.grid(row=5,column=0,columnspan=2)














window.mainloop()



