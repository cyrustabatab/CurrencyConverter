import tkinter,requests
from tkinter import messagebox
import json
from PIL import Image,ImageTk

def convert():
    
    try:
        dollars = float(starting_currency_entry.get())
    except ValueError:
        messagebox.showerror(title='Oops',message='Please enter a NUMBER!')
        starting_currency_entry.delete(0,tkinter.END)
    else:
        if dollars < 0:
            messagebox.showerror(title='Oops',message='Please enter a POSITIVE NUMBER!')
            starting_currency_entry.delete(0,tkinter.END)
        else:
            url = 'https://api.exchangeratesapi.io/latest'
            d = {'base': 'USD'}
            response = requests.get(url,params=d)
            exchange_rates = json.loads(response.text)
            print(exchange_rates)


##
            exchange_rate =euros_per_dollar = exchange_rates['rates']['EUR']
            radio_value = radio_state.get()
            if radio_value == 2:
                exchange_rate = 1 / exchange_rate

            euros = dollars * exchange_rate
            ending_currency_result['text'] = f"{euros:.2f}"

     
    








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



radio_state = tkinter.IntVar()
radio_state.set(1)
radiobutton1 = tkinter.Radiobutton(frame,text='USD to EURO',value=1,variable=radio_state,command=radio_used,font=font)
radiobutton1.grid(row=0,column=0)
radiobutton2 = tkinter.Radiobutton(frame,text='EURO to USD',value=2,variable=radio_state,command=radio_used,font=font)
radiobutton2.grid(row=1,column=0)

convert_button = tkinter.Button(text='CONVERT',font=font,command=convert)
convert_button.grid(row=3,column=1)











window.mainloop()



