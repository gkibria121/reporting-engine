
from ..base import IFormatter

class Default(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,condition,format_sepec):


        return value,condition,format_sepec

    def set_successor(self,successor):
        pass
