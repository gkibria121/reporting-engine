from .base import IReporter
import regex as re


class Formatter(IReporter):
    def __init__(self):
        self.successor = None

    def report(self, template):
        format_pattern = r'(?![}])(\{(\{((?:[^{}]|(?2))*)\:([^{}()[]*)\})\})(?![}])'





        matches = re.findall(format_pattern, template)

        for match in matches:
            value = match[2]
            format_spec      = match[3]

            if re.sub(r'[\s\.\,]','',value).isdigit():
                value = int(value) if value.endswith('.0') or '.' not in value else float(value)

            replacement = format(value,format_spec)


            pattern =r'({)\s*'+re.escape(match[1])+r'\s*(})'
            template = re.sub(pattern, replacement , template)


        return self.successor.report(template)

    def set_successor(self, successor):
        self.successor = successor
        pass

    def set_data(self, data):
        pass
