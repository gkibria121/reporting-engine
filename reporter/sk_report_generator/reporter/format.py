from .base import IReporter
from .formatter.floor import Floor
from .formatter.ceil import Ceil
from .formatter.width import WidthHandler
from .formatter.default import Default
import regex as re


class Formatter(IReporter):
    def __init__(self):
        self.successor = None
        self.floor = Floor()
        self.ceil = Ceil()
        self.default = Default()
        self.width_handler = WidthHandler()




    def report(self, template):

        format_pattern = r'(?![}])(\{(\{((?:[^{}]|(?2))*)\:([^{}]*)\})\})(?![}])'

        matches = re.findall(format_pattern, template)

        for match in matches:
            value = match[2]
            format_spec  = match[3]

            if re.sub(r'[\s\-\.]','',value).isdigit():
                value = int(value) if value.endswith('.0') or '.' not in value else float(value)
            try:
               replacement = format(value,format_spec)
            except ValueError:

                condition,format_specs = self.process(format_spec)
                format_pattern = '{{value}:{fill}{align}{sign}{pad}{width}{grouping_option}{precision}{type}}'
                resutl = self.width_handler.handle(value,condition,format_specs,format_pattern)
##                self.floor.format()

                replacement = ''


            pattern =r'({)\s*'+re.escape(match[1])+r'\s*(})'
            template = re.sub(pattern, replacement , template)


        return self.successor.report(template)

    def set_successor(self, successor):
        self.successor = successor
        self.floor.set_successor(self.ceil)
        self.ceil.set_successor(self.default)


        self.width_handler.set_successor(self.default)

    def set_data(self, data):
        pass


    def process(self,format_spec):
        format_list = {'f2': {'fill' : '0' , 'align' : 'left', 'sign': '+', 'pad' : '0' ,'width' : 10, 'grouping_option' : ',' ,'precision' : '.1' ,'type' : 'b'} ,'w2' :{'width' : 10}}
        matches = re.split(',',format_spec)
        condition = re.search(r'c(\(((?>[^()]+|(?1))*)\))',format_spec)

        format_spec_list = matches
        format_specs = {}
        if condition:
            condition = condition[2]
            format_spec_list = matches[1:]
        for key in format_spec_list:
            format_specs.update(format_list[key])


        return condition,format_specs
