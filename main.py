from calculator.sk_calculator import Calculator
from variable.sk_variable_handler.variable_handler import VariableHandler
from reporter.sk_report_generator import ReportGenerator
from declaration.sk_declaration import DeclarationGenerator


class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.variable = VariableHandler()
        self.variable.set_calculator(self.calculator)
        self.reporter = ReportGenerator()
        self.random_declarations = DeclarationGenerator()

    def get_data(self, declaration_string):
        return self.variable.get_result(declaration_string)

    def get_report(self, template, data):
        return self.reporter.generate_report(template, data)

    def get_declarations(self, text):
        declarations = self.random_declarations.generate(text)
        return declarations


Controller = Controller()
data = {'$person' : {'name' : 'kibria','age' : 23, 'city' : 'dhaka','country' : 'bangladesh'}};
template = '''{{$person}}'''
declaration = Controller.get_report(template,data)

print(declaration)

