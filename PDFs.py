import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class pdfMaker:

    def __init__(self):
        self.paper_measure = []
        self.working_measure = ' '
        self.area = ''
        self.paper_measurements()

    def html_maker(self):
        print('html maker')


    def css_maker(self):
        print('css maker')

    def paper_measurements(self):
        print('paper measurements')
        pap = tkinter.Tk()
        pmeasure = ['mm', 'px']
        w = tkinter.Label(pap, text='what are your measurements? (mm, px)')
        w.grid(row=0, column=0, columnspan=2)

        def pselect(event):
            selected_item = combo_box.get()
            label.config(text="Selected Item: " + selected_item)
            #self.paper_measure = combo_box.get()
            #pap.quit()
            #self.working_measurements()

        def pbutton(event):
            selected_item1 = combo_box.get()
            selected_item2 = e1.get()
            selected_item3 = e2.get()
            label.config(text="Selected Item: " + selected_item1)
            self.paper_measure.append(selected_item2)
            self.paper_measure.append(selected_item3)
            print(self.paper_measure)
            pap.quit()
            self.working_measurements()

        label = tkinter.Label(pap, text="Selected Item: ")
        label.grid(row=1, column=0, columnspan=2)

        combo_box = ttk.Combobox(pap, values=pmeasure, state='readonly')
        combo_box.grid(row=2, column=0, columnspan=2)

        combo_box.set(pmeasure[0])

        combo_box.bind("<<ComboboxSelected>>", pselect)

        Label(pap, text='Width').grid(row=3)
        Label(pap, text='Height').grid(row=4)
        e1 = Entry(pap)
        e1.grid(row=3, column=1)
        e2 = Entry(pap)
        e2.grid(row=4, column=1)

        button = ttk.Button(pap, text='Save', width=25)
        button.grid(row=5, column=0, columnspan=2)
        button.bind("<Button-1>", pbutton)

        pap.title("Measurements")
        pap.mainloop()

    def working_measurements(self):
        print('working measurements')
        mea = tkinter.Tk()
        wmeasure = ['mm', 'px', '%']
        w = tkinter.Label(mea, text='what are your measurements? (mm, px, %)')
        w.pack()

        def wselect(event):
            selected_item = combo_box.get()
            label.config(text="Selected Item: " + selected_item)
            self.working_measure = combo_box.get()
            mea.quit()

        # Create a label
        label = tkinter.Label(mea, text="Selected Item: ")
        label.pack(pady=10)

        # Create a Combobox widget
        combo_box = Combobox(mea, values=wmeasure, state='readonly')
        combo_box.pack(pady=5)

        # Set default value
        combo_box.set(wmeasure[0])

        # Bind event to selection
        combo_box.bind("<<ComboboxSelected>>", wselect)

        mea.title("Measurements")
        mea.mainloop()

'''
    def pdf_maker_main(self):
        print('main pdf function')


        #print('what are your measurements? (mm, px, %)')
        print('what is the width')
        print('what is the height')
        print('how many boxes')
        print('for this box...')
        print('from the left or right?')
        print('what is the posX?')
        print('from the top or bottom?')
        print('what is the posY?')
'''


