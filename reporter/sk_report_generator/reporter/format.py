from .base import IReporter
from .formatter.floor import Floor
from .formatter.ceil import Ceil
from .formatter.default import Default
import regex as re


class Formatter(IReporter):
    def __init__(self):
        self.successor = None
        self.floor = Floor()
        self.ceil = Ceil()
        self.default = Default()




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

                condition,format_spec_list = self.process(format_spec)
                result = ''

                for format_spec in format_spec_list:
                    result = self.floor.format(value,condition,format_spec)

                replacement = ''


            pattern =r'({)\s*'+re.escape(match[1])+r'\s*(})'
            template = re.sub(pattern, replacement , template)


        return self.successor.report(template)

    def set_successor(self, successor):
        self.successor = successor
        self.floor.set_successor(self.ceil)
        self.ceil.set_successor(self.default)

    def set_data(self, data):
        pass


    def process(self,format_spec):

        matches = re.split(',',format_spec)
        condition = re.search(r'c(\(((?>[^()]+|(?1))*)\))',format_spec)
        format_spec_list = matches
        if condition:
            condition = condition[2]

            format_spec_list = matches[1:]



        return condition,format_spec_list
