class draggableArea:
    boxes = []

    def __init__(self, x, y):
        self.sizeX = x
        self.sizeY = y

    def newBox(self, x, y):
        box = dragBox(x, y, self)
        self.boxes.append(box)
        print(f"I have a {box.sizeX}x{box.sizeY} box")

    def __str__(self):
        return f"I am a {self.sizeX}x{self.sizeY} area"


class dragBox:
    def __init__(self, x, y, drag):
        self.sizeX = x
        self.sizeY = y
        self.posX = self.sizeX / 2
        self.posY = self.sizeY / 2
        self.parentDrag = drag

    def moveSelf(self, x, y):
        limitX = self.parentDrag.sizeX
        limitY = self.parentDrag.sizeY
        if (x + self.sizeX / 2) > limitX:
            self.posX = limitX - self.sizeX / 2
        elif (x - self.sizeX / 2) < 0:
            self.posX = self.sizeX / 2
        else:
            self.posX = x

        if (y + self.sizeY / 2) > limitY:
            self.posY = limitY - self.sizeY / 2
        elif (y - self.sizeY / 2) < 0:
            self.posY = self.sizeY / 2
        else:
            self.posY = y
        print(self.posX)
        print(self.posY)


if __name__ == '__main__':
    drag = draggableArea(100, 100)
    print(drag)
    drag.newBox(15, 15)
    drag.boxes[0].moveSelf(35, 23)
    drag.boxes[0].moveSelf(305, -3)

