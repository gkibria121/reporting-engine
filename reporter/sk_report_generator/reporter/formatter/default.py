
from ..base import IFormatter

class Default(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,condition,format_sepec,format_pattern=''):


        return value,condition,format_sepec

    def handle(self,value,condition,format_sepec,format_pattern):

        return format_pattern
    def set_successor(self,successor):
        pass
