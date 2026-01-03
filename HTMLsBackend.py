class HTMLsBackend:
    def __init__(self):
        self.paper_measure = []
        self.working_measure = ' '

    def paperInserter(self, argument):
        self.paper_measure.append(argument)

    def paperGiver(self):
        return self.paper_measure

    def paperClear(self):
        self.paper_measure.clear()

    def setWorkingMeasure(self, argument):
        self.working_measure = argument