import regex as re


class WidthHandler:


    def handle(self,value,condition,format_specs,format_pattern):
        if 'width'  in format_specs:
            format_pattern = re.sub(r'\{width\}',str(format_specs['width']),format_pattern)
        else:
            format_pattern = re.sub(r'\{width\}','',format_specs)

        return self.successor.handle(value,condition,format_specs,format_pattern)

    def set_successor(self,successor):
        self.successor = successor


