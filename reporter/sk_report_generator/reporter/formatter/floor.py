from ..base import IFormatter

class Floor(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,condition,format_sepec):
        if condition == None:
            print(value)
        return self.successor.format(value,condition,format_sepec)

    def set_successor(self,successor):
        self.successor= successor