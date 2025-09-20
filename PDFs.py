import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import Tk, font

from boxes import draggableArea


class pdfMaker:

    def __init__(self):
        self.paper_measure = []
        self.working_measure = ' '
        self.area = ''

        self.html_component1 = ' '
        self.html_component2 = ' '
        self.html_component3 = ' '
        self.css_component1 = ' '
        self.css_component2 = ' '
        self.css_component3 = ' '

        self.open_screen()

    def html_maker(self):
        print('html maker')


    def css_maker(self):
        print('css maker')

    def main_screen(self):
        print('main window')
        mai = tkinter.Tk()

        pw1 = PanedWindow(mai)
        pw1.grid(column=0, row=0, columnspan=2, rowspan=2)
        button_newbox = ttk.Button(mai, text='New Box')
        button_newbox.grid(row=0, column=0, columnspan=2)
        button_removebox = ttk.Button(mai, text='Remove Box')
        button_removebox.grid(row=1, column=0, columnspan=2)

        def box_list(event):
            print('box chosen')

        pw2 = PanedWindow(mai)
        pw2.grid(column=0, row=2, columnspan=2, rowspan=5)
        pw3 = PanedWindow(mai)
        pw3.grid(column=2, row=0, columnspan=8, rowspan=2)
        pw4 = PanedWindow(mai)
        pw4.grid(column=2, row=2, columnspan=4, rowspan=5)
        pw5 = PanedWindow(mai)
        pw5.grid(column=5, row=2, columnspan=4, rowspan=5)

        mai.mainloop()

    def newbox_screen(self):
        print('new box screen')

    def save_screen(self):
        print('save screen')

    def open_screen(self):
        print('open screen')
        self.paper_measurements()

    def paper_measurements(self):
        print('paper measurements')
        pap = tkinter.Tk()
        pmeasure = ['mm', 'px']
        w = tkinter.Label(pap, text='what are your measurements? (mm, px)')
        w.grid(row=0, column=0, columnspan=2)

        def pselect(event):
            selected_item = combo_box.get()
            label.config(text="Selected Item: " + selected_item)

        def pbutton(event):

            selected_item1 = combo_box.get()
            selected_item2 = e1.get()
            selected_item3 = e2.get()
            try:
                label.config(text="Selected Item: " + selected_item1)

                self.paper_measure.append(selected_item1)
                self.paper_measure.append(int(selected_item2))
                self.paper_measure.append(int(selected_item3))
                self.area = draggableArea(self.paper_measure[1], self.paper_measure[2])
                pap.destroy()
                #print(self.paper_measure)
                self.working_measurements()
            except:
                self.paper_measure.clear()
                label.config(text="""The measurements were not numbers.
                Selected Item: """ + selected_item1)

        label = tkinter.Label(pap, text="Selected Item: ")
        label.grid(row=1, column=0, columnspan=2)

        combo_box = ttk.Combobox(pap, values=pmeasure, state='readonly')
        combo_box.grid(row=2, column=0, columnspan=2)

        combo_box.set(pmeasure[0])

        combo_box.bind("<<ComboboxSelected>>", pselect)

        Label(pap, text='Width').grid(row=3)
        Label(pap, text='Height').grid(row=4)
        e1 = Entry(pap)
        #e1.insert(0, "test")
        #e1.configure(state="disabled")
        e1.grid(row=3, column=1)
        e2 = Entry(pap)
        e2.grid(row=4, column=1)

        button_savemeasurements = ttk.Button(pap, text='Save', width=25)
        button_savemeasurements.grid(row=5, column=0, columnspan=2)
        button_savemeasurements.bind("<Button-1>", pbutton)

        pap.title("Measurements")
        pap.mainloop()

    def working_measurements(self):
        print('working measurements')
        mea = tkinter.Tk()
        wmeasure = ['mm', 'px', '%']
        w = tkinter.Label(mea, text='what are your working measurements? (mm, px, %)')
        w.pack()

        '''
        m2 = PanedWindow(mea, orient=HORIZONTAL)

        def wbuttonm(event):
            ff = ws.get()-1
            ws.set(ff)
            print(ws.get())

        button2 = ttk.Button(mea, text='<', width=25)
        m2.add(button2)
        button2.bind("<Button-1>", wbuttonm)
        m2.pack()

        ws = Scale(mea, from_=0, to=200, orient=HORIZONTAL)
        ws.set(50)
        m2.add(ws)

        def wbuttonM(event):
            ff = ws.get()+1
            ws.set(ff)
            print(ws.get())

        button = ttk.Button(mea, text='>', width=25)
        m2.add(button)
        button.bind("<Button-1>", wbuttonM)
        m2.pack()
        '''

        def wselect(event):
            selected_item = combo_box.get()
            label.config(text="Selected Item: " + selected_item)
            self.working_measure = combo_box.get()
            mea.destroy()
            self.main_screen()

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


