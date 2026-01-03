class HTMLsBackend:
    def __init__(self):
        self.paper_measure = []
        self.working_measure = ' '

    def paperInserter(self, argument):
        self.paper_measure.append(argument)

    def setWorkingMeasure(self, argument):
        self.working_measure = argument