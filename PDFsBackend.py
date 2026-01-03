from boxes import draggableArea


class PDFsBackend:
    def __init__(self):
        self.area = None

    def areaMaker(self, unit, width, height):
        self.area = draggableArea(unit, width, height)

    def lengthGiver(self):
        return len(self.area.boxes)