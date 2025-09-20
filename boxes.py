class draggableArea:
    boxes = []

    def __init__(self, name):
        self.name = name

    def newBox(self, x, y, name, oX, oY,):
        box = dragBox(x, y, name, oX, oY, self)
        self.boxes.append(box)




class dragBox:

    def __init__(self, posX, posY, name,oX, oY, area):

        self.posX = posX
        self.posY = posY
        self.name = name
        self.orientationX = oX
        self.orientationY = oY
        self.parentDrag = area
        self.text = ' '
        self.font = ' '
        self.size = ' '

    def __str__(self):
        return f"{self.name}"


#if __name__ == '__main__':
#    drag = draggableArea()
#    print(drag)
#    drag.newBox(15, 15)
#    drag.boxes[0].moveSelf(35, 23)
#    drag.boxes[0].moveSelf(305, -3)

