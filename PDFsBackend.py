from boxes import draggableArea

class PDFsBackend:
    def __init__(self):
        self.area = None

    def areaMaker(self, argument):
        self.area = draggableArea(argument[0], argument[1], argument[2])

    def boxesGiver(self):
        return self.area.boxes

    def lengthGiver(self):
        return len(self.area.boxes)