class draggableArea:
    boxes = []

    def __init__(self, unit, width, height):
        self.unit = unit
        self.width = width
        self.height = height

    def newBox(self, x, y, name, oX, oY,):
        box = dragBox(x, y, name, oX, oY)
        self.boxes.append(box)

class dragBox:

    def __init__(self, posX, posY, name,oX, oY):

        self.posX = posX
        self.posY = posY
        self.name = name
        self.orientationX = oX
        self.orientationY = oY
        self.text = ' '
        self.font = ' '
        self.size = ' '

    def __str__(self):
        return f"{self.name}"

    def nameGetter(self):
        return self.name

    def nameSetter(self, name):
        self.name = name

#if __name__ == '__main__':
#    drag = draggableArea()
#    print(drag)
#    drag.newBox(15, 15)
#    drag.boxes[0].moveSelf(35, 23)
#    drag.boxes[0].moveSelf(305, -3)

