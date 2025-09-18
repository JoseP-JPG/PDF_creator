class draggableArea:
    boxes = []

    def __init__(self, x, y):
        self.sizeX = x
        self.sizeY = y

    def newBox(self, x, y):
        box = dragBox(x, y, self)
        self.boxes.append(box)
        print(f"I have a {box.sizeX}x{box.sizeY} box, the measurements are percentage.")

    def __str__(self):
        return f"I am a {self.sizeX}x{self.sizeY} area."


class dragBox:

    def __init__(self, x, y, posX, posY, oX, oY, area):
        self.sizeX = x
        self.sizeY = y
        self.posX = posX
        self.posY = posY
        self.orientationX = oX
        self.orientationY = oY
        self.parentDrag = area


    def moveSelf(self, x, y):
        limitX = self.parentDrag.sizeX
        limitY = self.parentDrag.sizeY
        if x > limitX:
            self.posX = limitX
        elif x < 0:
            self.posX = 0
        else:
            self.posX = x

        if y > limitY:
            self.posY = limitY
        elif y < 0:
            self.posY = 0
        else:
            self.posY = y
        print(self.posX)
        print(self.posY)


#if __name__ == '__main__':
#    drag = draggableArea()
#    print(drag)
#    drag.newBox(15, 15)
#    drag.boxes[0].moveSelf(35, 23)
#    drag.boxes[0].moveSelf(305, -3)

