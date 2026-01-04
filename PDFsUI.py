import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import Tk, font

from HTMLsBackend import HTMLsBackend
from PDFsBackend import PDFsBackend


class pdfMaker:

    def __init__(self):
        self.PdF = PDFsBackend()
        self.HtML = HTMLsBackend()

        self.open_screen()

    def html_maker(self):
        print('html maker')


    def css_maker(self):
        print('css maker')

    def main_screen(self):
        print('main window')

        self.PdF.area.newBox(0, 0, 'box1', 'left', 'top')
        current_box= 0
        mai = tkinter.Tk()
        mai.resizable(False, False)

        pw1 = Frame(mai)
        pw1.grid(column=0, row=0)

        nameBox_sv = StringVar()
        nameBox = Entry(pw1, textvariable=nameBox_sv)
        nameBox.insert(0, self.PdF.area.boxes[0].name)
        nameBox.pack()

        button_newbox = ttk.Button(pw1, text='New Box')
        button_newbox.pack()
        button_removebox = ttk.Button(pw1, text='Remove Box')
        button_removebox.pack()

        pw2 = Frame(mai)
        pw2.grid(column=0, row=1)
        listOfBoxes = Listbox(pw2, selectmode=SINGLE)
        listOfBoxes.insert(0, self.PdF.area.boxes[0].name)
        listOfBoxes.pack(side=BOTTOM)

        pw3 = Frame(mai)
        pw3.grid(column=1, row=0)

        textBox = Text(pw3)
        textBox.insert(INSERT, 'Text')
        textBox.pack()

        pw4 = Frame(mai)
        pw4.grid(column=1, row=1)

        font_frame = Frame(pw4)
        font_frame.pack(side=LEFT)
        searchBox_sv = StringVar()
        searchBox = Entry(font_frame, textvariable=searchBox_sv)
        searchBox.pack()

        fonts = list(font.families())
        fonts.sort()
        listOfFonts = Listbox(font_frame, selectmode=SINGLE)
        for font1 in fonts:
            listOfFonts.insert(END, font1)
        listOfFonts.pack()

        def nameChange(var, index, mode):
            print (nameBox_sv.get())
            self.PdF.area.boxes[current_box].nameSetter(nameBox_sv.get())
            print(self.PdF.area.boxes[current_box].nameGetter())
            listOfBoxes.delete(current_box)
            listOfBoxes.insert(current_box, nameBox_sv.get())

        def fontSearch(var, index, mode):
            print(searchBox_sv.get())
            print (searchBox_sv.get()=='')
            if searchBox_sv.get() == '':
                listOfFonts.delete(0, 'end')
                for font2 in fonts:
                    listOfFonts.insert(END, font2)
            else:
                listOfFonts.delete(0, 'end')
                for font3 in fonts:
                    if searchBox_sv.get().lower() in font3.lower():
                        listOfFonts.insert(END, font3)

        def newBoxOnList(event):
            self.PdF.area.newBox(0, 0, 'box'+str(self.PdF.lengthGiver()+1), 'left', 'top')
            listOfBoxes.delete(0, 'end')
            for box in self.PdF.boxesGiver():
                print(box.nameGetter())
                listOfBoxes.insert(END, box.nameGetter())

        def selectTheFont(event):
            Selected = [listOfFonts.get(i) for i in listOfFonts.curselection()]
            print(Selected[0])
            self.PdF.area.boxes[current_box].fontSetter(Selected[0])
            searchBox.delete(0, 'end')
            searchBox.insert(0, Selected[0])
            listOfFonts.delete(0, 'end')
            for font2 in fonts:
                listOfFonts.insert(END, font2)

        def saveText(event):
            self.PdF.area.boxes[current_box].textSetter(textBox.get('1.0', 'end' + "-1c"))
            print(self.PdF.area.boxes[current_box].text)


        nameBox_sv.trace_add("write", nameChange)
        searchBox_sv.trace_add("write", fontSearch)
        button_newbox.bind("<Button-1>", newBoxOnList)
        textBox.bind('<KeyRelease>', saveText)
        listOfFonts.bind('<<ListboxSelect>>', selectTheFont)
        '''listOfBoxes.bind('<<ListboxSelect>>', swapBox)'''

        mai.title("Create the .PDF")
        mai.mainloop()

    def save_screen(self):
        print('save screen')

    def open_screen(self):
        print('open screen')
        self.paper_measurements()

    def paper_measurements(self):
        print('paper measurements')
        pap = tkinter.Tk()
        pap.resizable(False, False)
        pmeasure = ['mm', 'px']
        w = tkinter.Label(pap, text='what are your measurements? (mm, px)')
        w.pack()

        def pselect(event):
            selected_item = combo_box.get()
            label.config(text="Selected Item: " + selected_item)

        def pbutton(event):

            selected_item1 = combo_box.get()
            selected_item2 = e1.get()
            selected_item3 = e2.get()
            try:
                label.config(text="Selected Item: " + selected_item1)

                self.HtML.paperInserter(selected_item1)
                self.HtML.paperInserter(int(selected_item2))
                self.HtML.paperInserter(int(selected_item3))
                self.PdF.areaMaker(self.HtML.paperGiver())
                pap.destroy()
                #print(self.paper_measure)
                self.working_measurements()

            except:
                self.HtML.paperClear()
                label.config(text="""The measurements were not numbers.
                Selected Item: """ + selected_item1)

        label = tkinter.Label(pap, text="Selected Item: ")
        label.pack()

        combo_box = ttk.Combobox(pap, values=pmeasure, state='readonly')
        combo_box.pack()

        combo_box.set(pmeasure[0])

        combo_box.bind("<<ComboboxSelected>>", pselect)

        frame = tkinter.Frame(pap)
        Label(frame, text='Width').grid(row=0)
        Label(frame, text='Height').grid(row=1)
        e1 = Entry(frame)
        #e1.insert(0, "test")
        #e1.configure(state="disabled")
        e1.grid(row=0, column=1)
        e2 = Entry(frame)
        e2.grid(row=1, column=1)
        frame.pack()

        button_savemeasurements = ttk.Button(pap, text='Save', width=25)
        button_savemeasurements.pack()
        button_savemeasurements.bind("<Button-1>", pbutton)

        pap.title("Measurements")
        pap.mainloop()

    def working_measurements(self):
        print('working measurements')
        mea = tkinter.Tk()
        mea.resizable(False, False)
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
            self.HtML.working_measure = combo_box.get()
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


