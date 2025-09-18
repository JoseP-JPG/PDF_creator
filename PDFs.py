import tkinter
from tkinter import Tk, ttk


def html_maker():
    print('html maker')


def css_maker():
    print('css maker')

def paper_measurements():
    print('paper measurements')

def working_measurements():
    print('working measurements')
    mea = tkinter.Tk()
    measure = ['mm', 'px', '%']
    w = tkinter.Label(mea, text='what are your measurements? (mm, px, %)')
    w.pack()

    def select(event):
        selected_item = combo_box.get()
        label.config(text="Selected Item: " + selected_item)
        print(combo_box.get())
        mea.quit()

    # Create a label
    label = tkinter.Label(mea, text="Selected Item: ")
    label.pack(pady=10)

    # Create a Combobox widget
    combo_box = ttk.Combobox(mea, values=measure, state='readonly')
    combo_box.pack(pady=5)

    # Set default value
    combo_box.set(measure[0])

    # Bind event to selection
    combo_box.bind("<<ComboboxSelected>>", select)

    mea.title("Measurements")
    mea.mainloop()

def pdf_maker_main():
    print('main pdf function')

    paper_measurements()
    working_measurements()


    #print('what are your measurements? (mm, px, %)')
    print('what is the width')
    print('what is the height')
    print('how many boxes')
    print('for this box...')
    print('from the left or right?')
    print('what is the posX?')
    print('from the top or bottom?')
    print('what is the posY?')

pdf_maker_main()

