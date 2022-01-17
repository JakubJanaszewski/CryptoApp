from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar
from cryptocurrency import *

def option_menu_changed(changed_value: str = None):
    cryptocurrency = get_cryptocurrency(cryptocurrencies, chosen_crypto_name.get(), chosen_currency.get())
    equation.set("1 " + cryptocurrency.symbol + " = " + str(cryptocurrency.price.__round__(2)) + " " + chosen_currency.get())
    chosen_crypto_volume.set(cryptocurrency.volume_24h.__round__(2))
    chosen_crypto_change_1h.set(cryptocurrency.percent_change_1h.__round__(2))
    chosen_crypto_change_24h.set(cryptocurrency.percent_change_24h.__round__(2))
    chosen_crypto_change_7d.set(cryptocurrency.percent_change_7d.__round__(2))
    chosen_crypto_change_30d.set(cryptocurrency.percent_change_30d.__round__(2))
    change_background()

def change_background():
    label_change_1h.config(bg="green") if float(chosen_crypto_change_1h.get()) > 0 else label_change_1h.config(bg="red")
    label_change_24h.config(bg="green") if float(chosen_crypto_change_24h.get()) > 0 else label_change_24h.config(bg="red")
    label_change_7d.config(bg="green") if float(chosen_crypto_change_7d.get()) > 0 else label_change_7d.config(bg="red")
    label_change_30d.config(bg="green") if float(chosen_crypto_change_30d.get()) > 0 else label_change_30d.config(bg="red")

def button_clicked(progressbar: Progressbar):
    global cryptocurrencies, crypto_names
    cryptocurrencies, crypto_names = refresh_data()
    option_menu_changed()
    progressbar['value'] = 0

def refresh_loop(progressbar: Progressbar):
    global cryptocurrencies, crypto_names
    while True:
        option_menu_changed()
        progressbar['value']=0
        step = 0.1
        while progressbar['value'] <= progressbar['maximum']:
            sleep(step)
            progressbar['value']+=step
            app.update()
        cryptocurrencies, crypto_names = refresh_data()

def refresh_data() -> tuple[list[Cryptocurrency], list[str]]:
    cryptocurrencies_tmp = build_cryptocurrencies()
    return cryptocurrencies_tmp, get_cryptocurrency_name_list(cryptocurrencies_tmp)

def build_application():
    app.title("Crypto App")
    app.iconphoto(False, PhotoImage(file='logo.png'))

    Label(app, text="Currency:").grid(row=0,column=0,sticky=W,ipadx=2,ipady=4)
    Label(app, text="Cryptocurrency:").grid(row=1,column=0,sticky=W,ipadx=2,ipady=4)
    Label(app, textvariable=equation).grid(row=2,columnspan=2,sticky=EW,ipadx=2,ipady=4)
    Label(app, text="Volume (24h):").grid(row=3,column=0,sticky=W,ipadx=2,ipady=4)
    Label(app, text="Percent change (1h):").grid(row=4,column=0,sticky=W,ipadx=2,ipady=4)
    Label(app, text="Percent change (24h):").grid(row=5,column=0,sticky=W,ipadx=2,ipady=4)
    Label(app, text="Percent change (7d):").grid(row=6,column=0,sticky=W,ipadx=2,ipady=4)
    Label(app, text="Percent change (30d):").grid(row=7,column=0,sticky=W,ipadx=2,ipady=4)

    OptionMenu(app, chosen_currency, *["USD", "EUR", "PLN"], command=option_menu_changed).grid(row=0, column=1,sticky=EW)
    OptionMenu(app, chosen_crypto_name, *crypto_names, command=option_menu_changed).grid(row=1, column=1, sticky=EW)

    global label_change_1h, label_change_24h, label_change_7d, label_change_30d
    Label(app, textvariable=chosen_crypto_volume).grid(row=3,column=1, sticky=EW,ipadx=2,ipady=4)
    label_change_1h = Label(app, textvariable=chosen_crypto_change_1h, width=20)
    label_change_1h.grid(row=4, column=1, sticky=EW)
    label_change_24h = Label(app, textvariable=chosen_crypto_change_24h)
    label_change_24h.grid(row=5, column=1, sticky=EW)
    label_change_7d = Label(app, textvariable=chosen_crypto_change_7d)
    label_change_7d.grid(row=6, column=1, sticky=EW)
    label_change_30d = Label(app, textvariable=chosen_crypto_change_30d)
    label_change_30d.grid(row=7, column=1, sticky=EW)


    progressbar = Progressbar(app, mode='determinate')
    progressbar.grid(row=9, sticky=EW, columnspan=2)
    progressbar['maximum'] = 60

    Button(app, text='Refresh', command= lambda:button_clicked(progressbar)).grid(row=8, sticky=EW, columnspan=2)

    try:
        refresh_loop(progressbar)
    except TclError:
        pass

app = Tk()
cryptocurrencies = build_cryptocurrencies()
crypto_names = get_cryptocurrency_name_list(cryptocurrencies)

chosen_currency = StringVar()
chosen_currency.set("USD")
chosen_crypto_name = StringVar()
chosen_crypto_name.set("Bitcoin")
equation = StringVar()
chosen_crypto_volume = StringVar()
chosen_crypto_change_1h = StringVar()
chosen_crypto_change_24h = StringVar()
chosen_crypto_change_7d = StringVar()
chosen_crypto_change_30d = StringVar()
build_application()