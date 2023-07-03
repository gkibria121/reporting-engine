from .base import IReporter
import regex as re


class Formatter(IReporter):
    def __init__(self):
        self.successor = None

    def report(self, template):
        format_pattern = r'(?<=[^\{]\{\{)[^{}]+:[^{}]+(?=\}\}[^\}])'
        matches = re.findall(format_pattern, template)

        for match in matches:

            value, formula = match.replace(' ', '').split(':')
            try:
                value = eval(value)
                formula = formula
                replacement = format(value, formula)

            except ValueError as error:
                error_message = str(error)
                replacement = f'({value}, {error_message})'

            except TypeError as error:
                error_message = str(error)
                replacement = f'({value}, {error_message})'

            pattern = r'({{)\s*' + re.escape(match) + '\s*(}})'
            template = re.sub(pattern, replacement, template)

        return self.successor.report(template)

    def set_successor(self, successor):
        self.successor = successor
        pass

    def set_data(self, data):
        pass
